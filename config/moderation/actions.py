import os
from typing import Any, List, Optional

from nemoguardrails.actions import action
from nemoguardrails import LLMRails


@action()
async def block_list(file_name: Optional[str] = None, context: Optional[dict] = None):
    bot_response = context.get("last_bot_message")
    root_path = os.path.dirname(__file__)

    with open(os.path.join(root_path, file_name)) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        if line in bot_response:
            return True
    return False

def init(llm_rails: LLMRails):
    llm_rails.register_action("block_list", block_list)