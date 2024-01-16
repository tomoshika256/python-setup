import time
import requests
import api_post

for num in range(10):
    time.sleep(0.5)
    api_post.api_post()
    