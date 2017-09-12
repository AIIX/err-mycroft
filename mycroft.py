from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd
import re


class Mycroft(BotPlugin):

    """
    ask questions about mycroft and interact with a mycroft instance
    """

    @botcmd
    def mycroft_docs(self, message, match):
        """A command which gives you the location to the mycroft docs"""

        output = "The mycroft documentation can be found at " \
                 "https://docs.mycroft.ai"

        return output

    @botcmd
    def install_mycroft(self, message, match):
        """A command which gives you the location to the mycroft install"""

        output = "The information for installing mycroft can be found here, " \
                 "https://docs.mycroft.ai/installing.and.running"

        return output

    @botcmd
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

    @botcmd
    def about_me(self, mess, args):
        """A command that gives information about itself"""
        return "I am a bot to assist in Mycroft AI related questions and " \
               "issues."

    @botcmd
    def install_picroft(self, mess, args):
        """A command that gives information about installing picroft"""
        output = "The install guide for the picroft project can be found " \
                 "here, https://github.com/MycroftAI/enclosure-picroft/wiki" \
                 "/Getting-Started-Guide."
        return output

    @botcmd
    def install_plasmoid(self, mess, args):
        """A command that gives information about installing KDE Plasmoid"""
        output = "Follow the plasmoid install guide" \
                 "at, https://cgit.kde.org/plasma-mycroft.git/tree/Readme.md" \
                 "If you are running an Ubuntu or Fedora based distribution" \
                 "You can find the installation scripts" \
                 "here, https://github.com/MycroftAI/installers"
        return output

    @botcmd
    def install_qtapplication(self, mess, args):
        """A command that gives info about installing the QTApplication"""
        output = "Appimage for the standalone Qtapplication is available at" \
                 "https://github.com/AIIX/Mycroft-Ai-QtApplication/releases"
        return output

    @botcmd
    def troubleshoot_plasmoid(self, mess, args):
        """A command that gives troublehooting info for the KDE Plasmoid"""
        output = "Steps to troubleshoot your plasmoid install" \
                 "1: Check if mycroft is installed correctly" \
                 "2: Open plasmoid settings and check your mycroft path" \
                 "3: Run plasmashell in debug mode report error messages" \
                 "4: Submit your issue's on the #desktop channel, or" \
                 "5: Create a bug report at https://bugs.kde.org" \
                 "/describecomponents.cgi?product=plasma-mycroft"
        return output

    @botcmd
    def picroft_docs(self, mess, args):
        """A command that links you to the picroft documentation"""
        output = "The documentation for the picroft project can be found " \
                 "here, https://github.com/MycroftAI/enclosure-picroft/wiki."
        return output

    @botcmd
    def picroft_image(self, mess, args):
        """A command that links you to the picroft image"""
        output = "The image for the picroft project can be found here, " \
                 "https://rebrand.ly/Picroft-0_8"
        return output

    @botcmd
    def mycroft_skills(self, mess, args):
        """A command that links you the skills repo"""
        output = "The current list of mycroft skills can be found here, "\
                 "https://github.com/MycroftAI/mycroft-skills"
        return output

    @botcmd
    def available_skills(self, mess, args):
        """A command that links you the skills repo"""
        output = "The current list of mycroft skills can be found here, " \
                 "https://github.com/MycroftAI/mycroft-skills"
        return output

    @botcmd
    def desktop_clients(self, mess, args):
        """A command that list currently available desktop clients"""
        output = "The current list of mycroft desktop clients, " \
                 "KDE: http://cgit.kde.org/plasma-mycroft.git/tree/Readme.md" \
                 "Others: https://github.com/AIIX/Mycroft-AI-QtApplication"
        return output

    @botcmd
    def wake_word(self, mess, args):
        """A command that links you how to change the wake word"""
        output = "You can adjust the wake word and sensitivity of mycroft " \
                 "by using the docs here, " \
                 "https://docs.mycroft.ai/installing.and.running/faq"
        return output

    @botcmd
    def hello(self, message, match):
        """A command which responds to hello"""
        output = "Hello I can answer things related to Mycroft, you can " \
                 "ask me things like where are the mycroft docs, etc." \
                 "You can also ask !help or /help to get more info."

        return output
