from passlib.context import CryptContext  
crypt_context  = CryptContext(schemes= ["bcrypt"],deprecated = "auto")

def hash(password: str):
    return crypt_context.hash(password)