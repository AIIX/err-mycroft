from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd
import re

class Mycroft(BotPlugin):
    """
    ask questions about mycroft and interact with a mycroft instance
    """

    @re_botcmd(pattern=r"doc.*mycroft|mycroft.*doc.*",
               prefixed=False, flags=re.IGNORECASE)
    def mycroft_docs(self, message, match):
        """A command which gives you the location to the mycroft docs"""
        return "The mycroft documentation can be found at \
        https://docs.mycroft.ai"

    @re_botcmd(pattern=r"install.*mycroft|mycroft.*install.*",
               prefixed=False, flags=re.IGNORECASE)
    def install_mycroft(self, message, match):
        """A command which gives you the location to the mycroft install"""
        return "The information for installing mycroft can be found here, \
        https://docs.mycroft.ai/installing.and.running"
