# src/q06_requests_get.py
import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    print("Response JSON:")
    print(data)
    print("\nTitle field:", data.get("title"))

if __name__ == "__main__":
    main()
