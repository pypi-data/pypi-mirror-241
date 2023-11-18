from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class APIError(BaseModel):
    error: str
    errorMessage: str


class IllegalArgumentException(Exception):
    pass


class ForbiddenOperationException(Exception):
    pass


class UnknownException(Exception):
    pass


class User(BaseModel):
    id: UUID
    name: str


class UsernameInHistory(BaseModel):
    is_current: bool = True
    name: str
    changedToAt: datetime | None = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.changedToAt:
            self.is_current = False


class MCAuthRequest(BaseModel):
    username: str
    password: str
    clientToken: UUID
    requestUser: bool = False


class MCUserProperties(BaseModel):
    name: str
    value: str


class MCProfile(BaseModel):
    id: UUID
    name: str


class MCUser(BaseModel):
    id: UUID
    username: str
    properties: list[MCUserProperties]


class MCAuthResponse(BaseModel):
    accessToken: str
    clientToken: UUID
    availableProfiles: list[MCProfile]
    selectedProfile: MCProfile
    user: MCUser | None = None


class MCRefreshRequest(BaseModel):
    accessToken: str
    clientToken: UUID
    requestUser: bool = False


class MCSignOutRequest(BaseModel):
    username: str
    password: str


class MCInvalidateRequest(BaseModel):
    accessToken: str
    clientToken: UUID
