#!/usr/bin/env python3

"""
Connect externally via ldap3 Python3 module parsing 
config.ini config file
"""

from ldap3 import Server, Connection, ALL
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

server = config.get('Server', 'host')
options = config.getboolean('Options', 'auto_bind')
conn = Connection(server, auto_bind=options)
print(conn)
