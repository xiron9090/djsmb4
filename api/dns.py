# -*- coding: utf-8 -*-

from configparser import ConfigParser
from system import cmd

# Loading config
config = ConfigParser()
config.read('config.ini')

# Settings from server
server = config.get('Server', 'host')
user = config.get('Server', 'user')
passw = config.get('Server', 'passwd')

def zone_create(zone):
	query_direct = "samba-tool dns zonecreate localhost 1.10.10.in-addr.arpa -U 'user'%'passw'"
	query_reverse = "samba-tool dns add localhost 1.10.10.in-addr.arpa 4 PTR zone. -U 'administrator'%'Admin*123'"

def entry_list():
    result = cmd("samba-tool group list")
    print(result)

def entry_update(groupname):
    result = cmd("samba-tool group delete '%s'" % (groupname))
    return result

def entry_delete(groupname):
    result = cmd("samba-tool group delete '%s'" % (groupname))
    return result
