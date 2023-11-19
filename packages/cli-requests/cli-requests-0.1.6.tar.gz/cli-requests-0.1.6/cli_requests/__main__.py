from requester import Requester
from .argparser import parse_arguments
from .colorizer import colorize_info

def main():
    args = parse_arguments()

    requester = Requester()

    response = requester.request(
        url=args.url,
        method=args.method,
        params=args.params,
        files=args.files,
        proxies=args.proxies,
        data=args.data,
        headers=args.headers,
        timeout=args.timeout,
        auth=args.auth,
        cookies=args.cookies,
        verify=args.verify,
        cert=args.cert,
        allow_redirects=args.allow_redirects,
        nocolor=args.nocolor,
    )

    output_data = []

    if args.status_code:
        output_data.append(("Status Code", response.status_code))

    if args.headers_content:
        output_data.append(("Headers", response.headers))

    if args.text_content:
        output_data.append(("Text Content", response.text))

    if args.binary_content:
        output_data.append(("Binary Content", response.content))

    if args.json_content:
        try:
            json_data = response.json()
            output_data.append(("JSON Content", json_data))
        except ValueError:
            output_data.append(("JSON Content", "Response content is not in JSON format."))

    if args.final_url:
        output_data.append(("Final URL", response.url))

    if args.elapsed_time:
        output_data.append(("Elapsed Time", response.elapsed))

    if args.cookies_content:
        output_data.append(("Cookies", response.cookies))

    nocolor = args.nocolor
    
    if args.output_file:
        with open(args.output_file, 'w') as output_file:
            for item in output_data:
                output_file.write(f"{item[0]}:\n{item[1]}\n\n")
    else:
        for item in output_data:
            print(f"{colorize_info(item[0]) if not nocolor else item[0]}:\n{item[1]}\n")