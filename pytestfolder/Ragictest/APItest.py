import requests as req
import json
url="https://ap3.ragic.com/haisann/forms2/1?api=true"
header={
    "Authorization":"Basic cEg1bCtoV040TFBzYVA3REs1cGJBUW5mSjUwWm1kOExrRXVWenkzM3R0V0krVGE0UDlkOFpJUXlKSEdsektUUjR2ZXgxV21vSXVjPQ=="
}
params={
    "limit": "0,3"
}
r=req.get(url,headers=header,params=params)
print(r.text)
    # data=rep.read().decode()
# print(data)
# print(type(data))
# b=json.loads(data)
# print(b)
# for a in b:
#     print(a)
#     for i in b[a]:
#         print(b[a][i])
