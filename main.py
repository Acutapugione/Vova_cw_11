from pprint import pprint
from my_class.user import User
from helper.helper import UserHelper
from time import time, sleep


if __name__ == '__main__':
    pprint( UserHelper.generate_users(125) )
