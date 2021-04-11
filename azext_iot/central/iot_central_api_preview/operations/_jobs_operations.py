# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class JobsOperations(object):
    """JobsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~iot_central_api_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.JobCollection"]
        """Get the list of jobs in an application.

        Get the list of jobs in an application.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobCollection or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~iot_central_api_preview.models.JobCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.JobCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
                    'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
                    'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('JobCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/jobs'}  # type: ignore

    def get(
        self,
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Job"
        """Get a job by ID.

        Get details about a running or completed job by job ID.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job, or the result of cls(response)
        :rtype: ~iot_central_api_preview.models.Job
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Job"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Job', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/jobs/{job_id}'}  # type: ignore

    def set(
        self,
        job_id,  # type: str
        body,  # type: "_models.Job"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Job"
        """Execute a new job.

        Create and execute a new job via its job definition.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :param body: Job definition.
        :type body: ~iot_central_api_preview.models.Job
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job, or the result of cls(response)
        :rtype: ~iot_central_api_preview.models.Job
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Job"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.set.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Job')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Job', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    set.metadata = {'url': '/jobs/{job_id}'}  # type: ignore

    def get_devices(
        self,
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.JobDeviceStatusCollection"
        """Get device statuses.

        Get the list of individual device statuses by job ID.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobDeviceStatusCollection, or the result of cls(response)
        :rtype: ~iot_central_api_preview.models.JobDeviceStatusCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.JobDeviceStatusCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_devices.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JobDeviceStatusCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_devices.metadata = {'url': '/jobs/{job_id}/devices'}  # type: ignore

    def rerun(
        self,
        job_id,  # type: str
        rerun_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Job"
        """Rerun a job on failed devices.

        Execute a rerun of an existing job on all failed devices.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :param rerun_id: Unique ID of the job rerun.
        :type rerun_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job, or the result of cls(response)
        :rtype: ~iot_central_api_preview.models.Job
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Job"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.rerun.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
            'rerun_id': self._serialize.url("rerun_id", rerun_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Job', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    rerun.metadata = {'url': '/jobs/{job_id}/rerun/{rerun_id}'}  # type: ignore

    def stop(
        self,
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Stop a running job.

        Stop execution of a job that is currently running.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.stop.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    stop.metadata = {'url': '/jobs/{job_id}/stop'}  # type: ignore

    def resume(
        self,
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Resume a stopped job.

        Resume execution of an existing stopped job.

        :param job_id: Unique ID of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.resume.metadata['url']  # type: ignore
        path_format_arguments = {
            'centralDnsSuffixInPath': self._serialize.url("self._config.central_dns_suffix_in_path", self._config.central_dns_suffix_in_path, 'str', skip_quote=True),
            'subdomain': self._serialize.url("self._config.subdomain", self._config.subdomain, 'str'),
            'job_id': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    resume.metadata = {'url': '/jobs/{job_id}/resume'}  # type: ignore
