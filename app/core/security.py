import bcrypt

def hash_password(password):
    my_salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'),my_salt)
    return hashed.decode('utf-8')

def verify_hash_password(password,password_hash) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'),password_hash.encode('utf-8'))

