import os
from exceptions import PrivateKeyDoesNotExistError

class Secrets:

    def __init__(self) -> None:
        self.check_existing()

    @property
    def private_key(self):
        if not (secret_key := os.environ.get('PRIVATE_KEY')):
            raise PrivateKeyDoesNotExistError('Please set up `PRIVATE_KEY` to environ')
        return secret_key

    def check_existing(self):
        self.private_key
