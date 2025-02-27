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



# import models into sdk package
from .models.check_summary_of_the_submitted_document import CheckSummaryOfTheSubmittedDocument
from .models.classification_of_the_submitted_document import ClassificationOfTheSubmittedDocument
from .models.control import Control
from .models.control_group import ControlGroup
from .models.detailed_information_of_the_holder_of_the_submitted_document import DetailedInformationOfTheHolderOfTheSubmittedDocument
from .models.detailed_information_of_the_submitted_document import DetailedInformationOfTheSubmittedDocument
from .models.error_response import ErrorResponse
from .models.event_date import EventDate
from .models.extracted_image import ExtractedImage
from .models.generic_data import GenericData
from .models.health_response import HealthResponse
from .models.image import Image
from .models.image_indicator import ImageIndicator
from .models.image_list_response import ImageListResponse
from .models.image_request import ImageRequest
from .models.mrz import Mrz
from .models.mrz_list_response import MrzListResponse
from .models.mrz_request import MrzRequest
from .models.mrz_response import MrzResponse
from .models.report_response import ReportResponse
from .models.result_response import ResultResponse
from .models.task_response import TaskResponse
from .models.user_response import UserResponse

# import apis into sdk package
from .apis.administration_api import AdministrationApi
from .apis.analysis_api import AnalysisApi
from .apis.sandbox_api import SandboxApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
