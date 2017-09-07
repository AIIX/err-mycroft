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

        output = "The mycroft documentation can be found at " \
                 "https://docs.mycroft.ai"

        return output

    @re_botcmd(pattern=r"install.*mycroft|mycroft.*install.*",
               prefixed=False, flags=re.IGNORECASE)
    def install_mycroft(self, message, match):
        """A command which gives you the location to the mycroft install"""

        output = "The information for installing mycroft can be found here, " \
                 "https://docs.mycroft.ai/installing.and.running"

        return output

    @re_botcmd(pattern=r"what.i.*mycroft|mycroft.*what.*",
               prefixed=False, flags=re.IGNORECASE)
    def what_mycroft(self, message, match):
        """A command which gives you information about mycroft"""
        output = "Mycroft Core is the primary module that makes up the " \
                 "Mycroft Artificial Intelligence platform.  Mycroft makes " \
                 "use of the Adapt Intent Parser, Speech-to-Text software, " \
                 "and Text-to-Speech. The idea behind the platform " \
                 "is to be able to voice enable any device and turn " \
                 "it into a smart personal assistant, able to perform a " \
                 "variety of tasks. Mycroft is often used to refer " \
                 "to the hardware product produced by Mycroft AI, Inc. " \
                 "- so to avoid confusion, the software stack is " \
                 "often referred to as \"Mycroft Core\", more info can be " \
                 "found here, https://docs.mycroft.ai"

        return output

    @botcmd(split_args_with=None)
    def about_me(self, mess, args):
        return "I am a bot to assist in Mycroft AI related questions and issues."