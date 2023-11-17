"""GPT-Terminal GPT Settings file."""

import openai
from gpterminal.config import OPENAI_KEY, MAX_TOKENS, GPT_MODEL
from gpterminal.checks import check_api, check_max_tokens, check_model

check_api(OPENAI_KEY)
check_model(GPT_MODEL)
check_max_tokens(MAX_TOKENS)

openai.api_key = OPENAI_KEY




def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message['content']
