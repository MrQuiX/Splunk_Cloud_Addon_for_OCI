# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDetectorRuleDetails(object):
    """
    Details of a Detector Rule to be created in Detector Recipe
    """

    #: A constant which can be used with the risk_level property of a CreateDetectorRuleDetails.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a CreateDetectorRuleDetails.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a CreateDetectorRuleDetails.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a CreateDetectorRuleDetails.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a CreateDetectorRuleDetails.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDetectorRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_detector_rule_id:
            The value to assign to the source_detector_rule_id property of this CreateDetectorRuleDetails.
        :type source_detector_rule_id: str

        :param name:
            The value to assign to the name property of this CreateDetectorRuleDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDetectorRuleDetails.
        :type description: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateDetectorRuleDetails.
        :type is_enabled: bool

        :param risk_level:
            The value to assign to the risk_level property of this CreateDetectorRuleDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"
        :type risk_level: str

        :param configurations:
            The value to assign to the configurations property of this CreateDetectorRuleDetails.
        :type configurations: list[oci.cloud_guard.models.DetectorConfiguration]

        :param condition:
            The value to assign to the condition property of this CreateDetectorRuleDetails.
        :type condition: oci.cloud_guard.models.Condition

        :param labels:
            The value to assign to the labels property of this CreateDetectorRuleDetails.
        :type labels: list[str]

        :param recommendation:
            The value to assign to the recommendation property of this CreateDetectorRuleDetails.
        :type recommendation: str

        :param data_source_id:
            The value to assign to the data_source_id property of this CreateDetectorRuleDetails.
        :type data_source_id: str

        :param entities_mappings:
            The value to assign to the entities_mappings property of this CreateDetectorRuleDetails.
        :type entities_mappings: list[oci.cloud_guard.models.EntitiesMapping]

        """
        self.swagger_types = {
            'source_detector_rule_id': 'str',
            'name': 'str',
            'description': 'str',
            'is_enabled': 'bool',
            'risk_level': 'str',
            'configurations': 'list[DetectorConfiguration]',
            'condition': 'Condition',
            'labels': 'list[str]',
            'recommendation': 'str',
            'data_source_id': 'str',
            'entities_mappings': 'list[EntitiesMapping]'
        }

        self.attribute_map = {
            'source_detector_rule_id': 'sourceDetectorRuleId',
            'name': 'name',
            'description': 'description',
            'is_enabled': 'isEnabled',
            'risk_level': 'riskLevel',
            'configurations': 'configurations',
            'condition': 'condition',
            'labels': 'labels',
            'recommendation': 'recommendation',
            'data_source_id': 'dataSourceId',
            'entities_mappings': 'entitiesMappings'
        }

        self._source_detector_rule_id = None
        self._name = None
        self._description = None
        self._is_enabled = None
        self._risk_level = None
        self._configurations = None
        self._condition = None
        self._labels = None
        self._recommendation = None
        self._data_source_id = None
        self._entities_mappings = None

    @property
    def source_detector_rule_id(self):
        """
        Gets the source_detector_rule_id of this CreateDetectorRuleDetails.
        Id of source detector rule


        :return: The source_detector_rule_id of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._source_detector_rule_id

    @source_detector_rule_id.setter
    def source_detector_rule_id(self, source_detector_rule_id):
        """
        Sets the source_detector_rule_id of this CreateDetectorRuleDetails.
        Id of source detector rule


        :param source_detector_rule_id: The source_detector_rule_id of this CreateDetectorRuleDetails.
        :type: str
        """
        self._source_detector_rule_id = source_detector_rule_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDetectorRuleDetails.
        Name of the detector rule


        :return: The name of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDetectorRuleDetails.
        Name of the detector rule


        :param name: The name of this CreateDetectorRuleDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateDetectorRuleDetails.
        Description of the detector rule


        :return: The description of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDetectorRuleDetails.
        Description of the detector rule


        :param description: The description of this CreateDetectorRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateDetectorRuleDetails.
        Identifies state for detector rule


        :return: The is_enabled of this CreateDetectorRuleDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateDetectorRuleDetails.
        Identifies state for detector rule


        :param is_enabled: The is_enabled of this CreateDetectorRuleDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def risk_level(self):
        """
        Gets the risk_level of this CreateDetectorRuleDetails.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"


        :return: The risk_level of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this CreateDetectorRuleDetails.
        The Risk Level


        :param risk_level: The risk_level of this CreateDetectorRuleDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            raise ValueError(
                "Invalid value for `risk_level`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._risk_level = risk_level

    @property
    def configurations(self):
        """
        Gets the configurations of this CreateDetectorRuleDetails.
        Configuration details


        :return: The configurations of this CreateDetectorRuleDetails.
        :rtype: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this CreateDetectorRuleDetails.
        Configuration details


        :param configurations: The configurations of this CreateDetectorRuleDetails.
        :type: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        self._configurations = configurations

    @property
    def condition(self):
        """
        Gets the condition of this CreateDetectorRuleDetails.

        :return: The condition of this CreateDetectorRuleDetails.
        :rtype: oci.cloud_guard.models.Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this CreateDetectorRuleDetails.

        :param condition: The condition of this CreateDetectorRuleDetails.
        :type: oci.cloud_guard.models.Condition
        """
        self._condition = condition

    @property
    def labels(self):
        """
        Gets the labels of this CreateDetectorRuleDetails.
        user defined labels for a detector rule


        :return: The labels of this CreateDetectorRuleDetails.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this CreateDetectorRuleDetails.
        user defined labels for a detector rule


        :param labels: The labels of this CreateDetectorRuleDetails.
        :type: list[str]
        """
        self._labels = labels

    @property
    def recommendation(self):
        """
        Gets the recommendation of this CreateDetectorRuleDetails.
        Recommendations of the detector rule


        :return: The recommendation of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """
        Sets the recommendation of this CreateDetectorRuleDetails.
        Recommendations of the detector rule


        :param recommendation: The recommendation of this CreateDetectorRuleDetails.
        :type: str
        """
        self._recommendation = recommendation

    @property
    def data_source_id(self):
        """
        Gets the data_source_id of this CreateDetectorRuleDetails.
        ocid of the data source which needs to attached


        :return: The data_source_id of this CreateDetectorRuleDetails.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """
        Sets the data_source_id of this CreateDetectorRuleDetails.
        ocid of the data source which needs to attached


        :param data_source_id: The data_source_id of this CreateDetectorRuleDetails.
        :type: str
        """
        self._data_source_id = data_source_id

    @property
    def entities_mappings(self):
        """
        Gets the entities_mappings of this CreateDetectorRuleDetails.
        Data Source entities mapping for a Detector Rule


        :return: The entities_mappings of this CreateDetectorRuleDetails.
        :rtype: list[oci.cloud_guard.models.EntitiesMapping]
        """
        return self._entities_mappings

    @entities_mappings.setter
    def entities_mappings(self, entities_mappings):
        """
        Sets the entities_mappings of this CreateDetectorRuleDetails.
        Data Source entities mapping for a Detector Rule


        :param entities_mappings: The entities_mappings of this CreateDetectorRuleDetails.
        :type: list[oci.cloud_guard.models.EntitiesMapping]
        """
        self._entities_mappings = entities_mappings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
