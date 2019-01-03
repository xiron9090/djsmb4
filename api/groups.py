# -*- coding: utf-8 -*-

from system import cmd

def group_create(groupname):
    query = "samba-tool group add '%s'" % (groupname)
    result = cmd(query)
    return result

def group_list():
    result = cmd("samba-tool group list")
    print(result)

def group_delete(groupname):
    result = cmd("samba-tool group delete '%s'" % (groupname))
    return result

def get_groups():
    ls_groups = sorted(cmd("samba-tool group list"))
    return ls_groups
