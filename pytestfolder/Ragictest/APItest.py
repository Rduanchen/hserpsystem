import requests as req
import json

url="https://ap3.ragic.com/haisann/forms2/1"
header={
    "Authorization":"Basic cEg1bCtoV040TFBzYVA3REs1cGJBUW5mSjUwWm1kOExrRXVWenkzM3R0V0krVGE0UDlkOFpJUXlKSEdsektUUjR2ZXgxV21vSXVjPQ=="
}
# push_data={
#   "1000164":"2022/8/11",
#   "1000135":"2022/10/11 22:00",
#   "1000136":"2022/11/11 13:00",
#   "1000346":"不知道",
#   "1000138":"陳宥端",
#   "1000139":"11",
#   "1000140":"學生自治會",
#   "1000141":"justin94425@gmail.com",
#   "1000142":"justin",
#   "1000146":"api 測試"
# }
param={
    
}
r=req.get(url)
print(r.text)
print(r.status_code)
# b=json.loads(r.text)
# c=0
# name=[]
# num=[]
# for i in b:
#     num.append(b[i]["財產編號"])
#     name.append(b[i]["財產名稱"])
# print(name,num)




