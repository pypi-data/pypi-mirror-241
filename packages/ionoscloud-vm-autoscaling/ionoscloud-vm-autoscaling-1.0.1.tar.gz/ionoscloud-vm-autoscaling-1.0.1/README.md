[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=alert_status)](https://sonarcloud.io/summary?id=sdk-python-vm-autoscaling)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sdk-python-vm-autoscaling)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-vm-autoscaling)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-vm-autoscaling)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-vm-autoscaling)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-vm-autoscaling&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sdk-python-vm-autoscaling)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python-vm-autoscaling.svg)](https://github.com/ionos-cloud/sdk-python-vm-autoscaling/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python-vm-autoscaling.svg)](https://github.com/ionos-cloud/sdk-python-vm-autoscaling/releases/latest)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-vm-autoscaling)](https://pypi.org/project/ionoscloud-vm-autoscaling/)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud_vm_autoscaling

The VM Auto Scaling Service enables IONOS clients to horizontally scale the number of VM replicas based on configured rules. You can use VM Auto Scaling to ensure that you have a sufficient number of replicas to handle your application loads at all times.

For this purpose, create a VM Auto Scaling Group that contains the server replicas. The VM Auto Scaling Service ensures that the number of replicas in the group is always within the defined limits.


When scaling policies are set, VM Auto Scaling creates or deletes replicas according to the requirements of your applications. For each policy, specified 'scale-in' and 'scale-out' actions are performed when the corresponding thresholds are reached.

## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud-vm-autoscaling
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-vm-autoscaling.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-vm-autoscaling.git`

Then import the package:

```python
import ionoscloud_vm_autoscaling
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud_vm_autoscaling
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_vm_autoscaling.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN'
                )
client = ionoscloud_vm_autoscaling.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_vm_autoscaling.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN')
                )
client = ionoscloud_vm_autoscaling.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

Each line in `IONOS_HTTP_PROXY_HEADERS` represents one header, where the header name and value is separated by a colon. Newline characters within a value need to be escaped. See this example:
```
Connection: Keep-Alive
User-Info: MyID
User-Group: my long\nheader value
```


### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud_vm_autoscaling.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud_vm_autoscaling.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://api.ionos.com/autoscaling*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| AutoScalingGroupsApi | [**groups_actions_find_by_id**](docs/api/AutoScalingGroupsApi.md#groups_actions_find_by_id) | **GET** /groups/{groupId}/actions/{actionId} | Get Scaling Action Details by ID |
| AutoScalingGroupsApi | [**groups_actions_get**](docs/api/AutoScalingGroupsApi.md#groups_actions_get) | **GET** /groups/{groupId}/actions | Get Scaling Actions |
| AutoScalingGroupsApi | [**groups_delete**](docs/api/AutoScalingGroupsApi.md#groups_delete) | **DELETE** /groups/{groupId} | Delete a VM Auto Scaling Group by ID |
| AutoScalingGroupsApi | [**groups_find_by_id**](docs/api/AutoScalingGroupsApi.md#groups_find_by_id) | **GET** /groups/{groupId} | Get an Auto Scaling by ID |
| AutoScalingGroupsApi | [**groups_get**](docs/api/AutoScalingGroupsApi.md#groups_get) | **GET** /groups | Get VM Auto Scaling Groups |
| AutoScalingGroupsApi | [**groups_post**](docs/api/AutoScalingGroupsApi.md#groups_post) | **POST** /groups | Create a VM Auto Scaling Group |
| AutoScalingGroupsApi | [**groups_put**](docs/api/AutoScalingGroupsApi.md#groups_put) | **PUT** /groups/{groupId} | Update a VM Auto Scaling Group by ID |
| AutoScalingGroupsApi | [**groups_servers_find_by_id**](docs/api/AutoScalingGroupsApi.md#groups_servers_find_by_id) | **GET** /groups/{groupId}/servers/{serverId} | Get VM Auto Scaling Group Server by ID |
| AutoScalingGroupsApi | [**groups_servers_get**](docs/api/AutoScalingGroupsApi.md#groups_servers_get) | **GET** /groups/{groupId}/servers | Get VM Auto Scaling Group Servers |

</details>

## Documentation For Models

All URIs are relative to *https://api.ionos.com/autoscaling*
<details >
<summary title="Click to toggle">API models list</summary>

 - [Action](docs/models/Action)
 - [ActionAmount](docs/models/ActionAmount)
 - [ActionCollection](docs/models/ActionCollection)
 - [ActionProperties](docs/models/ActionProperties)
 - [ActionResource](docs/models/ActionResource)
 - [ActionStatus](docs/models/ActionStatus)
 - [ActionType](docs/models/ActionType)
 - [ActionsLinkResource](docs/models/ActionsLinkResource)
 - [AvailabilityZone](docs/models/AvailabilityZone)
 - [BusType](docs/models/BusType)
 - [CpuFamily](docs/models/CpuFamily)
 - [DatacenterServer](docs/models/DatacenterServer)
 - [Error401](docs/models/Error401)
 - [Error401Message](docs/models/Error401Message)
 - [Error404](docs/models/Error404)
 - [Error404Message](docs/models/Error404Message)
 - [ErrorAuthorize](docs/models/ErrorAuthorize)
 - [ErrorAuthorizeMessage](docs/models/ErrorAuthorizeMessage)
 - [ErrorGroupValidate](docs/models/ErrorGroupValidate)
 - [ErrorGroupValidateMessage](docs/models/ErrorGroupValidateMessage)
 - [ErrorMessage](docs/models/ErrorMessage)
 - [ErrorMessageParse](docs/models/ErrorMessageParse)
 - [Group](docs/models/Group)
 - [GroupCollection](docs/models/GroupCollection)
 - [GroupEntities](docs/models/GroupEntities)
 - [GroupPolicy](docs/models/GroupPolicy)
 - [GroupPolicyScaleInAction](docs/models/GroupPolicyScaleInAction)
 - [GroupPolicyScaleOutAction](docs/models/GroupPolicyScaleOutAction)
 - [GroupPost](docs/models/GroupPost)
 - [GroupPostEntities](docs/models/GroupPostEntities)
 - [GroupPostResponse](docs/models/GroupPostResponse)
 - [GroupProperties](docs/models/GroupProperties)
 - [GroupPropertiesDatacenter](docs/models/GroupPropertiesDatacenter)
 - [GroupPut](docs/models/GroupPut)
 - [GroupPutProperties](docs/models/GroupPutProperties)
 - [GroupPutPropertiesDatacenter](docs/models/GroupPutPropertiesDatacenter)
 - [GroupResource](docs/models/GroupResource)
 - [Metadata](docs/models/Metadata)
 - [MetadataBasic](docs/models/MetadataBasic)
 - [MetadataState](docs/models/MetadataState)
 - [Metric](docs/models/Metric)
 - [NicFirewallRule](docs/models/NicFirewallRule)
 - [NicFlowLog](docs/models/NicFlowLog)
 - [ParseError](docs/models/ParseError)
 - [QueryUnit](docs/models/QueryUnit)
 - [ReplicaNic](docs/models/ReplicaNic)
 - [ReplicaPropertiesPost](docs/models/ReplicaPropertiesPost)
 - [ReplicaVolumePost](docs/models/ReplicaVolumePost)
 - [Server](docs/models/Server)
 - [ServerCollection](docs/models/ServerCollection)
 - [ServerProperties](docs/models/ServerProperties)
 - [ServersLinkResource](docs/models/ServersLinkResource)
 - [TargetGroup](docs/models/TargetGroup)
 - [TerminationPolicyType](docs/models/TerminationPolicyType)
 - [VolumeHwType](docs/models/VolumeHwType)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>