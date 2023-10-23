# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateAuthorityBundle(object):
    """
    The contents of the certificate, properties of the certificate (and certificate version), and user-provided contextual metadata for the certificate.
    """

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "CURRENT"
    STAGES_CURRENT = "CURRENT"

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "PENDING"
    STAGES_PENDING = "PENDING"

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "LATEST"
    STAGES_LATEST = "LATEST"

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "PREVIOUS"
    STAGES_PREVIOUS = "PREVIOUS"

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "DEPRECATED"
    STAGES_DEPRECATED = "DEPRECATED"

    #: A constant which can be used with the stages property of a CertificateAuthorityBundle.
    #: This constant has a value of "FAILED"
    STAGES_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateAuthorityBundle object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_authority_id:
            The value to assign to the certificate_authority_id property of this CertificateAuthorityBundle.
        :type certificate_authority_id: str

        :param certificate_authority_name:
            The value to assign to the certificate_authority_name property of this CertificateAuthorityBundle.
        :type certificate_authority_name: str

        :param serial_number:
            The value to assign to the serial_number property of this CertificateAuthorityBundle.
        :type serial_number: str

        :param certificate_pem:
            The value to assign to the certificate_pem property of this CertificateAuthorityBundle.
        :type certificate_pem: str

        :param cert_chain_pem:
            The value to assign to the cert_chain_pem property of this CertificateAuthorityBundle.
        :type cert_chain_pem: str

        :param version_name:
            The value to assign to the version_name property of this CertificateAuthorityBundle.
        :type version_name: str

        :param time_created:
            The value to assign to the time_created property of this CertificateAuthorityBundle.
        :type time_created: datetime

        :param version_number:
            The value to assign to the version_number property of this CertificateAuthorityBundle.
        :type version_number: int

        :param validity:
            The value to assign to the validity property of this CertificateAuthorityBundle.
        :type validity: oci.certificates.models.Validity

        :param stages:
            The value to assign to the stages property of this CertificateAuthorityBundle.
            Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stages: list[str]

        :param revocation_status:
            The value to assign to the revocation_status property of this CertificateAuthorityBundle.
        :type revocation_status: oci.certificates.models.RevocationStatus

        """
        self.swagger_types = {
            'certificate_authority_id': 'str',
            'certificate_authority_name': 'str',
            'serial_number': 'str',
            'certificate_pem': 'str',
            'cert_chain_pem': 'str',
            'version_name': 'str',
            'time_created': 'datetime',
            'version_number': 'int',
            'validity': 'Validity',
            'stages': 'list[str]',
            'revocation_status': 'RevocationStatus'
        }

        self.attribute_map = {
            'certificate_authority_id': 'certificateAuthorityId',
            'certificate_authority_name': 'certificateAuthorityName',
            'serial_number': 'serialNumber',
            'certificate_pem': 'certificatePem',
            'cert_chain_pem': 'certChainPem',
            'version_name': 'versionName',
            'time_created': 'timeCreated',
            'version_number': 'versionNumber',
            'validity': 'validity',
            'stages': 'stages',
            'revocation_status': 'revocationStatus'
        }

        self._certificate_authority_id = None
        self._certificate_authority_name = None
        self._serial_number = None
        self._certificate_pem = None
        self._cert_chain_pem = None
        self._version_name = None
        self._time_created = None
        self._version_number = None
        self._validity = None
        self._stages = None
        self._revocation_status = None

    @property
    def certificate_authority_id(self):
        """
        **[Required]** Gets the certificate_authority_id of this CertificateAuthorityBundle.
        The OCID of the certificate authority (CA).


        :return: The certificate_authority_id of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._certificate_authority_id

    @certificate_authority_id.setter
    def certificate_authority_id(self, certificate_authority_id):
        """
        Sets the certificate_authority_id of this CertificateAuthorityBundle.
        The OCID of the certificate authority (CA).


        :param certificate_authority_id: The certificate_authority_id of this CertificateAuthorityBundle.
        :type: str
        """
        self._certificate_authority_id = certificate_authority_id

    @property
    def certificate_authority_name(self):
        """
        **[Required]** Gets the certificate_authority_name of this CertificateAuthorityBundle.
        The name of the CA.


        :return: The certificate_authority_name of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._certificate_authority_name

    @certificate_authority_name.setter
    def certificate_authority_name(self, certificate_authority_name):
        """
        Sets the certificate_authority_name of this CertificateAuthorityBundle.
        The name of the CA.


        :param certificate_authority_name: The certificate_authority_name of this CertificateAuthorityBundle.
        :type: str
        """
        self._certificate_authority_name = certificate_authority_name

    @property
    def serial_number(self):
        """
        **[Required]** Gets the serial_number of this CertificateAuthorityBundle.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :return: The serial_number of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CertificateAuthorityBundle.
        A unique certificate identifier used in certificate revocation tracking, formatted as octets.
        Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`


        :param serial_number: The serial_number of this CertificateAuthorityBundle.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def certificate_pem(self):
        """
        **[Required]** Gets the certificate_pem of this CertificateAuthorityBundle.
        The certificate (in PEM format) for this CA version.


        :return: The certificate_pem of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        """
        Sets the certificate_pem of this CertificateAuthorityBundle.
        The certificate (in PEM format) for this CA version.


        :param certificate_pem: The certificate_pem of this CertificateAuthorityBundle.
        :type: str
        """
        self._certificate_pem = certificate_pem

    @property
    def cert_chain_pem(self):
        """
        Gets the cert_chain_pem of this CertificateAuthorityBundle.
        The certificate chain (in PEM format) for this CA version.


        :return: The cert_chain_pem of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._cert_chain_pem

    @cert_chain_pem.setter
    def cert_chain_pem(self, cert_chain_pem):
        """
        Sets the cert_chain_pem of this CertificateAuthorityBundle.
        The certificate chain (in PEM format) for this CA version.


        :param cert_chain_pem: The cert_chain_pem of this CertificateAuthorityBundle.
        :type: str
        """
        self._cert_chain_pem = cert_chain_pem

    @property
    def version_name(self):
        """
        Gets the version_name of this CertificateAuthorityBundle.
        The name of the CA.


        :return: The version_name of this CertificateAuthorityBundle.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this CertificateAuthorityBundle.
        The name of the CA.


        :param version_name: The version_name of this CertificateAuthorityBundle.
        :type: str
        """
        self._version_name = version_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CertificateAuthorityBundle.
        A property indicating when the CA was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CertificateAuthorityBundle.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CertificateAuthorityBundle.
        A property indicating when the CA was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CertificateAuthorityBundle.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version_number(self):
        """
        **[Required]** Gets the version_number of this CertificateAuthorityBundle.
        The version number of the CA.


        :return: The version_number of this CertificateAuthorityBundle.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this CertificateAuthorityBundle.
        The version number of the CA.


        :param version_number: The version_number of this CertificateAuthorityBundle.
        :type: int
        """
        self._version_number = version_number

    @property
    def validity(self):
        """
        **[Required]** Gets the validity of this CertificateAuthorityBundle.

        :return: The validity of this CertificateAuthorityBundle.
        :rtype: oci.certificates.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CertificateAuthorityBundle.

        :param validity: The validity of this CertificateAuthorityBundle.
        :type: oci.certificates.models.Validity
        """
        self._validity = validity

    @property
    def stages(self):
        """
        **[Required]** Gets the stages of this CertificateAuthorityBundle.
        A list of rotation states for this CA.

        Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stages of this CertificateAuthorityBundle.
        :rtype: list[str]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this CertificateAuthorityBundle.
        A list of rotation states for this CA.


        :param stages: The stages of this CertificateAuthorityBundle.
        :type: list[str]
        """
        allowed_values = ["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED"]
        if stages:
            stages[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in stages]
        self._stages = stages

    @property
    def revocation_status(self):
        """
        Gets the revocation_status of this CertificateAuthorityBundle.

        :return: The revocation_status of this CertificateAuthorityBundle.
        :rtype: oci.certificates.models.RevocationStatus
        """
        return self._revocation_status

    @revocation_status.setter
    def revocation_status(self, revocation_status):
        """
        Sets the revocation_status of this CertificateAuthorityBundle.

        :param revocation_status: The revocation_status of this CertificateAuthorityBundle.
        :type: oci.certificates.models.RevocationStatus
        """
        self._revocation_status = revocation_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
