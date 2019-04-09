from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    Function that gets called when a user calls the /auth endpont
    with their username and password.
    :param username: User's username in string format
    :param password: User's un-encripted password in string format.
    :return: A user if authentication was successfull, none otherwise
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask_JWT
    verified their authorisation header is correct
    :param payload: A dictionary with 'identity' key, which is the user id.
    :return: A UserModel object.
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
