class User:
    def __init__(self, username, password):
        if len(username) <=3:
            raise UserException()
        if len(password) <=5:
            raise PasswordException()
        
        #if not any(c.isdigit() for c in password) or not any (c.isalpha() for c in password):
            #raise PasswordException("Le mot de passe doit contenir un chiffre ou une lettre")
        
        self.username = username
        self.password = password

class PasswordException(Exception):
    def __init__(self, msg="Mot de passe trop court", *args, **kwargs ):
        super().__init__(msg, *args, **kwargs)

class UserException(Exception):
    def __init__(self, msg="Utilisateur trop court", *args, **kwargs ):
        super().__init__(msg, *args, **kwargs)

if __name__ == "__main__":
    user = User("John","supersecret")
    try:
        user = User("t", "supersecret")
    except UserException:
        print("L'exception sur le nom a été levée")
    
    try:
        user = User("John", "t")
    except PasswordException:
        print("L'exception sur le mot de passe a été levée")