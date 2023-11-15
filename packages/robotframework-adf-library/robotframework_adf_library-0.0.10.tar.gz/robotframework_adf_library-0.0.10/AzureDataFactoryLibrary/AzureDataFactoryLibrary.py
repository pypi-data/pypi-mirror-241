from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.identity import DefaultAzureCredential
from robot.api import logger
from robot.api.deco import library, keyword
from datetime import timedelta, date
import time


@library
class AzureDataFactoryLibrary:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.credential = None
        self.client = None
        self.resource_group_name = None
        self.datafactory_name = None

    @keyword
    def connect_to_adf(self, subscription_id: str, resource_group_name: str, datafactory_name: str):
        """
        Keyword that connects with a Azure Data Factory(ADF). You do not need to disconnect after you are done with
        your test.

        ``subscription_id`` The Subscription Id to which the ADF belongs to

        ``resource_group_name`` The Resource Group Name to which the ADF belongs to

        ``data_factory_name`` The name of the ADF instance
        """
        self.resource_group_name = resource_group_name
        self.datafactory_name = datafactory_name
        self.credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        self.client = DataFactoryManagementClient(credential=self.credential, subscription_id=subscription_id)

    @keyword
    def get_pipelines_of_adf_instance(self):
        """
        Keyword that returns all the pipelines of an Azure Data Factory. Make sure to connect to the ADF first.

        ``returns`` List of pipelines in the Azure Data Factory
        """
        response = self.client.pipelines.list_by_factory(resource_group_name=self.resource_group_name,
                                                          factory_name=self.datafactory_name)

        list_of_pipelines = []
        for pipeline in response:
            list_of_pipelines.append(pipeline.name)
        return list_of_pipelines


    @keyword
    def start_pipeline_and_expect_it_to_succeed(self, pipeline_name: str, parameters: dict = None,
                                               refresh_rate_in_seconds: int = 15, timeout_in_minutes: int = 60):
        """
        Keyword that starts an Azure Data Factory(ADF) pipeline and waits until it has succeeded or the timeout has been
        reached. Make sure to connect to the ADF first.

        ``pipeline_name`` Name of the pipeline that you want to start

        ``pipeline_parameters`` Optional parameters that can be added to the run of the pipeline. Default no
        parameters are added to the pipeline run.

        ``refresh_rate`` Optional parameter that specifies how often the run status is checked. Default values is 15.

        ``timeout`` Optional parameter that specifies the timelimit before the keywords has a timeout. Default values is 60.
        """
        status = self.start_pipeline_and_wait_for_completion(pipeline_name, parameters, refresh_rate_in_seconds, timeout_in_minutes)
        assert status == "Succeeded"

    @keyword
    def start_pipeline_and_expect_it_to_fail(self, pipeline_name: str, parameters: dict = None,
                                               refresh_rate_in_seconds: int = 15, timeout_in_minutes: int = 60):
        """
        Keyword that starts an Azure Data Factory(ADF) pipeline and waits until it has failed or the timeout has been
        reached. Make sure to connect to the ADF first.

        ``pipeline_name`` Name of the pipeline that you want to start

        ``pipeline_parameters`` Optional parameters that can be added to the run of the pipeline. Default no
        parameters are added to the pipeline run.

        ``refresh_rate`` Optional parameter that specifies how often the run status is checked. Default values is 15.

        ``timeout`` Optional parameter that specifies the timelimit before the keywords has a timeout. Default values is 60.
        """
        status = self.start_pipeline_and_wait_for_completion(pipeline_name, parameters, refresh_rate_in_seconds, timeout_in_minutes)
        assert status == "Failed"

    def start_pipeline_and_wait_for_completion(self, pipeline_name: str, parameters: dict,
                                               refresh_rate_in_seconds: int, timeout_in_minutes: int):
        run_id = self.client.pipelines.create_run(self.resource_group_name, self.datafactory_name, pipeline_name,
                                                  parameters=parameters).run_id
        seconds_run = 0
        refresh_rate = timedelta(seconds= refresh_rate_in_seconds)
        timeout = timedelta(minutes=timeout_in_minutes)
        while seconds_run < timeout.total_seconds():
            status = self.get_status_of_pipeline(run_id)
            if status == "Succeeded" or status == "Failed" or status == "Cancelled":
                logger.info('pipeline: {} with run_id: {} is completed with status: {}'.format(pipeline_name, run_id, status))
                return status
            logger.info('pipeline: {} with run_id: {} has status: {}'.format(pipeline_name, run_id, status))
            time.sleep(refresh_rate.total_seconds())
            seconds_run += refresh_rate.total_seconds()
        status = self.get_status_of_pipeline(run_id)
        return "Timeout after {} minutes, status is {}".format(timeout_in_minutes,status)

    def get_status_of_pipeline(self, run_id: str):
        status = self.client.pipeline_runs.get(self.resource_group_name, self.datafactory_name, run_id).status
        return status
