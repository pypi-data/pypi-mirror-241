from .chromaconsole import enabled

class Text:
    @staticmethod
    def black():
        return "\033[30m" if enabled else ""
        
    @staticmethod
    def red():
        return "\033[31m" if enabled else ""
        
    @staticmethod
    def green():
        return "\033[32m" if enabled else ""
        
    @staticmethod
    def yellow():
        return "\033[33m" if enabled else ""
        
    @staticmethod
    def blue():
        return "\033[34m" if enabled else ""
        
    @staticmethod
    def magenta():
        return "\033[35m" if enabled else ""
        
    @staticmethod
    def cyan():
        return "\033[36m" if enabled else ""
    
    @staticmethod
    def white():
        return "\033[37m" if enabled else ""
    
    @staticmethod
    def br_black():
        return "\033[90m" if enabled else ""
        
    @staticmethod
    def br_red():
        return "\033[91m" if enabled else ""
        
    @staticmethod
    def br_green():
        return "\033[92m" if enabled else ""
        
    @staticmethod
    def br_yellow():
        return "\033[93m" if enabled else ""
        
    @staticmethod
    def br_blue():
        return "\033[94m" if enabled else ""
        
    @staticmethod
    def br_magenta():
        return "\033[95m" if enabled else ""
        
    @staticmethod
    def br_cyan():
        return "\033[96m" if enabled else ""
    
    @staticmethod
    def br_white():
        return "\033[97m" if enabled else ""