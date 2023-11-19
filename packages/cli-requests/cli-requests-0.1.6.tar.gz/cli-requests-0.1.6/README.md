# Cli-Requests

**Cli-Requests** is a command-line interface tool for simplifying HTTP requests. It allows you to effortlessly interact with APIs and websites directly from the terminal. This tool is designed to provide a seamless experience, enabling you to focus on making requests without the complexities of traditional tools.

## Installation

To get started with Cli-Requests, you can install it using pip. Ensure you have Python 3.8 or higher installed.

```bash
pip3 install cli-requests
```

## Usage

Cli-Requests makes it easy to send HTTP requests with various options. Here are some examples:

### Basic Request

```bash
cli-requests https://example.com/
```
It's a basic GET request that will return nothing on success or an error.

### Get Specific Response Data

You can use various command-line arguments to get specific information from the response:

- `--status-code`: Show the HTTP status code.
- `--headers-content`: Show the response headers.
- `--text-content`: Show the text content of the response.
- `--binary-content`: Show the binary content of the response.
- `--json-content`: Show the response content as JSON.
- `--final-url`: Show the final URL after following redirects.
- `--elapsed-time`: Show the elapsed time for the request.
- `--cookies-content`: Show the cookies.
  
For example, to get the status code and headers, use:

```bash
cli_requests https://google.com --status-code --headers-content
```
This code will print stauts code and headers in console.

### Save Response to a File

To save the response content to a file, you can use IO redirection with --nocolor argument or --output-file parameter. For example, to save the response to a file named `output.txt`, use:

```bash
cli_requests https://google.com/ --headers-content --status-code --elapsed-time --nocolor > output.txt
```
OR
```bash
cli_requests https://google.com/ --headers-content --status-code --elapsed-time --output-file output.txt
```

output.txt example

```plaintext

Status Code:
200

Headers:
{'Date': 'Sat, 18 Nov 2023 14:05:29 GMT', 'Expires': '-1', ...}

Elapsed Time:
0:00:00.193750

```

### Sending POST Request with JSON Data

```bash
cli-requests (YOUR URL) --method POST --data '{"key": "value"}'
```
**Issue with Escaping Quotes in Windows Console when Using JSON Objects**

When working with JSON objects in the Windows console, there might be issues due to the required escaping of quotes. You must pass JSON objects like this.

```bash
cli-requests (YOUR URL) --method POST --data '{\"key\": \"value\"}'
```

### Reading Request Configuration from a File

URL is always required, so make sure that you passed it even with configuration file.

```bash
cli-requests (YOUR URL) --load-config path/to/request_config.json
```

### Colorized Output

The output from cli-requests is always presented in color for improved readability. However, for those who prefer a monochromatic display or have specific requirements, there is an optional parameter `--nocolor`. Adding this parameter to the command will disable the colorful output. For example:

```bash
cli-requests https://google.com --status-code --nocolor
```

## Request Configuration

Create a JSON file to define your request configuration. Below is an example for a GET request:

```json
{
  "url": "YOUR URL",
  "method": "GET",
  "params": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Authorization": "Bearer YourAccessToken"
  },
  "timeout": 5000
}
```
### List of parameters

#### Use `-h` | `--help` for help

#### Request parameters

1. `-m` | `--method`: HTTP method (default: GET)
2. `-p` | `--params`: Request parameters (in JSON format)
3. `-f` | `--files`: Files to upload with the request (in JSON format)
4. `-x` | `--proxies`: Proxies for the request (in JSON format)
5. `-d` | `--data`: Data for the request (in JSON format)
6. `-s` | `--headers`: Headers for the request (in JSON format)
7. `-t` | `--timeout`: Timeout for the request (in seconds)
8. `-a` | `--auth`: Authentication credentials (username and password)
9. `-c` | `--cookies`: Cookies for the request (in JSON format)
10. `-v` | `--verify`: Verify SSL certificate (default: True)
11. `-e` | `--cert`: Path to SSL certificate file
12. `-r` | `--allow-redirects`: Allow redirects (default: True)

#### Additional parameters for displaying information:

14. `-S` | `--status-code`: Show the status code
15. `-H` | `--headers-content`: Show the headers
16. `-T` | `--text-content`: Show the text content
17. `-B` | `--binary-content`: Show the binary content
18. `-J` | `--json-content`: Show the JSON content
19. `-U` | `--final-url`: Show the final URL
20. `-E` | `--elapsed-time`: Show the elapsed time
21. `-C` | `--cookies-content`: Show the cookies

#### Additional parameters:

22. `-L` | `--load-config`: Load configuration from a JSON file
23. `-O` | `--output-file`: Save the output to a file

To disable colored output, use `-w` | `--nocolor`.

## Contribution

Feel free to fork the project, make your changes, and submit a pull request.

## License

Cli-Requests is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Sabberian

Sabberian@gmail.com

https://github.com/Sabberian
