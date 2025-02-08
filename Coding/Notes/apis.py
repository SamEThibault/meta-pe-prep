# Syntax notes relating to handling API requests and processing
import requests

res = requests.get("url", headers=None, params=None, timeout=None)
content = res.json()