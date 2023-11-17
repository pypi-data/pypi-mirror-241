"""GPT-Terminal configuration file."""

import platform

APP_NAME = "gpt-terminal"

OPENAI_KEY = ''
MAX_TOKENS = 500
GPT_MODEL = 'gpt-3.5-turbo'


MODELS = {
    "gpt-3.5-turbo": 4097,
    "gpt-3.5-turbo-16k": 16385,
    "gpt-4": 8192,
    "gpt-4-32k": 32768,
}

MODELS_LIST = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-4",
    "gpt-4-32k",
]

def machine_info():
    """Get the current machine info."""

    return platform.platform()

INIT_SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""
- Your name is "GPTerminal".
- You are a helpful personal assistant for programers.
- You are running on {machine_info()} machine.
- Please note that your answers will be displayed on the terminal.
- So keep answers short as possible and use a suitable format for printing on a terminal.
""",
}


INIT_WELCOME_MESSAGE = {
    "role": "system",
    "content": """
- Please start the conversation with a random and short greeting message starts with 'Welcome to GPTerminal'.
- Add a ton of self humor.
- Keep it short as possible, one line.
""",
}

INIT_WELCOME_BACK_MESSAGE = {
    "role": "system",
    "content": """
The conversation you remember was a while ago, now we are continuing it.
Please start the conversation with a random and short welcome back message.
- Start with 'Welcome back to GPTerminal'.
- Add a ton of self humor.
- Keep it short as possible, one line.

After the welcome back message, please summarize the last conversation. (e.g. "Last time we talked about ...")
- End with a something that invites the user to continue the conversation.
""",
}

TITLE_MESSAGE = """
Please give this conversation a short title.
I'm going to use this title as a file name for the conversation.
There are going to a lot of files like that under a folder "~/.gpterminal/conversations"
- Hard limit of 5 words.
- Use underscores instead of spaces.
- Don't mention yourself in it. (e.g. "GPTerminal conversation")
- Don't use any special characters.
- Don't use any numbers.
- Don't use any capital letters.
- Don't use any spaces.
- Don't use any punctuation.
- Don't use any symbols.
- Don't use any emojis.
- Don't use any accents.
- Don't use quotes.
- Don't use word like: "macos", "programmer_assistant", "conversation".
- Don't use any file extensions. (e.g. ".txt" or ".json")
"""