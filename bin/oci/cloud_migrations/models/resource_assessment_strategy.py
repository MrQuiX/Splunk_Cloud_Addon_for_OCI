# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceAssessmentStrategy(object):
    """
    Migration strategy for the resource to be migrated.
    """

    #: A constant which can be used with the resource_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "CPU"
    RESOURCE_TYPE_CPU = "CPU"

    #: A constant which can be used with the resource_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "MEMORY"
    RESOURCE_TYPE_MEMORY = "MEMORY"

    #: A constant which can be used with the resource_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "ALL"
    RESOURCE_TYPE_ALL = "ALL"

    #: A constant which can be used with the strategy_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "AS_IS"
    STRATEGY_TYPE_AS_IS = "AS_IS"

    #: A constant which can be used with the strategy_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "AVERAGE"
    STRATEGY_TYPE_AVERAGE = "AVERAGE"

    #: A constant which can be used with the strategy_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "PEAK"
    STRATEGY_TYPE_PEAK = "PEAK"

    #: A constant which can be used with the strategy_type property of a ResourceAssessmentStrategy.
    #: This constant has a value of "PERCENTILE"
    STRATEGY_TYPE_PERCENTILE = "PERCENTILE"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceAssessmentStrategy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.PeakResourceAssessmentStrategy`
        * :class:`~oci.cloud_migrations.models.PercentileResourceAssessmentStrategy`
        * :class:`~oci.cloud_migrations.models.AverageResourceAssessmentStrategy`
        * :class:`~oci.cloud_migrations.models.AsIsResourceAssessmentStrategy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this ResourceAssessmentStrategy.
            Allowed values for this property are: "CPU", "MEMORY", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param strategy_type:
            The value to assign to the strategy_type property of this ResourceAssessmentStrategy.
            Allowed values for this property are: "AS_IS", "AVERAGE", "PEAK", "PERCENTILE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type strategy_type: str

        """
        self.swagger_types = {
            'resource_type': 'str',
            'strategy_type': 'str'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'strategy_type': 'strategyType'
        }

        self._resource_type = None
        self._strategy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['strategyType']

        if type == 'PEAK':
            return 'PeakResourceAssessmentStrategy'

        if type == 'PERCENTILE':
            return 'PercentileResourceAssessmentStrategy'

        if type == 'AVERAGE':
            return 'AverageResourceAssessmentStrategy'

        if type == 'AS_IS':
            return 'AsIsResourceAssessmentStrategy'
        else:
            return 'ResourceAssessmentStrategy'

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this ResourceAssessmentStrategy.
        The type of resource.

        Allowed values for this property are: "CPU", "MEMORY", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this ResourceAssessmentStrategy.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResourceAssessmentStrategy.
        The type of resource.


        :param resource_type: The resource_type of this ResourceAssessmentStrategy.
        :type: str
        """
        allowed_values = ["CPU", "MEMORY", "ALL"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def strategy_type(self):
        """
        **[Required]** Gets the strategy_type of this ResourceAssessmentStrategy.
        The type of strategy used for migration.

        Allowed values for this property are: "AS_IS", "AVERAGE", "PEAK", "PERCENTILE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The strategy_type of this ResourceAssessmentStrategy.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        """
        Sets the strategy_type of this ResourceAssessmentStrategy.
        The type of strategy used for migration.


        :param strategy_type: The strategy_type of this ResourceAssessmentStrategy.
        :type: str
        """
        allowed_values = ["AS_IS", "AVERAGE", "PEAK", "PERCENTILE"]
        if not value_allowed_none_or_none_sentinel(strategy_type, allowed_values):
            strategy_type = 'UNKNOWN_ENUM_VALUE'
        self._strategy_type = strategy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
