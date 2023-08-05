# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['CustomImageArgs', 'CustomImage']

@pulumi.input_type
class CustomImageArgs:
    def __init__(__self__, *,
                 regions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 url: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 distribution: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CustomImage resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: A list of regions. (Currently only one is supported).
        :param pulumi.Input[str] url: A URL from which the custom Linux virtual machine image may be retrieved.
        :param pulumi.Input[str] description: An optional description for the image.
        :param pulumi.Input[str] distribution: An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image)
        :param pulumi.Input[str] name: A name for the Custom Image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of optional tags for the image.
        """
        pulumi.set(__self__, "regions", regions)
        pulumi.set(__self__, "url", url)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if distribution is not None:
            pulumi.set(__self__, "distribution", distribution)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of regions. (Currently only one is supported).
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        A URL from which the custom Linux virtual machine image may be retrieved.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description for the image.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def distribution(self) -> Optional[pulumi.Input[str]]:
        """
        An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image)
        """
        return pulumi.get(self, "distribution")

    @distribution.setter
    def distribution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "distribution", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the Custom Image.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of optional tags for the image.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class CustomImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distribution: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource which can be used to create a [custom image](https://www.digitalocean.com/docs/images/custom-images/)
        from a URL. The URL must point to an image in one of the following file formats:

        - Raw (.img) with an MBR or GPT partition table
        - qcow2
        - VHDX
        - VDI
        - VMDK

        The image may be compressed using gzip or bzip2. See the DigitalOcean Custom
        Image documentation for [additional requirements](https://www.digitalocean.com/docs/images/custom-images/#image-requirements).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        flatcar = digitalocean.CustomImage("flatcar",
            url="https://stable.release.flatcar-linux.net/amd64-usr/2605.7.0/flatcar_production_digitalocean_image.bin.bz2",
            regions=["nyc3"])
        example = digitalocean.Droplet("example",
            image=flatcar.id,
            region="nyc3",
            size="s-1vcpu-1gb",
            ssh_keys=["12345"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description for the image.
        :param pulumi.Input[str] distribution: An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image)
        :param pulumi.Input[str] name: A name for the Custom Image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: A list of regions. (Currently only one is supported).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of optional tags for the image.
        :param pulumi.Input[str] url: A URL from which the custom Linux virtual machine image may be retrieved.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource which can be used to create a [custom image](https://www.digitalocean.com/docs/images/custom-images/)
        from a URL. The URL must point to an image in one of the following file formats:

        - Raw (.img) with an MBR or GPT partition table
        - qcow2
        - VHDX
        - VDI
        - VMDK

        The image may be compressed using gzip or bzip2. See the DigitalOcean Custom
        Image documentation for [additional requirements](https://www.digitalocean.com/docs/images/custom-images/#image-requirements).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        flatcar = digitalocean.CustomImage("flatcar",
            url="https://stable.release.flatcar-linux.net/amd64-usr/2605.7.0/flatcar_production_digitalocean_image.bin.bz2",
            regions=["nyc3"])
        example = digitalocean.Droplet("example",
            image=flatcar.id,
            region="nyc3",
            size="s-1vcpu-1gb",
            ssh_keys=["12345"])
        ```

        :param str resource_name: The name of the resource.
        :param CustomImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distribution: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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

            __props__['description'] = description
            __props__['distribution'] = distribution
            __props__['name'] = name
            if regions is None and not opts.urn:
                raise TypeError("Missing required property 'regions'")
            __props__['regions'] = regions
            __props__['tags'] = tags
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__['url'] = url
            __props__['created_at'] = None
            __props__['image_id'] = None
            __props__['min_disk_size'] = None
            __props__['public'] = None
            __props__['size_gigabytes'] = None
            __props__['slug'] = None
            __props__['status'] = None
            __props__['type'] = None
        super(CustomImage, __self__).__init__(
            'digitalocean:index/customImage:CustomImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            distribution: Optional[pulumi.Input[str]] = None,
            image_id: Optional[pulumi.Input[int]] = None,
            min_disk_size: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public: Optional[pulumi.Input[bool]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            size_gigabytes: Optional[pulumi.Input[float]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'CustomImage':
        """
        Get an existing CustomImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description for the image.
        :param pulumi.Input[str] distribution: An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image)
        :param pulumi.Input[str] name: A name for the Custom Image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: A list of regions. (Currently only one is supported).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of optional tags for the image.
        :param pulumi.Input[str] url: A URL from which the custom Linux virtual machine image may be retrieved.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["created_at"] = created_at
        __props__["description"] = description
        __props__["distribution"] = distribution
        __props__["image_id"] = image_id
        __props__["min_disk_size"] = min_disk_size
        __props__["name"] = name
        __props__["public"] = public
        __props__["regions"] = regions
        __props__["size_gigabytes"] = size_gigabytes
        __props__["slug"] = slug
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["url"] = url
        return CustomImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description for the image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def distribution(self) -> pulumi.Output[Optional[str]]:
        """
        An optional distribution name for the image. Valid values are documented [here](https://developers.digitalocean.com/documentation/v2/#create-a-custom-image)
        """
        return pulumi.get(self, "distribution")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="minDiskSize")
    def min_disk_size(self) -> pulumi.Output[int]:
        return pulumi.get(self, "min_disk_size")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for the Custom Image.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def public(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "public")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of regions. (Currently only one is supported).
        """
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="sizeGigabytes")
    def size_gigabytes(self) -> pulumi.Output[float]:
        return pulumi.get(self, "size_gigabytes")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of optional tags for the image.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        A URL from which the custom Linux virtual machine image may be retrieved.
        """
        return pulumi.get(self, "url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

