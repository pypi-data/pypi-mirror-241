import typing

import botocore.exceptions


class LobotomyError(Exception):
    """Base exception class for all lobotomy custom exceptions."""

    def __init__(self, message: str):
        """Create the generic lobotomy error with the given message."""
        super(LobotomyError, self).__init__(message)


class NoResponseFound(LobotomyError):
    """Error raised when no response was found for the given method call."""

    pass


class NoSuchMethod(LobotomyError):
    """Error raised when a service method definition cannot be found."""

    pass


class DataTypeError(LobotomyError):
    """Error raised during casting of data types that fails."""

    pass


class RequestValidationError(LobotomyError):
    """Error raised when validation of the request arguments fails for a method call."""

    pass


class ErrorResponseError(typing.TypedDict):
    """Botocore error response error definition."""

    Code: str
    Message: typing.Optional[str]


class ErrorResponse(typing.TypedDict):
    """Botocore error response object interface."""

    Error: "ErrorResponseError"


class ClientError(botocore.exceptions.ClientError):
    """
    An exception that mirrors the structure of a boto3/botocore exception.

    This is used to create errors without the added complexity of those actual exception
    classes.
    """

    def __init__(
        self,
        error_response: typing.Optional["ErrorResponse"] = None,
        operation_name: typing.Optional[str] = None,
        **kwargs,
    ):
        """Create the error."""
        response = error_response or {
            "Error": {"Code": "Unknown", "Message": "Unknown"}
        }
        name = operation_name or "Unknown"
        super(ClientError, self).__init__(response, name)

    def populate(self, **kwargs) -> "ClientError":
        """Specify code and message for the client error."""
        code = kwargs.get("Code", "Unknown")
        message = kwargs.get("Message", "Unknown")
        error = {"Code": code, "Message": message}
        self.response = {"Error": error}
        self.operation_name = kwargs.get("operation_name", "Unknown")
        exception_message = self.MSG_TEMPLATE.format(
            error_code=code,
            error_message=message,
            operation_name=self.operation_name,
            retry_info="",
        )
        self.args = (exception_message,)
        return self
