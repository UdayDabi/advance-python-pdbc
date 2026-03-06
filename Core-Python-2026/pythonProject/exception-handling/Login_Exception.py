class LoginException(Exception):

    def __int__(self, msg):
        super().__int__(msg)


Login_id = "Admin"
Password = "Admin"

try:
    if Login_id == 'Admin' and Password == 'Admin':
        print("Valid User")

    else:
        raise LoginException("InValud User")

except LoginException as e:
    print('LoginException', e)
