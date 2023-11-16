from typing import Optional


class ApiException(Exception):
    def __init__(self, code: int, status_text: str, message: Optional[str] = None):
        self.code = code
        self.status_text = status_text
        self.message = message or status_text

        super().__init__(f"Status {self.code} {self.status_text}: {self.message}")

    def compose(self):
        return ({"Status": f"{self.code} {self.status_text}"}, self.message)


class BadRequestException(ApiException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(400, "Bad Request", message=message)


class UnauthorizedException(ApiException):
    def __init__(self):
        super().__init__(401, "Unauthorized")


class PaymentRequiredException(ApiException):
    def __init__(self):
        super().__init__(402, "Payment Required")


class ForbiddenException(ApiException):
    def __init__(self):
        super().__init__(403, "Forbidden")


class NotFoundException(ApiException):
    def __init__(self):
        super().__init__(404, "Not Found")


class MethodNotAllowedException(ApiException):
    def __init__(self):
        super().__init__(405, "Method Not Allowed")


class NotAcceptableException(ApiException):
    def __init__(self):
        super().__init__(406, "Not Acceptable")


class ProxyAuthenticationRequiredException(ApiException):
    def __init__(self):
        super().__init__(407, "Proxy Authentication Required")


class RequestTimeoutException(ApiException):
    def __init__(self):
        super().__init__(408, "Request Timeout")


class ConflictException(ApiException):
    def __init__(self):
        super().__init__(409, "Conflict")


class GoneException(ApiException):
    def __init__(self):
        super().__init__(410, "Gone")


class LengthRequiredException(ApiException):
    def __init__(self):
        super().__init__(411, "Length Required")


class PreconditionException(ApiException):
    def __init__(self):
        super().__init__(412, "Precondition Failed")


class PayloadTooLargeException(ApiException):
    def __init__(self):
        super().__init__(413, "Payload Too Large")


class URITooLongException(ApiException):
    def __init__(self):
        super().__init__(414, "URI Too Long")


class UnsupportedMediaTypeException(ApiException):
    def __init__(self):
        super().__init__(415, "Unsupported Media Type")


class RangeNotSatisfiableException(ApiException):
    def __init__(self):
        super().__init__(416, "Range Not Satisfiable")


class ExpectationFailedException(ApiException):
    def __init__(self):
        super().__init__(417, "Expectation Failed")


class ImATeaPotException(ApiException):
    def __init__(self):
        super().__init__(418, "I'm a Teapot")


class MisdirectedRequestException(ApiException):
    def __init__(self):
        super().__init__(421, "Misdirected Request")


class UnprocessableContentException(ApiException):
    def __init__(self):
        super().__init__(422, "Unprocessable Content")


class LockedException(ApiException):
    def __init__(self):
        super().__init__(423, "Locked")


class FailedDependencyException(ApiException):
    def __init__(self):
        super().__init__(424, "Failed Dependency")


class TooEarlyException(ApiException):
    def __init__(self):
        super().__init__(425, "Too Early")


class UpgradeRequiredException(ApiException):
    def __init__(self):
        super().__init__(426, "Upgrade Required")


class PreconditionRequiredException(ApiException):
    def __init__(self):
        super().__init__(428, "Precondition Required")


class TooManyRequestsException(ApiException):
    def __init__(self):
        super().__init__(429, "Too Many Requests")


class RequestHeaderFieldsTooLargeException(ApiException):
    def __init__(self):
        super().__init__(431, "Request Header Fields Too Large")


class UnavailableForLegalReasonsException(ApiException):
    def __init__(self):
        super().__init__(451, "Unavailable For Legal Reasons")


class InternalServiceErrorException(ApiException):
    def __init__(self):
        super().__init__(500, "Internal Service Error")
