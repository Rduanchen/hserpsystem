import requests as req
import json

url="https://ap3.ragic.com/haisann/forms2/1?api=true"
header={
    "Authorization":"Basic cEg1bCtoV040TFBzYVA3REs1cGJBUW5mSjUwWm1kOExrRXVWenkzM3R0V0krVGE0UDlkOFpJUXlKSEdsektUUjR2ZXgxV21vSXVjPQ=="
}

param={
    
}
r=req.get(url)
print(r.text)
print(r.status_code)




