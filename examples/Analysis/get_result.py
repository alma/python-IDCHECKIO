# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest

import idcheckio_python_client
from pprint import pprint
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.apis.analysis_api import AnalysisApi
from idcheckio_python_client.api_client import ApiClient
from idcheckio_python_client.configuration import Configuration

class GetResult():

    def init(self):
        config = Configuration()
        config.username = "exemple@exemple.com"
        config.password = "exemple"
        api_client = ApiClient(host="http://api.idcheck.io/rest")
        self.api_analysis = AnalysisApi(api_client=api_client)


    def run(self, uid):
        try:
            result_response = self.api_analysis.get_result(uid)
            pprint(result_response)
        except ApiException as e:
            print("Exception when calling AnalysisApi->get_result: {}".format(e))
