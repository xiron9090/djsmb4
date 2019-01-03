# -*- coding: utf-8 -*-

from system import cmd

def user_create(username, password, given_name, surname):
    query = "samba-tool user create '%s' '%s' --given-name='%s' --surname='%s'" % (
        username, password, given_name, surname)
    result = cmd(query)
    return result

def user_delete(username):
    result = cmd("samba-tool user delete %s" % (username))
    return result

def get_users():
    users = {'resultult': []}
    result = cmd("samba-tool user list|egrep -v 'Guest|krbtgt'")
    query = "|".join(result)
    get_users = cmd("pdbedit -Lf|egrep '%s'" % query)
    # print get_users
    for user in get_users:
        if user.split(':')[2]:
            users['resultult'].append({'username': user.split(
                ':')[0], 'full_name': user.split(':')[2]})
        else:
            users['resultult'].append({'username': user.split(
                ':')[0], 'full_name': user.split(':')[0].title()})

    return users



# user_create("pepe.perez", "password_for_pepe", "Jose", "Perez Hernandez")
