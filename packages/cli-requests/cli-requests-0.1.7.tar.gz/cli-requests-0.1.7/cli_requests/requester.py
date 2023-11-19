import requests
from colorama import Fore
from .colorizer import colorize_error
from .exceptions import *


class Requester:
    def __init__(self) -> None:
        pass

    def request(
        self,
        url: str,
        params: dict = None,
        files: dict = None,
        proxies: dict = None,
        method: str = 'GET',
        data: dict = None,
        headers: dict = None,
        timeout: float = None,
        auth: tuple = None,
        cookies: dict = None,
        verify: bool = True,
        cert: str = None,
        allow_redirects: bool = True,
        nocolor=False,
    ) -> requests.Response:
        try:
            response = requests.request(
                method,
                url,
                params=params,
                files=files,
                proxies=proxies,
                data=data,
                headers=headers,
                timeout=timeout,
                auth=auth,
                cookies=cookies,
                verify=verify,
                cert=cert,
                allow_redirects=allow_redirects
            )
            
            response.raise_for_status()

            return response
        
        except requests.exceptions.HTTPError as errh:
            err_text = f"HTTP Error: {errh}"
            raise HttpRequestError(colorize_error(err_text) if not nocolor else err_text) from errh
        except requests.exceptions.ConnectionError as errc:
            err_text = f"Error Connecting: {errc}"
            raise CliRequestsError(colorize_error(err_text) if not nocolor else err_text) from errc
        except requests.exceptions.Timeout as errt:
            err_text = f"Timeout Error: {errt}"
            raise CliRequestsError(colorize_error(err_text) if not nocolor else err_text) from errt
        except requests.exceptions.RequestException as err:
            err_text = f"Error: {err}"
            raise CliRequestsError(colorize_error(err_text) if not nocolor else err_text) from err