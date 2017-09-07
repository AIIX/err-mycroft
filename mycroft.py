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
        """A command that gives information about itself"""
        return "I am a bot to assist in Mycroft AI related questions and " \
               "issues."

    @botcmd()
    def mycroft_help(self, mess, args):
        """A command which gives you help info about the mycroft bot"""
        output = "I am here to help with topics related to\n " \
                 "What is mycroft\n How do I install mycroft\n " \
                 "Where is the mycroft documentation, and anything " \
                 "else about mycroft."
        return output

    @re_botcmd(pattern=r"install.*picroft|picroft.*install.*",
               prefixed=False, flags=re.IGNORECASE)
    def install_picroft(self, mess, args):
        """A command that gives information about installing picroft"""
        output = "The install guide for the picroft project can be found " \
                 "here, https://github.com/MycroftAI/enclosure-picroft/wiki" \
                 "/Getting-Started-Guide."
        return output

    @re_botcmd(pattern=r"doc.*picroft|picroft.*doc.*",
               prefixed=False, flags=re.IGNORECASE)
    def picroft_docs(self, mess, args):
        """A command that links you to the picroft documentation"""
        output = "The documentation for the picroft project can be found " \
                 "here, https://github.com/MycroftAI/enclosure-picroft/wiki."
        return output

    @re_botcmd(pattern=r"image.*picroft|picroft.*image.*",
               prefixed=False, flags=re.IGNORECASE)
    def picroft_image(self, mess, args):
        """A command that links you to the picroft image"""
        output = "The image for the picroft project can be found here, " \
                 "https://rebrand.ly/Picroft-0_8"
        return output

    @re_botcmd(pattern=r"skill.*list|list.*skill.*",
               prefixed=False, flags=re.IGNORECASE)
    def mycroft_skills(self, mess, args):
        """A command that links you the skills repo"""
        output = "The current list of mycroft skills can be found here, "\
                 "https://github.com/MycroftAI/mycroft-skills"
        return output

    @re_botcmd(pattern=r"skill.*available|available.*skill.*",
               prefixed=False, flags=re.IGNORECASE)
    def available_skills(self, mess, args):
        """A command that links you the skills repo"""
        output = "The current list of mycroft skills can be found here, " \
                 "https://github.com/MycroftAI/mycroft-skills"
        return output

