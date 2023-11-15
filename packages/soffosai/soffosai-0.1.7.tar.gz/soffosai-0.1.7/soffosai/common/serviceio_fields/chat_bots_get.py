'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-10
Purpose: Input/Output description for Chat Bots Get Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ChatBotsGetIO(ServiceIO):
    service = ServiceString.CHAT_BOTS_GET
    required_input_fields = []
    optional_input_fields = ["chatbot_ids"]
    input_structure = {
        "chatbot_ids": list
    }

    output_structure = {
        "chatbots": list
    }

