'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-13
Purpose: Input/Output description for Website Converter Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class WebsiteConverterIO(ServiceIO):
    service = ServiceString.WEBSITE_CONVERTER
    required_input_fields = ["url"]
    optional_input_fields = []
    input_structure = {
        "url": str
    }

    output_structure = {
        "text": str,
        "links": dict
    }

