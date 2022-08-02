'''
.. autoclass:: APIError
.. autoclass:: ConnectionError
.. autoclass:: ImpersonationError
.. autoclass:: NotFoundError
.. autoclass:: PackageMissingError
.. autoclass:: PasswordComplexityError
.. autoclass:: RetryError
.. autoclass:: ServerError
.. autoclass:: TenableException
.. autoclass:: TioExportsError
.. autoclass:: TioExportsTimeout
.. autoclass:: UnexpectedValueError
.. autoclass:: UnknownError
.. autoclass:: UnsupportedError
'''
from restfly.errors import *


class AuthenticationWarning(Warning):  # noqa: PLW0622
    '''
    An authentication warning is thrown when an unauthenticated API session is
    initiated.
    '''


class FileDownloadError(RestflyException):
    '''
    FileDownloadError is thrown when a file fails to download.

    Attributes:
        msg (str):
            The error message
        filename (str):
            The Filename or file id that was requested.
        resource (str):
            The resource that the file was requested from (e.g. "scans")
        resource_id (str):
            The identifier for the resource that was requested.
    '''

    def __init__(self, resource: str, resource_id: str, filename: str):
        self.resource = resource
        self.resource_id = resource_id
        self.filename = filename
        self.msg = (f'resource {resource}:{resource_id} '
                    f'requested file {filename} and has failed.'
                    )


class TioExportsError(RestflyException):
    '''
    When the exports APIs throw an error when processing an export, pyTenable
    will throw this error in turn to relay that context to the user.
    '''

    def __init__(self, export: str, uuid: str):
        self.export = export
        self.uuid = uuid
        super().__init__(self, r'{export} export {uuid} has errored.')


class TioExportsTimeout(TioExportsError):
    '''
    When an export has been cancelled due to timeout, this error is thrown.
    '''


class ImpersonationError(APIError):
    '''
    An ImpersonationError exists when there is an issue with user impersonation.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''


class PasswordComplexityError(APIError):
    '''
    PasswordComplexityError is thrown when attempting to change a password and
    the password complexity is insufficient.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
