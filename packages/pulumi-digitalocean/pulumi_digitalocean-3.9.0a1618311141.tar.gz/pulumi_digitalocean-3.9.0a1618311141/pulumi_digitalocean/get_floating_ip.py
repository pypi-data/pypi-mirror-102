# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = [
    'GetFloatingIpResult',
    'AwaitableGetFloatingIpResult',
    'get_floating_ip',
]

@pulumi.output_type
class GetFloatingIpResult:
    """
    A collection of values returned by getFloatingIp.
    """
    def __init__(__self__, droplet_id=None, floating_ip_urn=None, id=None, ip_address=None, region=None):
        if droplet_id and not isinstance(droplet_id, int):
            raise TypeError("Expected argument 'droplet_id' to be a int")
        pulumi.set(__self__, "droplet_id", droplet_id)
        if floating_ip_urn and not isinstance(floating_ip_urn, str):
            raise TypeError("Expected argument 'floating_ip_urn' to be a str")
        pulumi.set(__self__, "floating_ip_urn", floating_ip_urn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="dropletId")
    def droplet_id(self) -> int:
        return pulumi.get(self, "droplet_id")

    @property
    @pulumi.getter(name="floatingIpUrn")
    def floating_ip_urn(self) -> str:
        return pulumi.get(self, "floating_ip_urn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")


class AwaitableGetFloatingIpResult(GetFloatingIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFloatingIpResult(
            droplet_id=self.droplet_id,
            floating_ip_urn=self.floating_ip_urn,
            id=self.id,
            ip_address=self.ip_address,
            region=self.region)


def get_floating_ip(ip_address: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFloatingIpResult:
    """
    Get information on a floating ip. This data source provides the region and Droplet id
    as configured on your DigitalOcean account. This is useful if the floating IP
    in question is not managed by the provider or you need to find the Droplet the IP is
    attached to.

    An error is triggered if the provided floating IP does not exist.

    ## Example Usage

    Get the floating IP:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    config = pulumi.Config()
    public_ip = config.require_object("publicIp")
    example = digitalocean.get_floating_ip(ip_address=public_ip)
    pulumi.export("fipOutput", example.droplet_id)
    ```


    :param str ip_address: The allocated IP address of the specific floating IP to retrieve.
    """
    __args__ = dict()
    __args__['ipAddress'] = ip_address
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getFloatingIp:getFloatingIp', __args__, opts=opts, typ=GetFloatingIpResult).value

    return AwaitableGetFloatingIpResult(
        droplet_id=__ret__.droplet_id,
        floating_ip_urn=__ret__.floating_ip_urn,
        id=__ret__.id,
        ip_address=__ret__.ip_address,
        region=__ret__.region)
