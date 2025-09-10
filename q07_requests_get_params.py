# src/q07_requests_get_params.py
import requests
import json

def main():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": 1}
    resp = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    print("Number of results:", len(data))
    print("\nFirst 2 items:")
    print(json.dumps(data[:2], indent=2))

if __name__ == "__main__":
    main()
