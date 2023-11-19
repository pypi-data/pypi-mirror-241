class CliRequestsError(Exception):
    """Base exception for errors related to the cli_requests library."""

class HttpRequestError(CliRequestsError):
    """Exception raised for errors in HTTP requests."""

class HttpDownloadError(CliRequestsError):
    """Exception raised for errors in downloading files over HTTP."""

class CliRequestsArgumentError(CliRequestsError):
    """Exception related to errors in command-line arguments."""