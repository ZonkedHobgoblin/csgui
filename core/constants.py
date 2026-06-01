import platform
from pathlib import Path

class Env:
    OS_NAME = platform.system()
    SCRIPT_PATH = Path(__file__).resolve().parent.parent
class AppMeta:
    CSGUI_VER = "v0.0.1"
    REPO_URL = "https://github.com/ZonkedHobgoblin/csgui"
    API_REPO_URL = "https://api.github.com/repos/ZonkedHobgoblin/csgui/releases/latest"

class UIConstants:
    CLI_INPUT_PROMPT = "> "

class ErrorCodes:
    CONFIG_SAVE = "CM-ER-000"
    CONFIG_CORRUPT = "CM-ER-001"
    CONFIG_NOTFOUND = "CM-ER-002"
    CONFIG_PARSE = "CM-ER-003"
    CONFIG_UNKOWN = "CM-ER-004"