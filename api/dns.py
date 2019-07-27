# -*- coding: utf-8 -*-

from configparser import ConfigParser
from system import cmd

# Loading config
config = ConfigParser()
config.read('config.ini')

# Settings from server
ADDC = config.get('Server', 'addc')
SRVR = config.get('Server', 'host')
USER = config.get('Server', 'user')
PASSWD = config.get('Server', 'passwd')

def dns_info():
	# samba-tool dns serverinfo localhost -U 'USER'%'PASSWD'
	pass

def zone_info():
	# samba-tool dns zoneinfo SRVR ADDC -U 'USER'%'PASSWD'
	pass

def zone_list():
	# samba-tool dns zonelist localhost -U 'USER'%'PASSWD'
	pass

def entry_list():
	addc = config.get('Server', 'addc')
	result = cmd("samba-tool dns query localhost addc @ ALL -U 'USER'%'PASSWD'")
	print(result)

def zone_create(zone):
	ip = server.split('.')
	query_direct = "samba-tool dns zonecreate localhost ip[2].ip[1].ip[0].in-addr.arpa -U 'USER'%'PASSWD'"
	query_reverse = "samba-tool dns add localhost ip[2].ip[1].ip[0].in-addr.arpa ip[3] PTR zone. -U 'USER'%'PASSWD'"

#def entry_add():
#    result = cmd("samba-tool dns add localhost ADDC pepe A 10.10.1.101 -U 'USER'%'PASSWD')
#    return result

#def entry_delete():
#    result = cmd("samba-tool dns delete localhost ADDC pepe A 10.10.1.101 -U 'USER'%'PASSWD')
#    return result

#PTR
def add_ptr():
	pass

def del_ptr():
	pass

#CNAME
def add_cname():
	pass

def del_cname():
	pass

# NS
def add_ns():
	pass

def del_ns():
	pass

#MX
def add_mx():
	pass

def del_mx():
	pass



