import requests as req
import json
url="https://raw.githubusercontent.com/Rduanchen/hserpsystem.github.io/main/WEB_2/lend_system.html"
r=req.get(url)
print(r.text)