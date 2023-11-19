import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI program to make HTTP requests")

    parser.add_argument("url", help="URL for the HTTP request")

    parser.add_argument("-m", "--method", default="GET", help="HTTP method (default: GET)")
    parser.add_argument("-p", "--params", type=json.loads, help="Parameters for the request (JSON format)")
    parser.add_argument("-f", "--files", type=json.loads, help="Files to upload with the request (JSON format)")
    parser.add_argument("-x", "--proxies", type=json.loads, help="Proxies for the request (JSON format)")
    parser.add_argument("-d", "--data", type=json.loads, help="Data for the request (JSON format)")
    parser.add_argument("-s", "--headers", type=json.loads, help="Headers for the request (JSON format)")
    parser.add_argument("-t", "--timeout", type=float, help="Timeout for the request")
    parser.add_argument("-a", "--auth", type=tuple, help="Authentication credentials (username, password)")
    parser.add_argument("-c", "--cookies", type=json.loads, help="Cookies for the request (JSON format)")
    parser.add_argument("-v", "--verify", type=bool, default=True, help="Verify SSL certificate (default: True)")
    parser.add_argument("-e", "--cert", help="Path to SSL certificate file")
    parser.add_argument("-r", "--allow-redirects", type=bool, default=True, help="Allow redirects (default: True)")
    parser.add_argument("-w", "--nocolor", action="store_true", help="Disable colored output")

    parser.add_argument("-S", "--status-code", action="store_true", help="Show the status code")
    parser.add_argument("-H", "--headers-content", action="store_true", help="Show the headers")
    parser.add_argument("-T", "--text-content", action="store_true", help="Show the text content")
    parser.add_argument("-B", "--binary-content", action="store_true", help="Show the binary content")
    parser.add_argument("-J", "--json-content", action="store_true", help="Show the JSON content")
    parser.add_argument("-U", "--final-url", action="store_true", help="Show the final URL")
    parser.add_argument("-E", "--elapsed-time", action="store_true", help="Show the elapsed time")
    parser.add_argument("-C", "--cookies-content", action="store_true", help="Show the cookies")

    parser.add_argument("-L", "--load-config", help="Load configuration from a JSON file")
    parser.add_argument("-O", "--output-file", help="Save the output to a file")

    args = parser.parse_args()

    if args.load_config:
        with open(args.load_config, 'r') as config_file:
            config = json.load(config_file)
            for key, value in config.items():
                setattr(args, key, value)

    return args