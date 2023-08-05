# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['ContainerRegistryDockerCredentialsArgs', 'ContainerRegistryDockerCredentials']

@pulumi.input_type
class ContainerRegistryDockerCredentialsArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 expiry_seconds: Optional[pulumi.Input[int]] = None,
                 write: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ContainerRegistryDockerCredentials resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[int] expiry_seconds: The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.
        :param pulumi.Input[bool] write: Allow for write access to the container registry. Defaults to false.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        if expiry_seconds is not None:
            pulumi.set(__self__, "expiry_seconds", expiry_seconds)
        if write is not None:
            pulumi.set(__self__, "write", write)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="expirySeconds")
    def expiry_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.
        """
        return pulumi.get(self, "expiry_seconds")

    @expiry_seconds.setter
    def expiry_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "expiry_seconds", value)

    @property
    @pulumi.getter
    def write(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow for write access to the container registry. Defaults to false.
        """
        return pulumi.get(self, "write")

    @write.setter
    def write(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "write", value)


class ContainerRegistryDockerCredentials(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiry_seconds: Optional[pulumi.Input[int]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 write: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Get Docker credentials for your DigitalOcean container registry.

        An error is triggered if the provided container registry name does not exist.

        ## Example Usage
        ### Basic Example

        Get the container registry:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        example = digitalocean.ContainerRegistryDockerCredentials("example", registry_name="example")
        ```
        ### Docker Provider Example

        Use the `endpoint` and `docker_credentials` with the Docker provider:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        example_container_registry = digitalocean.get_container_registry(name="example")
        example_container_registry_docker_credentials = digitalocean.ContainerRegistryDockerCredentials("exampleContainerRegistryDockerCredentials", registry_name="example")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] expiry_seconds: The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[bool] write: Allow for write access to the container registry. Defaults to false.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerRegistryDockerCredentialsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Get Docker credentials for your DigitalOcean container registry.

        An error is triggered if the provided container registry name does not exist.

        ## Example Usage
        ### Basic Example

        Get the container registry:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        example = digitalocean.ContainerRegistryDockerCredentials("example", registry_name="example")
        ```
        ### Docker Provider Example

        Use the `endpoint` and `docker_credentials` with the Docker provider:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        example_container_registry = digitalocean.get_container_registry(name="example")
        example_container_registry_docker_credentials = digitalocean.ContainerRegistryDockerCredentials("exampleContainerRegistryDockerCredentials", registry_name="example")
        ```

        :param str resource_name: The name of the resource.
        :param ContainerRegistryDockerCredentialsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerRegistryDockerCredentialsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiry_seconds: Optional[pulumi.Input[int]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 write: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['expiry_seconds'] = expiry_seconds
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__['registry_name'] = registry_name
            __props__['write'] = write
            __props__['credential_expiration_time'] = None
            __props__['docker_credentials'] = None
        super(ContainerRegistryDockerCredentials, __self__).__init__(
            'digitalocean:index/containerRegistryDockerCredentials:ContainerRegistryDockerCredentials',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credential_expiration_time: Optional[pulumi.Input[str]] = None,
            docker_credentials: Optional[pulumi.Input[str]] = None,
            expiry_seconds: Optional[pulumi.Input[int]] = None,
            registry_name: Optional[pulumi.Input[str]] = None,
            write: Optional[pulumi.Input[bool]] = None) -> 'ContainerRegistryDockerCredentials':
        """
        Get an existing ContainerRegistryDockerCredentials resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] expiry_seconds: The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[bool] write: Allow for write access to the container registry. Defaults to false.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["credential_expiration_time"] = credential_expiration_time
        __props__["docker_credentials"] = docker_credentials
        __props__["expiry_seconds"] = expiry_seconds
        __props__["registry_name"] = registry_name
        __props__["write"] = write
        return ContainerRegistryDockerCredentials(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="credentialExpirationTime")
    def credential_expiration_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "credential_expiration_time")

    @property
    @pulumi.getter(name="dockerCredentials")
    def docker_credentials(self) -> pulumi.Output[str]:
        return pulumi.get(self, "docker_credentials")

    @property
    @pulumi.getter(name="expirySeconds")
    def expiry_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time to pass before the Docker credentials expire in seconds. Defaults to 1576800000, or roughly 50 years. Must be greater than 0 and less than 1576800000.
        """
        return pulumi.get(self, "expiry_seconds")

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Output[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @property
    @pulumi.getter
    def write(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow for write access to the container registry. Defaults to false.
        """
        return pulumi.get(self, "write")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

