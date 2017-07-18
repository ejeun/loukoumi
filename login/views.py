from ldap3 import Server,Connection,ALL, NTLM
from django.shortcuts import render


def authenticate(name,pwd):
    server = Server('kgs.loc',get_info=ALL)
    conn = Connection(server, user=name, password=pwd, authentication=NTLM)

    if  conn.bind() == True:
        print('this is the POST from the request', name)
        return name
    else:
        return 'Wrong Pass'

def index(request) :
    # hardcoded for now
    pwd = ''
    name = ''
    authenticate(name,pwd)
    return render(request, 'login/index.html')

