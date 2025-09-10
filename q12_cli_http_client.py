# src/q12_cli_http_client.py
import sys
import json
import requests

def main(argv):
    if not argv or len(argv) < 2:
        print("Usage: python q12_cli_http_client.py METHOD URL [BODY_JSON]")
        return 1

    method = argv[0].upper()
    url = argv[1]
    body = None
    if method in {"POST", "PUT"}:
        if len(argv) >= 3:
            raw = argv[2]
            try:
                body = json.loads(raw)
            except json.JSONDecodeError:
                print("Invalid JSON body provided.")
                return 2
        else:
            print(f"{method} requires a JSON body as the third argument.")
            return 2

    try:
        if method == "GET":
            resp = requests.get(url, timeout=10)
        elif method == "POST":
            resp = requests.post(url, json=body, timeout=10)
        elif method == "PUT":
            resp = requests.put(url, json=body, timeout=10)
        elif method == "DELETE":
            resp = requests.delete(url, timeout=10)
        else:
            print("Invalid method. Use GET, POST, PUT, DELETE.")
            return 3
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return 4

    print("Status code:", resp.status_code)
    # try JSON else text
    try:
        print("Response JSON:", json.dumps(resp.json(), indent=2))
    except ValueError:
        print("Response text:", resp.text[:1000])
    return 0

if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
