import requests
import time
from functools import wraps


def cache(f):
    saved = {}

    @wraps(f)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in saved:
            return saved[key]
        result = f(*args, **kwargs)
        saved[key] = result
        return result
    return wrapper


def web_lookup(url, cache={}):
    if url in cache:
        return cache[url]
    result = requests.get(url).text
    cache[url] = result
    return result


@cache
def web_lookup2(url):
    return requests.get(url).text


def main():
    start = time.time()
    url = "http://cnn.com"
    web_lookup2(url)
    end = time.time()
    print(f"It took {end-start} seconds")

    start = time.time()
    url = "http://cnn.com"
    web_lookup2(url)
    end = time.time()
    print(f"It took {end-start} seconds")


if __name__ == '__main__':
    main()
