# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 size: pulumi.Input[int],
                 description: Optional[pulumi.Input[str]] = None,
                 filesystem_type: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_label: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] region: The region that the block storage volume will be created in.
        :param pulumi.Input[int] size: The size of the block storage volume in GiB. If updated, can only be expanded.
        :param pulumi.Input[str] description: A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
        :param pulumi.Input[str] filesystem_type: Filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_label: Initial filesystem label for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_type: Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] name: A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
        :param pulumi.Input[str] snapshot_id: The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of the tags to be applied to this Volume.
        """
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "size", size)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if filesystem_type is not None:
            warnings.warn("""This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.""", DeprecationWarning)
            pulumi.log.warn("""filesystem_type is deprecated: This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.""")
        if filesystem_type is not None:
            pulumi.set(__self__, "filesystem_type", filesystem_type)
        if initial_filesystem_label is not None:
            pulumi.set(__self__, "initial_filesystem_label", initial_filesystem_label)
        if initial_filesystem_type is not None:
            pulumi.set(__self__, "initial_filesystem_type", initial_filesystem_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region that the block storage volume will be created in.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        The size of the block storage volume in GiB. If updated, can only be expanded.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="filesystemType")
    def filesystem_type(self) -> Optional[pulumi.Input[str]]:
        """
        Filesystem type (`xfs` or `ext4`) for the block storage volume.
        """
        return pulumi.get(self, "filesystem_type")

    @filesystem_type.setter
    def filesystem_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filesystem_type", value)

    @property
    @pulumi.getter(name="initialFilesystemLabel")
    def initial_filesystem_label(self) -> Optional[pulumi.Input[str]]:
        """
        Initial filesystem label for the block storage volume.
        """
        return pulumi.get(self, "initial_filesystem_label")

    @initial_filesystem_label.setter
    def initial_filesystem_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "initial_filesystem_label", value)

    @property
    @pulumi.getter(name="initialFilesystemType")
    def initial_filesystem_type(self) -> Optional[pulumi.Input[str]]:
        """
        Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
        """
        return pulumi.get(self, "initial_filesystem_type")

    @initial_filesystem_type.setter
    def initial_filesystem_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "initial_filesystem_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
        """
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the tags to be applied to this Volume.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filesystem_type: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_label: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_volume = digitalocean.Volume("foobarVolume",
            region="nyc1",
            size=100,
            initial_filesystem_type="ext4",
            description="an example volume")
        foobar_droplet = digitalocean.Droplet("foobarDroplet",
            size="s-1vcpu-1gb",
            image="ubuntu-18-04-x64",
            region="nyc1")
        foobar_volume_attachment = digitalocean.VolumeAttachment("foobarVolumeAttachment",
            droplet_id=foobar_droplet.id,
            volume_id=foobar_volume.id)
        ```

        You can also create a volume from an existing snapshot.

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_volume_snapshot = digitalocean.get_volume_snapshot(name="baz")
        foobar_volume = digitalocean.Volume("foobarVolume",
            region="lon1",
            size=foobar_volume_snapshot.min_disk_size,
            snapshot_id=foobar_volume_snapshot.id)
        ```

        ## Import

        Volumes can be imported using the `volume id`, e.g.

        ```sh
         $ pulumi import digitalocean:index/volume:Volume volume 506f78a4-e098-11e5-ad9f-000f53306ae1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
        :param pulumi.Input[str] filesystem_type: Filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_label: Initial filesystem label for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_type: Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] name: A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
        :param pulumi.Input[str] region: The region that the block storage volume will be created in.
        :param pulumi.Input[int] size: The size of the block storage volume in GiB. If updated, can only be expanded.
        :param pulumi.Input[str] snapshot_id: The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of the tags to be applied to this Volume.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_volume = digitalocean.Volume("foobarVolume",
            region="nyc1",
            size=100,
            initial_filesystem_type="ext4",
            description="an example volume")
        foobar_droplet = digitalocean.Droplet("foobarDroplet",
            size="s-1vcpu-1gb",
            image="ubuntu-18-04-x64",
            region="nyc1")
        foobar_volume_attachment = digitalocean.VolumeAttachment("foobarVolumeAttachment",
            droplet_id=foobar_droplet.id,
            volume_id=foobar_volume.id)
        ```

        You can also create a volume from an existing snapshot.

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_volume_snapshot = digitalocean.get_volume_snapshot(name="baz")
        foobar_volume = digitalocean.Volume("foobarVolume",
            region="lon1",
            size=foobar_volume_snapshot.min_disk_size,
            snapshot_id=foobar_volume_snapshot.id)
        ```

        ## Import

        Volumes can be imported using the `volume id`, e.g.

        ```sh
         $ pulumi import digitalocean:index/volume:Volume volume 506f78a4-e098-11e5-ad9f-000f53306ae1
        ```

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filesystem_type: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_label: Optional[pulumi.Input[str]] = None,
                 initial_filesystem_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            if filesystem_type is not None and not opts.urn:
                warnings.warn("""This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.""", DeprecationWarning)
                pulumi.log.warn("""filesystem_type is deprecated: This fields functionality has been replaced by `initial_filesystem_type`. The property will still remain as a computed attribute representing the current volumes filesystem type.""")
            __props__['filesystem_type'] = filesystem_type
            __props__['initial_filesystem_label'] = initial_filesystem_label
            __props__['initial_filesystem_type'] = initial_filesystem_type
            __props__['name'] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['snapshot_id'] = snapshot_id
            __props__['tags'] = tags
            __props__['droplet_ids'] = None
            __props__['filesystem_label'] = None
            __props__['volume_urn'] = None
        super(Volume, __self__).__init__(
            'digitalocean:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            droplet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            filesystem_label: Optional[pulumi.Input[str]] = None,
            filesystem_type: Optional[pulumi.Input[str]] = None,
            initial_filesystem_label: Optional[pulumi.Input[str]] = None,
            initial_filesystem_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            snapshot_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            volume_urn: Optional[pulumi.Input[str]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] droplet_ids: A list of associated droplet ids.
        :param pulumi.Input[str] filesystem_label: Filesystem label for the block storage volume.
        :param pulumi.Input[str] filesystem_type: Filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_label: Initial filesystem label for the block storage volume.
        :param pulumi.Input[str] initial_filesystem_type: Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
        :param pulumi.Input[str] name: A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
        :param pulumi.Input[str] region: The region that the block storage volume will be created in.
        :param pulumi.Input[int] size: The size of the block storage volume in GiB. If updated, can only be expanded.
        :param pulumi.Input[str] snapshot_id: The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of the tags to be applied to this Volume.
        :param pulumi.Input[str] volume_urn: The uniform resource name for the volume.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["droplet_ids"] = droplet_ids
        __props__["filesystem_label"] = filesystem_label
        __props__["filesystem_type"] = filesystem_type
        __props__["initial_filesystem_label"] = initial_filesystem_label
        __props__["initial_filesystem_type"] = initial_filesystem_type
        __props__["name"] = name
        __props__["region"] = region
        __props__["size"] = size
        __props__["snapshot_id"] = snapshot_id
        __props__["tags"] = tags
        __props__["volume_urn"] = volume_urn
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A free-form text field up to a limit of 1024 bytes to describe a block storage volume.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dropletIds")
    def droplet_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        A list of associated droplet ids.
        """
        return pulumi.get(self, "droplet_ids")

    @property
    @pulumi.getter(name="filesystemLabel")
    def filesystem_label(self) -> pulumi.Output[str]:
        """
        Filesystem label for the block storage volume.
        """
        return pulumi.get(self, "filesystem_label")

    @property
    @pulumi.getter(name="filesystemType")
    def filesystem_type(self) -> pulumi.Output[str]:
        """
        Filesystem type (`xfs` or `ext4`) for the block storage volume.
        """
        return pulumi.get(self, "filesystem_type")

    @property
    @pulumi.getter(name="initialFilesystemLabel")
    def initial_filesystem_label(self) -> pulumi.Output[Optional[str]]:
        """
        Initial filesystem label for the block storage volume.
        """
        return pulumi.get(self, "initial_filesystem_label")

    @property
    @pulumi.getter(name="initialFilesystemType")
    def initial_filesystem_type(self) -> pulumi.Output[Optional[str]]:
        """
        Initial filesystem type (`xfs` or `ext4`) for the block storage volume.
        """
        return pulumi.get(self, "initial_filesystem_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region that the block storage volume will be created in.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the block storage volume in GiB. If updated, can only be expanded.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of the tags to be applied to this Volume.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="volumeUrn")
    def volume_urn(self) -> pulumi.Output[str]:
        """
        The uniform resource name for the volume.
        """
        return pulumi.get(self, "volume_urn")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

