# import requests as req
# import json
# url="https://raw.githubusercontent.com/Rduanchen/hserpsystem.github.io/main/WEB_2/lend_system.html"
# r=req.get(url)
# print(r.text)
import json
# from multiprocessing.resource_sharer import stop
# from time import time
# from tracemalloc import start

json_sample="""
{
    'key1':'value'
    'key2':'value
}
"""
a=json.loads(json_sample)
print(type(a))