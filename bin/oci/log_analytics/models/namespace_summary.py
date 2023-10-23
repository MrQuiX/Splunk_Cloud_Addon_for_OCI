# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamespaceSummary(object):
    """
    The is the namespace summary of a tenancy in Logan Analytics application
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamespaceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this NamespaceSummary.
        :type namespace_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NamespaceSummary.
        :type compartment_id: str

        :param is_onboarded:
            The value to assign to the is_onboarded property of this NamespaceSummary.
        :type is_onboarded: bool

        :param is_log_set_enabled:
            The value to assign to the is_log_set_enabled property of this NamespaceSummary.
        :type is_log_set_enabled: bool

        :param is_data_ever_ingested:
            The value to assign to the is_data_ever_ingested property of this NamespaceSummary.
        :type is_data_ever_ingested: bool

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'compartment_id': 'str',
            'is_onboarded': 'bool',
            'is_log_set_enabled': 'bool',
            'is_data_ever_ingested': 'bool'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'compartment_id': 'compartmentId',
            'is_onboarded': 'isOnboarded',
            'is_log_set_enabled': 'isLogSetEnabled',
            'is_data_ever_ingested': 'isDataEverIngested'
        }

        self._namespace_name = None
        self._compartment_id = None
        self._is_onboarded = None
        self._is_log_set_enabled = None
        self._is_data_ever_ingested = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this NamespaceSummary.
        This is the namespace name of a tenancy


        :return: The namespace_name of this NamespaceSummary.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this NamespaceSummary.
        This is the namespace name of a tenancy


        :param namespace_name: The namespace_name of this NamespaceSummary.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NamespaceSummary.
        The is the tenancy ID


        :return: The compartment_id of this NamespaceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NamespaceSummary.
        The is the tenancy ID


        :param compartment_id: The compartment_id of this NamespaceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_onboarded(self):
        """
        **[Required]** Gets the is_onboarded of this NamespaceSummary.
        This indicates if the tenancy is onboarded to Logging Analytics


        :return: The is_onboarded of this NamespaceSummary.
        :rtype: bool
        """
        return self._is_onboarded

    @is_onboarded.setter
    def is_onboarded(self, is_onboarded):
        """
        Sets the is_onboarded of this NamespaceSummary.
        This indicates if the tenancy is onboarded to Logging Analytics


        :param is_onboarded: The is_onboarded of this NamespaceSummary.
        :type: bool
        """
        self._is_onboarded = is_onboarded

    @property
    def is_log_set_enabled(self):
        """
        Gets the is_log_set_enabled of this NamespaceSummary.
        This indicates if the log set feature is enabled for the tenancy


        :return: The is_log_set_enabled of this NamespaceSummary.
        :rtype: bool
        """
        return self._is_log_set_enabled

    @is_log_set_enabled.setter
    def is_log_set_enabled(self, is_log_set_enabled):
        """
        Sets the is_log_set_enabled of this NamespaceSummary.
        This indicates if the log set feature is enabled for the tenancy


        :param is_log_set_enabled: The is_log_set_enabled of this NamespaceSummary.
        :type: bool
        """
        self._is_log_set_enabled = is_log_set_enabled

    @property
    def is_data_ever_ingested(self):
        """
        Gets the is_data_ever_ingested of this NamespaceSummary.
        This indicates if data has ever been ingested for the tenancy in Logging Analytics


        :return: The is_data_ever_ingested of this NamespaceSummary.
        :rtype: bool
        """
        return self._is_data_ever_ingested

    @is_data_ever_ingested.setter
    def is_data_ever_ingested(self, is_data_ever_ingested):
        """
        Sets the is_data_ever_ingested of this NamespaceSummary.
        This indicates if data has ever been ingested for the tenancy in Logging Analytics


        :param is_data_ever_ingested: The is_data_ever_ingested of this NamespaceSummary.
        :type: bool
        """
        self._is_data_ever_ingested = is_data_ever_ingested

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
