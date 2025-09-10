# src/q11_fetch_with_status_handling.py
import requests

def fetch_data(url: str) -> None:
    try:
        resp = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        print(f"Timeout when fetching: {url}")
        return
    except requests.exceptions.ConnectionError:
        print(f"Connection error when fetching: {url}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    code = resp.status_code
    if code == 200:
        print("Success")
    elif 400 <= code <= 499:
        print("Client Error")
    elif 500 <= code <= 599:
        print("Server Error")
    else:
        print(f"Unexpected status code: {code}")

if __name__ == "__main__":
    tests = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/invalid",
        "http://does-not-exist.example"
    ]
    for t in tests:
        print(f"\nFetching: {t}")
        fetch_data(t)
