login = ''

def init(_login):
    global login
    login = _login 
    setting()

def set_arg(*args):
    print(args)

def setting():
    global login


