import threading
import requests
import random
import queue
import time


def fetch(url, q, t):
    response = requests.get(url)
    time.sleep(t)
    q.put(f"Fetched data from {url} with status {response.status_code} | sleeping: {t}")

def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    q = queue.Queue()

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch, args=(url, q, random.randint(1, 5)))
        threads.append(thread)
        thread.start()

    # for thread in threads:
    #     thread.join()

    k = 0
    while k != len(urls):
        print(k, q.get())
        k += 1

if __name__ == "__main__":
    main()
