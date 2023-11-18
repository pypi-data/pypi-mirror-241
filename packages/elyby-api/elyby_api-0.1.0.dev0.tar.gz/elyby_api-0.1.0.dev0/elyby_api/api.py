import time
from datetime import datetime
from uuid import UUID

import requests

from elyby_api._types import MCAuthRequest, MCAuthResponse, UnknownException, MCRefreshRequest, User, UsernameInHistory, APIError, IllegalArgumentException, MCSignOutRequest, MCInvalidateRequest
from elyby_api.utils import get_exception

BASE_URL = 'https://authserver.ely.by'
API_URL = f'{BASE_URL}/api'
AUTH_URL = f'{BASE_URL}/auth'


class BaseAPI:

    @staticmethod
    def get_user_by_username(username: str, at_time: datetime | None = None) -> User | None:
        """
        Get user from uuid


        >>> BaseAPI.get_user_by_username('ErickSkrauch')
        User(id=UUID('ffc8fdc9-5824-509e-8a57-c99b940fb996'), name='ErickSkrauch')
        >>> BaseAPI.get_user_by_username('')
        Traceback (most recent call last):
        ...
        elyby_api._types.IllegalArgumentException: Invalid username format.
        >>> BaseAPI.get_user_by_username('a') is None
        True


        :param username: Ely.by - Username
        :param at_time: Time relative to which the user will be received
        :return: User class
        """

        if not username:
            raise IllegalArgumentException('Invalid username format.')

        url = f'{API_URL}/users/profiles/minecraft/{username}'

        if at_time:
            timestamp = time.mktime(at_time.timetuple())
            url += f'?at={round(timestamp)}'

        resp = requests.get(url)
        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 204:
            return

        if resp.status_code == 200:
            return User(**resp.json())

        return

    @staticmethod
    def get_name_history(uuid: UUID | str) -> list[UsernameInHistory] | None:
        """
        Return username history by user UUID


        >>> BaseAPI.get_name_history('ffc8fdc95824509e8a57c99b940fb996')[0].name
        'ErickSkrauch'
        >>> BaseAPI.get_name_history('')
        Traceback (most recent call last):
        ...
        elyby_api._types.IllegalArgumentException: Invalid uuid format.
        >>> BaseAPI.get_name_history('123')
        Traceback (most recent call last):
        ...
        elyby_api._types.IllegalArgumentException: Invalid uuid format.
        >>> BaseAPI.get_name_history('ffffffffffffffffffffffffffffffff') is None
        True


        :param uuid: User UUID
        :return: UsernameInHistory type from elyby_api._types
        """
        if not uuid:
            raise IllegalArgumentException('Invalid uuid format.')

        url = f'{API_URL}/user/profiles/{str(uuid)}/names'

        resp = requests.get(url)
        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 204:
            return

        if resp.status_code == 200:
            history = []
            for i in resp.json():
                history.append(UsernameInHistory(**i))
            return history

    @staticmethod
    def get_users_by_usernames(usernames: list[str]) -> list[User]:
        """
        Return users list by usernames


        >>> a, b, c = BaseAPI.get_users_by_usernames(["ErickSkrauch", "EnoTiK", "KmotherfuckerF"])
        >>> a
        User(id=UUID('ffc8fdc9-5824-509e-8a57-c99b940fb996'), name='ErickSkrauch')
        >>> b
        User(id=UUID('27c22edc-7b82-5616-babc-6cd88079f55e'), name='enotik')
        >>> c
        User(id=UUID('39f42ba7-23de-56d9-8867-eabafc5e8e91'), name='KmotherfuckerF')
        >>> a = []
        >>> for _ in range(101): a.append('a')
        >>> BaseAPI.get_users_by_usernames(a)
        Traceback (most recent call last):
        ...
        elyby_api._types.IllegalArgumentException: Not more that 100 profile name per call is allowed.
        >>> BaseAPI.get_users_by_usernames([])
        []
        >>> BaseAPI.get_users_by_usernames(['a'])
        []


        :param usernames: List of usernames
        :return: List of users
        """

        if len(usernames) > 100:
            raise IllegalArgumentException('Not more that 100 profile name per call is allowed.')
        if not usernames:
            return []

        url = f'{API_URL}/profiles/minecraft'

        resp = requests.post(url, json=usernames)

        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            usernames = []
            for i in resp.json():
                usernames.append(User(**i))
            return usernames

        return []


class MCAuthAPI:

    @staticmethod
    def authenticate(data: MCAuthRequest) -> MCAuthResponse:
        """
        Authenticate by username and password


        >>> import uuid
        >>> class FakeResponse: status_code = 200
        >>> FakeResponse.json = lambda: {"accessToken":"fakeaccesstoken","clientToken":"ffffffffffffffffffffffffffffffff","availableProfiles":[{"id": "ffffffffffffffffffffffffffffffff","name": "fakeusername"}],"selectedProfile": {"id": "ffffffffffffffffffffffffffffffff","name": "fakeusername"},"user": {"id": "ffffffffffffffffffffffffffffffff","username": "fakeusername","properties": [{"name": "preferredLanguage","value": "ru"}]}}
        >>> requests.post = lambda _, json: FakeResponse
        >>> MCAuthAPI.authenticate(MCAuthRequest(username='fakeusername1', password='pass123', clientToken=uuid.uuid1(), requestUser=True))
        MCAuthResponse(accessToken='fakeaccesstoken', clientToken=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), availableProfiles=[MCProfile(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), name='fakeusername')], selectedProfile=MCProfile(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), name='fakeusername'), user=MCUser(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), username='fakeusername', properties=[MCUserProperties(name='preferredLanguage', value='ru')]))


        :param data: Authenticate data
        :return: MCAuthResponse type
        """

        url = f'{AUTH_URL}/authenticate'

        resp = requests.post(url, json=data.model_dump_json())
        if resp.status_code == 401 or resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            return MCAuthResponse(**resp.json())

        raise UnknownException(resp.text)

    @staticmethod
    def refresh(data: MCRefreshRequest) -> MCAuthResponse:
        """
        Updates valid accessToken


        >>> import uuid
        >>> class FakeResponse: status_code = 200
        >>> FakeResponse.json = lambda: {"accessToken":"fakeaccesstoken","clientToken":"ffffffffffffffffffffffffffffffff","availableProfiles":[{"id": "ffffffffffffffffffffffffffffffff","name": "fakeusername"}],"selectedProfile": {"id": "ffffffffffffffffffffffffffffffff","name": "fakeusername"},"user": {"id": "ffffffffffffffffffffffffffffffff","username": "fakeusername","properties": [{"name": "preferredLanguage","value": "ru"}]}}
        >>> requests.post = lambda _, json: FakeResponse
        >>> MCAuthAPI.refresh(MCRefreshRequest(accessToken='faketoken', clientToken=uuid.uuid1(), requestUser=True))
        MCAuthResponse(accessToken='fakeaccesstoken', clientToken=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), availableProfiles=[MCProfile(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), name='fakeusername')], selectedProfile=MCProfile(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), name='fakeusername'), user=MCUser(id=UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'), username='fakeusername', properties=[MCUserProperties(name='preferredLanguage', value='ru')]))


        :param data: MCRefreshRequest type
        :return: MCAuthResponse type
        """

        url = f'{AUTH_URL}/refresh'

        resp = requests.post(url, json=data.model_dump_json())
        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            return MCAuthResponse(**resp.json())

        raise UnknownException(resp.text)

    @staticmethod
    def validate(accessToken: str) -> bool:
        """
        Validate token


        >>> class FakeResponse: status_code = 400
        >>> FakeResponse.text = '{"error":"ForbiddenOperationException","errorMessage":"Token expired."}'
        >>> FakeResponse.json = lambda: {"error":"ForbiddenOperationException","errorMessage":"Token expired."}
        >>> requests.post = lambda _, json: FakeResponse
        >>> MCAuthAPI.validate('')
        False
        >>> class FakeResponse: status_code = 200
        >>> MCAuthAPI.validate('')
        True


        :param accessToken: User access token
        :return: Return bool value depending on whether the token is valid or not
        """

        url = f'{AUTH_URL}/validate'

        resp = requests.post(url, json={'accessToken': accessToken})
        if resp.status_code == 400 or resp.status_code == 401:
            if resp.text and resp.json().get('errorMessage') == 'Token expired.':
                return False
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            return True

        raise UnknownException(resp.text)

    @staticmethod
    def signout(data: MCSignOutRequest) -> None:
        """
        This query enables the invalidation of all tokens issued to the user.


        >>> class FakeResponse:pass
        >>> FakeResponse.status_code = 400
        >>> FakeResponse.json = lambda: {'error':'ForbiddenOperationException','errorMessage':'fakeerror'}
        >>> requests.post = lambda _, json: FakeResponse
        >>> MCAuthAPI.signout(MCSignOutRequest(username='fakeusername', password='pass123'))
        Traceback (most recent call last):
        ...
        elyby_api._types.ForbiddenOperationException: fakeerror
        >>> FakeResponse.status_code = 200
        >>> MCAuthAPI.signout(MCSignOutRequest(username='fakeusername', password='pass123')) is None
        True


        :param data: MCSignOutRequest type
        :return: None
        """

        url = f'{AUTH_URL}/signout'

        resp = requests.post(url, json=data.model_dump_json())

        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            return

        raise UnknownException(resp.text)

    @staticmethod
    def invalidate(data: MCInvalidateRequest) -> None:
        """
        The query allows you to invalidate the accessToken.


        >>> import uuid
        >>> class FakeResponse:pass
        >>> FakeResponse.status_code = 400
        >>> FakeResponse.json = lambda: {'error':'ForbiddenOperationException','errorMessage':'fakeerror'}
        >>> requests.post = lambda _, json: FakeResponse
        >>> MCAuthAPI.invalidate(MCInvalidateRequest(accessToken='faketoken', clientToken=uuid.uuid1()))
        Traceback (most recent call last):
        ...
        elyby_api._types.ForbiddenOperationException: fakeerror
        >>> FakeResponse.status_code = 200
        >>> MCAuthAPI.invalidate(MCInvalidateRequest(accessToken='faketoken', clientToken=uuid.uuid1())) is None
        True


        :param data: MCInvalidateRequest type
        :return: None
        """

        url = f'{AUTH_URL}/invalidate'

        resp = requests.post(url, json=data.model_dump_json())

        if resp.status_code == 400:
            error = APIError(**resp.json())
            raise get_exception(error)

        if resp.status_code == 200:
            return

        raise UnknownException(resp.text)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
