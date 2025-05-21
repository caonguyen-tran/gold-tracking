import bcrypt

def get_password_hash(password: str) -> str:
    # convert password from str to bcrypt
    password_bytes = password.encode('utf-8')

    # generate random salt
    salt = bcrypt.gensalt()

    # hash password with salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)