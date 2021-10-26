# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class ElasticDeploymentStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag specifying if the Elastic deployment status is healthy or not.
    """

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"

class LiftrResourceCategories(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "Unknown"
    MONITOR_LOGS = "MonitorLogs"

class ManagedIdentityTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Managed Identity types.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"

class MonitoringStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag specifying if the resource monitoring is enabled or disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class OperationName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operation to be performed on the given vm resource id.
    """

    ADD = "Add"
    DELETE = "Delete"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of Elastic resource.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETED = "Deleted"
    NOT_SPECIFIED = "NotSpecified"

class SendingLogs(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag indicating the status of the resource for sending logs operation to Elastic.
    """

    TRUE = "True"
    FALSE = "False"

class TagAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Valid actions for a filtering tag. Exclusion takes priority over inclusion.
    """

    INCLUDE = "Include"
    EXCLUDE = "Exclude"