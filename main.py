import logging
import sys
import traceback
from utils import LoggerSetup, I18nSetup
from ui import CLIInterface
from core import ConfigManager

class csguiApp:
    
    
    def __init__(self):
        LoggerSetup.initialize()
        I18nSetup.initialize()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Starting CSGUI")
        
        config_manager = ConfigManager()
        # yet to implement - updater = Updater()
        
        self.ui = CLIInterface(config_manager)
        self.logger.info("CSGUI initialized")
    
    
    def start(self):
        self.ui.run()
        self.logger.info("CSGUI stopped")


if __name__ == "__main__":
    try:
        app = csguiApp()
        app.start()
        
    except KeyboardInterrupt:
        print("\nExiting CSGUI...")
        sys.exit(0)
        
    except Exception:
        # if launch fails, we can fallback to traceback if logger wasnt setup
        error_details = traceback.format_exc()
        
        logger = logging.getLogger(__name__)
        
        if logging.getLogger().hasHandlers():
            logger.critical("A fatal unhandled exception occurred!", exc_info=True)
            print("\nAn unexpected error occurred. Please check csgui.log for details.")
            
        else:
            fallback_file = "csgui_crash.log"
            try:
                with open(fallback_file, "a", encoding="utf-8") as f:
                    f.write(f"FATAL CRASH PRE-INIT:\n{error_details}\n")
                print(f"\nCritical failure before initialization. Check {fallback_file} for details.")
            except Exception:
                print("\nCritical failure and cannot write to disk. Error details:")
                print(error_details, file=sys.stderr)
                
        sys.exit(1)