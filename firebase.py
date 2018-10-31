import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import constant

# push
# sales.push({
#     'name': '3ce 립스틱',
#     'url': 'https://search.shopping.naver.com/detail/detail.nhn?nv_mid=12804648154&cat_id=50000391&frm=NVSHMDL&query=&NaPm=ct%3Djmwz6vdc%7Cci%3D2b003e3024fa1a918ef1b431f6f3cdceafc32fbd%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D253e7b00d1ab4680dab951fe67baa41eb224824b'
# })
# sales.push({
#     'name': '샤넬 루쥬 볼립떼',
#     'url': 'https://search.shopping.naver.com/detail/detail.nhn?nv_mid=12804648154&cat_id=50000391&frm=NVSHMDL&query=&NaPm=ct%3Djmwz6vdc%7Cci%3D2b003e3024fa1a918ef1b431f6f3cdceafc32fbd%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D253e7b00d1ab4680dab951fe67baa41eb224824b'
# })

cred = credentials.Certificate(constant.db_api_key)
firebase_admin.initialize_app(cred, {
    'databaseURL': constant.db_adress
})

sales = db.reference(constant.db_ref)

re = sales.get()
print(re)
for i in re:
    print(re[i]['url'])
