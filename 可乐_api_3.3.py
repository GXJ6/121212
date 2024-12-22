#   --------------------------------注释区--------------------------------
#   入口:微信打开 http://280766611011953.av9j2ff3w1.cn/r?bwr=dim&jcz=l2g&pla=pjr&t5n=xfz&upuid=2807666&zrb=av8
#   走个头谢谢 不然没更新动力了呜呜呜
#
#   需抓取数据: 
#   * 填写自动过检的api接口 本地 内网ip:5000 非本地自行进行穿透
#   * 登录多少个账号就跑多少个账号
#
#
#   变量名:yuanshen_api
withdrawal_money = 3000 # 提现金币数量 1000金币=0.1r
Quantity_limit = 180  # 阅读上限篇数 跑满(195篇左右)概率封号
fuck_list = [1,2,126] # 强制识别为检测文章并推送篇数 不懂默认 需要新加的话在后面用 英文逗号加篇数 新增自定义参数就行 
max_threads = 1 #运行线程数 不懂默认
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
import requests
import string
import uuid
from base64 import b64encode
import time
import os
from urllib.parse import urlparse, parse_qs,quote
import re
import random
import math
import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] ===> %(message)s')
code = "可乐阅读_api版"
ver = "3.3"
envname = "yuanshen_api"
debug = False #debug模式 开启即从脚本内部获取环境变量
debugcookie = "127.0.0.1:5000"
is_bulletin = False #公告开关
is_toulu = False #偷撸公告开关
is_with_sleep = False #是否开启随机延时

class env():
    """
    env模块,获取cookie并转成列表,统计时间,提示脚本开始结束,检测一些配置,try except异常处理
    :param args: 传递给env的参数
    :param kwargs: 传递给env的关键字参数
    :return: Null

    Powered by huaji
    """
    def __init__(self, *args, **kwargs):
        self.cookie = None
        self.env_ver = '1.5' #版本号
        self.split_chars = ['@', '&', '\n'] #分隔符
        self.identifiers = ['Powered By Huaji', 'QQ Group:901898186', 'yuanshen'] #标识符
    def check_file(self):
        file_path = __file__
        try:

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            results = {}
            
            # 批量检查每个标识符
            for identifier in self.identifiers:
                if identifier in content:
                    results[identifier] = True
                else:
                    results[identifier] = False
                    logging.error(f"文件可能被恶意篡改,请勿修改文件内容")

            all_identifiers_present = all(results.values())
            if not all_identifiers_present:
                logging.error(f"文件可能被恶意篡改,请勿修改文件内容")
                self.force_exit()
        
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
            self.force_exit()

    def split_cookies(self):
        """根据多个分隔符分割cookie"""
        for sep in self.split_chars:
            if sep in self.cookie:
                return self.cookie.split(sep)
        return [self.cookie]
    
    def scmain(self):
        if 'https://' not in self.cookie and 'http://' not in self.cookie:
            apiurl = 'http://' + self.cookies[0]
        r = requests.get(apiurl + '/getallwx').json()
        for i, cookie in enumerate(r, 1):
            print(f"--------开始第{i}个账号--------")
            main = yuanshen(cookie,apiurl)
            main.main()
            print(f"--------第{i}个账号执行完毕--------")



    def force_exit(self,code=0):
        exit()
        print("Warning: 篡改你妈")
        os._exit(code)  # 强制退出程序
        sys.exit(code)  # 正常退出
        import ctypes
        while True:
            ctypes.string_at(114514)
            ctypes.string_at(1919810)
            ctypes.string_at(666666)
            print("Warning: 篡改你妈")
        

    def run(self):
        if not os.getenv(envname) and not debug:
            logging.warning(f"请先设置环境变量[{envname}]")
            self.force_exit()

        self.cookie = os.getenv(envname, "")

        if debug:
            self.cookie = debugcookie
        if is_bulletin:
            try:
                print(requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text, "\n\n\n")
            except:
                logging.error("网络异常,链接公告服务器失败(gitee)，请检查网络")
                self.force_exit()
        if is_toulu:
            try:
                txt = '''
此为滑稽的偷撸本本 如你不在滑稽的小群却意外通过某种渠道获得了该脚本
请联系QQ3487934983 提供证据后 你将代替泄露人员获得该群位置
=======================================================
        '''
                print(txt*5)
            except:
                self.force_exit()
        if is_with_sleep:
            random_time = random.randint(10,60)
            logging.info(f"随机延时[{random_time}]秒")
            time.sleep(random_time)

        self.cookies = self.split_cookies()
        account_count = len(self.cookies)
        logging.info(f"一共获取到{account_count}个账号")
        print(f"=========🔔开始执行[{code}][{ver}]=========\n")
    
    
        start_time = time.time()
        if debug:
            self.scmain()
        else:
            try:
                self.scmain()
            except Exception as e:
                logging.error(f"脚本执行出错: {e}")
        end_time = time.time()

        execution_time = end_time - start_time

        print(f"\n============🔔脚本[{code}]执行结束============")
        print(f"本次脚本总运行时间: [{execution_time:.2f}] 秒")
        self.force_exit()

    def main(self):
        self.check_file()
        self.run()

    def random_str(self,charset="all", length=8, to_upper=False,to_lower=False):
        if charset == "all": #包含大小写字母和数字
            chars = string.ascii_letters + string.digits  
        elif charset == "letters": #大小写字母
            chars = string.ascii_letters
        elif charset == "digits":
            chars = string.digits
        elif charset == "lowercase": #小写字母
            chars = string.ascii_lowercase  
        elif charset == "uuid":
            return str(uuid.uuid4())
        elif charset == "uuid_str":
            return str(uuid.uuid4()).replace("-", "")
        elif charset != '' and charset is not None:
            chars = charset


        random_string = ''.join(random.choice(chars) for _ in range(length))

        if to_upper:
            return random_string.upper()
        elif to_lower:
            return random_string.lower()
        else:
            return random_string
    
    def aes_encrypt(self,data):
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad, unpad
        from binascii import hexlify, unhexlify
        key = self.key.encode('utf-8')
        iv = self.iv.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = pad(data.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        encrypted_base64 = b64encode(ciphertext).decode('utf-8')

        return encrypted_base64

class yuanshen:
    def __init__(self,cookie,apiurl) -> None:
        self.apiurl = apiurl
        self.Wxid = cookie['Wxid']
        self.bz = cookie['wxname']
        logging.info(f'[{self.bz}]开始运行')
        self.is_wx = True
        self.is_zfb = False
        self.fuck_list = fuck_list
        self.biz_list = ['MzkwNTY1MzYxOQ==','MzA3NzMzNjMwMQ==']

    
    def tuisong(self):
        # 发送消息到wxpusher
        url = f"{self.apiurl}/zdgjc"
        data = {"url":self.readurl}
        r = requests.post(url,json=data).json()
        logging.info(f"遇到检测文章:推送结果[{r}]")

    def getmain(self):
        headers = {
  "Host": "280766611061943.uvmlg2qxl.cn",
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": user_agent,
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "X-Requested-With": "com.tencent.mm",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        
        url = 'http://280766611061943.uvmlg2qxl.cn/r?fne=232&g7g=s0w&lgn=ll7&upuid=2807666&wxl=zy8&x7f=76e'
        r = requests.get(url,headers=headers,allow_redirects=False)
        if r.status_code == 302:
            j = urlparse(r.headers['Location'])
            self.mainurl = j.netloc
            logging.info(f"获取主域名成功:[{self.mainurl}]")
            self.headers = {
    'User-Agent': user_agent,
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    'X-Requested-With': 'XMLHttpRequest',
    'udtauth12': self.cookie,
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Origin': f'http://{self.mainurl}',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': f'http://{self.mainurl}/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}


            self.mainurl = 'm.zzyi4cf7z8.cn'
        else:
            logging.error('获取主域名失败')
            return False
        return True

    def getdomain(self):
        url = f'http://{self.mainurl}/tuijian?url='
        r = requests.get(url,headers=self.headers).json()
        if r['code'] == 0:
            self.today_num = int(r["data"]["infoView"]["num"])
            try:
                logging.info(r["data"]["infoView"]["msg"])
                return False
            except:
                pass
        
        time.sleep(3)
        url = 'https://m.zzyi4cf7z8.cn/new/bbbbb'
        try:
            r = requests.get(url,headers=self.headers)
            print(r.text)
            self.domain =  r.json()['jump']
        except:
            logging.error('获取域名失败 原因为ck失效或遭封了')
            return False
        j = urlparse(self.domain)
        p = parse_qs(self.domain.split('?')[1])
        self.iu = p.get('iu', [None])[0]
        self.domain_url = j.netloc
        logging.info(f"获取域名成功:[{self.domain_url}][{self.iu}]")
        time.sleep(2)
        h = {
"Host": self.domain_url,
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": user_agent,
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"X-Requested-With": "com.tencent.mm",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}       

        r = requests.get(self.domain,headers=h,allow_redirects=False)
        # print(r.text)
        # match = re.search(r"var url = '(.*)'", r.text)
        
        self.is_read_a = False
        self.is_read_b = False
        


        match = re.search(r"var url = '(.*)'", r.text)
        if match:
            self.canshu = match.group(1)
            self.is_read_a = True
            logging.info(f"取阅读参数A成功[{self.canshu}]")
            self.readh2 = {
    'User-Agent': user_agent,
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Origin': f'http://{self.domain_url}',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': f'http://{self.domain_url}/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
            return True
        else:
            logging.error("取阅读参数A失败")
            
        if match:
            match = re.search(r"var dr_url = '(.*)'", r.text)
            self.canshu = match.group(1)
            self.is_read_b = True
            logging.info(f"取阅读参数B成功[{self.canshu}]")
            self.readh2 = {
    "Host": "m.zzyi4cf7z8.cn",
    "Connection": "keep-alive",
    "sec-ch-ua": "Chromium;v=122, Not(A:Brand;v=24, Android",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": user_agent,
    "sec-ch-ua-platform": "Android",
    "Accept": "*/*",
    "Origin": f"http://{self.domain_url}",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": f"http://{self.domain_url}/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
            return True
        else:
            logging.error("取阅读参数B失败")

        return False

        

    
    def read(self):


        logging.info(f"今日已读:[{self.today_num}]篇文章")
        jkey = None
        time.sleep(random.randint(2,5))
        while True:
            if self.today_num >= Quantity_limit:
                logging.info(f"今日已读数量已达设置上限")
                return
            self.today_num += 1
            r = random.random()
            if jkey is None:
                if self.is_read_a:
                    url = f"{self.canshu}?iu={self.iu}&pageshow&r={r}"
                elif self.is_read_b:
                    url = f"http://{self.domain_url}{self.canshu}?iu={self.iu}&t={r}"
            else:
                if self.is_read_a:
                    url = f"{self.canshu}?iu={self.iu}&pageshow&r={r}&jkey={jkey}"
                elif self.is_read_b:
                    url = f"http://{self.domain_url}{self.canshu}?iu={self.iu}&t={r}&jkey={jkey}"
                
            r = requests.get(url,headers=self.readh2).json()
            try:
                jkey = r["jkey"]
                self.readurl = r['url']
                if r['url'] is None or r['url'] == 'close':
                    logging.error(f"未返回有效文章url")
                    return
            except:
                logging.error(f"获取文章链接失败[{r}]")
                break
            
            logging.info(f"第[{self.today_num}]次获取文章成功:[{r['url']}]")
            k = urlparse(self.readurl)
            biz = parse_qs(k.query).get('__biz', [''])[0] if '__biz' in parse_qs(k.query) else ''
            if biz in self.biz_list or self.today_num in self.fuck_list:
                print('遇到检测文章，推送ing....')
                self.tuisong()
                time.sleep(random.randint(20,26))
            else:
                time.sleep(random.randint(8,18))

    def userinfo(self):
        url = f'http://{self.mainurl}/tuijian?url='
        r = requests.get(url,headers=self.headers).json()
        if r['code'] == 0:
            gold = float(r['data']['user']['score']) * 100
            logging.info(f'今日已赚金币:[{float(r["data"]["infoView"]["score"])*100}]')
            logging.info(f'当前账号剩余金币:[{gold}] = [{gold/10000}]元')
            if gold >= withdrawal_money:
                self.withdrawal()
            else:
                logging.info(f"金币余额不足[{withdrawal_money}] 不提现")
        else:
            logging.error(f"查询个人余额失败:[{r}]")

    def withdrawal(self):
        url = f'http://{self.mainurl}/withdrawal'
        r = requests.get(url,headers=self.headers).json()
        if r['code'] == 0:
            score = math.floor(float(r['data']['user']['score']))
            if self.is_wx:
                data = {'amount':score,'type':'wx'}
            elif self.is_zfb:
                data = {'amount':score,'type':'ali','u_ali_account':self.alipay,'u_ali_real_name':self.alipayname}

            url = f'http://{self.mainurl}/withdrawal/doWithdraw'
            r = requests.post(url,data=data,headers=self.headers)
            logging.info(f"提现结果:[{r.text}]")

    def login(self):
        h = {
  "Host": "m.zzyi4cf7z8.cn",
  "Connection": "keep-alive",
  "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
  "Accept": "application/json, text/plain, */*",
  "X-Requested-With": "XMLHttpRequest",
  #"udtauth12": "63e2zZogVUJV9DUya0ouQk9gXzSkwqy3tTNF2ycNMdf%2FyF5NfTVX5W7HfbxNSakX%2B7YCKBhq8lIxMS9G33sE%2B93v4bxUECwyk9J%2F4bAe0dJ1HYUtWvJoqAwRvpJmklIxajBH1HFpagDaIu0OtSAllTtyDhYlCAwpF5FGxeVTwcw",
  "sec-ch-ua-mobile": "?1",
  "User-Agent": user_agent,
  "sec-ch-ua-platform": "\"Android\"",
  "Origin": "http://klluodi-06.eos-ningbo-1.cmecloud.cn",
  "Sec-Fetch-Site": "cross-site",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "http://klluodi-06.eos-ningbo-1.cmecloud.cn/",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        url = f'https://m.zzyi4cf7z8.cn/tuijian?url=fne%3D232%26g7g%3Ds0w%26lgn%3Dll7%26upuid%3D2807666%26wxl%3Dzy8%26x7f%3D76e%26t%3D1730983021&upuid=2807666'
        r = requests.get(url,headers=h).json()
        loginurl = r['url']
        data = {'Wxid':self.Wxid,'url':loginurl}
        url = requests.post(self.apiurl+'/loginbyweb',json=data).json()['url']
        code = url.split('&code=')[1].split('&')[0]
        print(code)
        url = f'https://m.zzyi4cf7z8.cn/user/login3?code={code}'
        r = requests.get(url,headers=h,allow_redirects=False)
        self.cookie = r.headers['Set-Cookie'].split('udtauth12=')[1].split(';')[0]
        print(self.cookie)
        
    def main(self):
        try:
            self.login()
            if not self.getmain():
                return
            time.sleep(random.randint(2,5))
            if self.getdomain():
                print("="*30)
                self.read()

            print("="*30)
            self.userinfo()
        except Exception as e:
            logging.error(f"发生错误:{e}")




if __name__ == '__main__':
    user_agent = os.getenv('yuanshen_useragent')
    #user_agent = '63e2zZogVUJV9DUya0ouQk9gXzSkwqy3tTNF2ycNMdf%2FyF5NfTVX5W7HfbxNSakX%2B7YCKBhq8lIxMS9G33sE%2B93v4bxUECwyk9J%2F4bAe0dJ1HYUtWvJoqAwRvpJmklIxajBH1HFpagDaIu0OtSAllTtyDhYlCAwpF5FGxeVTwcw'
    if not user_agent:
        logging.error("❌你还没有设置user_agent,请设置环境变量:yuanshen_useragent")
        exit()
    env().main()
