import logger
import uuid


class User:
    def __init__(self, username, userpass, email):
        self.id = uuid.uuid4()
        self._username = username
        self._userpass = userpass
        self.email = email
        self.log = logger
        self.log.info(f'New user {self._username})

    @property
    def username(self):
        return self._username

    @property
    def userpass(self):
        self.log.error(f' enter correct pass for {self._username})
        return '*' * len(self._userpass)
                
