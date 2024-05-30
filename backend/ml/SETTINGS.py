HOST = 'ch_server'
PORT = "8123"
TABLE_NAME = "Data"
DEVICE = "cuda"
LLM_PATH = "model-q8_0.gguf"
SYSTEM_PROMPT_HR = """
Потом придумаю что-то.

Инструкции:
1. Потом придумаю что-то.
"""

SYSTEM_PROMPT_HR_WITH_TEMPLATE = """
Потом придумаю что-то.

Инструкции:
1. Потом придумаю что-то.
КОНТЕКСТ: {}
"""

SYSTEM_TOKEN = 1587
USER_TOKEN = 2188
BOT_TOKEN = 12435
LINEBREAK_TOKEN = 13
ROLE_TOKENS = {"user": USER_TOKEN, "bot": BOT_TOKEN, "system": SYSTEM_TOKEN}
TG_TOKEN = "pass"
