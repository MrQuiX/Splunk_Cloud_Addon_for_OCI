# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableAutoAssociationDetail(object):
    """
    The information required to enable log source auto-association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableAutoAssociationDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_group_id:
            The value to assign to the log_group_id property of this EnableAutoAssociationDetail.
        :type log_group_id: str

        """
        self.swagger_types = {
            'log_group_id': 'str'
        }

        self.attribute_map = {
            'log_group_id': 'logGroupId'
        }

        self._log_group_id = None

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this EnableAutoAssociationDetail.
        The unique identifier of the log group to use when auto-associting the log source to
        eligible entities.


        :return: The log_group_id of this EnableAutoAssociationDetail.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this EnableAutoAssociationDetail.
        The unique identifier of the log group to use when auto-associting the log source to
        eligible entities.


        :param log_group_id: The log_group_id of this EnableAutoAssociationDetail.
        :type: str
        """
        self._log_group_id = log_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other