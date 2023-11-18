from elyby_api._types import APIError, IllegalArgumentException, ForbiddenOperationException, UnknownException


def get_exception(exception: APIError) -> Exception:
    if exception.error == 'IllegalArgumentException':
        return IllegalArgumentException(exception.errorMessage)
    if exception.error == 'ForbiddenOperationException':
        return ForbiddenOperationException(exception.errorMessage)
    return UnknownException(exception.errorMessage)
