import requests
import time

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def do_something_slow(data):
    time.sleep(5)
    return "did something slow with: {}".format(data)
