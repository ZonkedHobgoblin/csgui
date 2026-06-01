"""
01/06/26 - cli.py
Command-Line alternative/fallback for the CS:GUI app
"""

import sys
from core.constants import Env, AppMeta, UIConstants
from utils.cli_utils import CLIUtils
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def _(message: str) -> str: ...
    """Dev only - Stops IDE errors"""

class CLIInterface:
    
    
    def __init__(self, config_ref):
        self.config = config_ref
        
        
    def run(self):
        self.config.load()
        self.current_config = self.config.settings
        while True:
            CLIUtils.clear()
            self.menu()
            match CLIUtils.get_sanitized_num_input(UIConstants.CLI_INPUT_PROMPT, int, 1, 4):
                case 1:
                    CLIUtils.clear()
                case 2:
                    CLIUtils.clear()
                    self.config_menu()
                case 3:
                    CLIUtils.clear()
                    self.show_about()
                case 4:
                    break
    
    
    def menu(self) -> None:
        """Displays the main menu and captures the user's choice."""
        print(_("CS:GUI Menu:\n"
                "\n1 - n/a\n2 - Config\n3 - About\n4 - Quit\n"))
        
        
    def show_about(self) -> None:
        """Displays information about the script."""
        print(_("About:\n\nCS:GUI {csgui_ver} by zonkedhobgoblin\n"
        "{repo_url}\n\n"
        "N/A.\n\n").format(csgui_ver=AppMeta.CSGUI_VER, repo_url=AppMeta.REPO_URL))
        CLIUtils.pause()

    def config_menu(self) -> None:
        """Handles the configuration sub-menu, allowing the user to mutate settings."""
        CLIUtils.clear()
        
        
        
    def handle_config_io(self) -> None:
        """Handles the loading and saving of the config manager."""
        status = self.config.load()
        match status:
            case "SUCCESS":
                pass
                
            case "ERR_CORRUPT":
                print(_("Config file is possibly corrupted! Using default settings."))
                pass
                
            case "ERR_NOTFOUND":
                print(_("Config file not found! Using default settings."))
                pass
            
            case "ERR_PARSE":
                print(_("Config file contains incorrect values! Using default settings."))
                pass
                
            case "ERR_UNKOWN":
                print(_("An unknown error occured! Using default settings."))
                pass
            
            case _:
                print(_("Something went wrong when attempting to load config file. Exiting."))
                sys.exit(1)
                
        status = self.config.save()
        match status:
            case "SUCCESS":
                pass
            case "ERR_SAVE":
                print(_("Something went wrong when attempting to save config file. Exiting."))
                sys.exit(1)