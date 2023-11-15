# robotframework-azure-data-factory

Robot Framework library which enables you to interface with Azure Data Factory(ADF)

# Requirements
- Python 3.7+ is required due to Azure dependencies.
- Robot Framework
- Azure Subscription

# Installation
```
pip install robotframework-adf-library
```

# Examples
```RobotFramework
*** settings ***
Library     AzureDataFactoryLibrary
Library     Collections

Suite Setup     Connect To Adf    <subscription_id>    <resource_group_name>    <datafactory_name>

*** Test Cases ***
Run testcase and expect the ADF pipeline to succeed
    Start Pipeline And Expect It To Succeed    <pipeline_name>

Run testcase and expect the ADF pipeline to fail
    Start Pipeline And Expect It To Fail    <pipeline_name>
    
Run testcase and the name check if a pipeline exists
    @{lijst van pipelines} =    Get Pipelines Of Adf Instance
    List Should Contain Value    ${lijst van pipelines}    <pipeline_name>
```

# Known limitations
- Authentication with ADF is done via User Authentication via the browser. Future updates will include other ways of authentication.
- Only one connection with ADF is possible for the keywords to work at the moment. Future updates will remedy this limitation.

# Further references
- [Homepage for Azure Data Factory](https://azure.microsoft.com/en-us/products/data-factory)
- [Python SDK for Azure Data Factory](https://pypi.org/project/azure-mgmt-datafactory/)
- [Python SDK for Azure Identities](https://pypi.org/project/azure-identity/)