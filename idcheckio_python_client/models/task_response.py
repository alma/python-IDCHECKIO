# coding: utf-8

"""
    IdCheck.IO API

    Check identity documents

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class TaskResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uid=None, is_with_progress=False, accepted=None, started=None, ended=None, last_progress=None, percentage=None, redirect_url=None, message=None):
        """
        TaskResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'uid': 'str',
            'is_with_progress': 'bool',
            'accepted': 'int',
            'started': 'int',
            'ended': 'int',
            'last_progress': 'int',
            'percentage': 'int',
            'redirect_url': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'uid': 'uid',
            'is_with_progress': 'isWithProgress',
            'accepted': 'accepted',
            'started': 'started',
            'ended': 'ended',
            'last_progress': 'lastProgress',
            'percentage': 'percentage',
            'redirect_url': 'redirectUrl',
            'message': 'message'
        }

        self._uid = uid
        self._is_with_progress = is_with_progress
        self._accepted = accepted
        self._started = started
        self._ended = ended
        self._last_progress = last_progress
        self._percentage = percentage
        self._redirect_url = redirect_url
        self._message = message

    @property
    def uid(self):
        """
        Gets the uid of this TaskResponse.
        analysisRefUid

        :return: The uid of this TaskResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this TaskResponse.
        analysisRefUid

        :param uid: The uid of this TaskResponse.
        :type: str
        """

        self._uid = uid

    @property
    def is_with_progress(self):
        """
        Gets the is_with_progress of this TaskResponse.
        task with progress

        :return: The is_with_progress of this TaskResponse.
        :rtype: bool
        """
        return self._is_with_progress

    @is_with_progress.setter
    def is_with_progress(self, is_with_progress):
        """
        Sets the is_with_progress of this TaskResponse.
        task with progress

        :param is_with_progress: The is_with_progress of this TaskResponse.
        :type: bool
        """

        self._is_with_progress = is_with_progress

    @property
    def accepted(self):
        """
        Gets the accepted of this TaskResponse.
        task accepted date

        :return: The accepted of this TaskResponse.
        :rtype: int
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """
        Sets the accepted of this TaskResponse.
        task accepted date

        :param accepted: The accepted of this TaskResponse.
        :type: int
        """

        self._accepted = accepted

    @property
    def started(self):
        """
        Gets the started of this TaskResponse.
        task started date

        :return: The started of this TaskResponse.
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """
        Sets the started of this TaskResponse.
        task started date

        :param started: The started of this TaskResponse.
        :type: int
        """

        self._started = started

    @property
    def ended(self):
        """
        Gets the ended of this TaskResponse.
        task ended date

        :return: The ended of this TaskResponse.
        :rtype: int
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """
        Sets the ended of this TaskResponse.
        task ended date

        :param ended: The ended of this TaskResponse.
        :type: int
        """

        self._ended = ended

    @property
    def last_progress(self):
        """
        Gets the last_progress of this TaskResponse.
        last progress date

        :return: The last_progress of this TaskResponse.
        :rtype: int
        """
        return self._last_progress

    @last_progress.setter
    def last_progress(self, last_progress):
        """
        Sets the last_progress of this TaskResponse.
        last progress date

        :param last_progress: The last_progress of this TaskResponse.
        :type: int
        """

        self._last_progress = last_progress

    @property
    def percentage(self):
        """
        Gets the percentage of this TaskResponse.
        percentage progress

        :return: The percentage of this TaskResponse.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this TaskResponse.
        percentage progress

        :param percentage: The percentage of this TaskResponse.
        :type: int
        """

        self._percentage = percentage

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this TaskResponse.
        redirect url

        :return: The redirect_url of this TaskResponse.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this TaskResponse.
        redirect url

        :param redirect_url: The redirect_url of this TaskResponse.
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def message(self):
        """
        Gets the message of this TaskResponse.
        message

        :return: The message of this TaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TaskResponse.
        message

        :param message: The message of this TaskResponse.
        :type: str
        """

        self._message = message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
