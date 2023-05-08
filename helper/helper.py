from pprint import pprint
from random import choices, randint
from string import ascii_letters, digits, punctuation
from main import User


class UserHelper:
    @staticmethod
    def generate_users(count: int = 1):
        users = set()
        for i in range(count):
            email = "".join(choices(ascii_letters, k=randint(4, 9))) + "@gmail.com"
            password = "".join(
                [
                    x
                    for x in choices(
                        ascii_letters + digits + punctuation, k=randint(10, 19)
                    )
                ]
            )
            users.add(
                User(
                    email=email,
                    password=password,
                )
            )
        return users

