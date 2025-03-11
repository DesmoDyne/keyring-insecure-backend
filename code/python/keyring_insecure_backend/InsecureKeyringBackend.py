# keyring.py
#
# Insecure Keyring Backend implementation.
#
# author  : stefan schablowski
# contact : stefan.schablowski@desmodyne.com
# created : 2025-03-11


# Keyring > Write your own keyring backend:
#   https://github.com/jaraco/keyring ...
#    ... ?tab=readme-ov-file#write-your-own-keyring-backend


# https://pypi.org/project/keyring
from keyring.backend import KeyringBackend


class InsecureKeyringBackend(KeyringBackend):
    """
    An insecure Keyring backend that stores secrets in plain text.
    """

    # TODO: doc
    priority = 30


    def delete_password(self, service: str, username: str) -> None:
        """
        TODO: doc
        """

        raise NotImplementedError


    def get_password(self, service: str, username: str) -> str:
        """
        TODO: doc
        """

        return 'some password'


    def set_password(self, service: str, username: str, password: str) -> None:
        """
        TODO: doc
        """

        raise NotImplementedError
