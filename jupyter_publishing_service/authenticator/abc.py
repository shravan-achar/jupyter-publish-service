from abc import ABC, abstractmethod


class Authenticator(ABC):

    @abstractmethod
    def authenticate(self, data) -> dict:
        """
        Authenticate a user with login data

        This must be non-blocking co-routine

        Must return username on successful authentication,
        and return None on failed authentication

        Args:
            data (dict): Login data

        Returns:
            user (dict or None): Must return a dict with key 'name' with a unique value. Can include other fields
        """
        ...
