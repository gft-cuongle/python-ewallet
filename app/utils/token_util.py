import jwt

# Define your secret key
secret = 'python_e_wallet_secret_key'


def init_jwt_token(payload):
    # Generate the token
    token = jwt.encode(payload, secret)
    return token


def jwt_decode(token):
    try:
        decoded_payload = jwt.decode(token, secret)
        print(decoded_payload)
        return decoded_payload
    except jwt.exceptions.DecodeError:
        print('Invalid token')
