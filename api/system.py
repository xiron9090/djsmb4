# -*- coding: utf-8 -*-

import platform
import commands

# system 
def actual_distro():
	distro = platform.dist()[0]
	return distro

def actual_version():
	version = platform.dist()[1]
	return version

def actual_release():
	release = platform.dist()[2]
	return release 

def cmd(shell_command):
    status, output = commands.getstatusoutput(shell_command)
    if status == 0:
        return output.splitlines()
