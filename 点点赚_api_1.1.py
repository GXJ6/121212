#   --------------------------------注释区--------------------------------
#   入口:https://168750027-1257141735.cos-website.ap-nanjing.myqcloud.com/index.html?pid=16345
#   
#  
#   需抓取数据: 
#   * 填写自动过检的api接口 本地 内网ip:5000 非本地自行进行穿透
#   * 登录多少个账号就跑多少个账号
#
#
#   抓取请求头中的user-agent填入yuanshen_useragent 无论多少个号都只填一个即可!!!!
#
#   变量名:yuanshen_api
#    
#   填支付宝账号#姓名到 yuanshen_ddz_alipay 即可自动提现
withdraw_points = 10000 #提现积分阈值 10000=1r
#   --------------------------------祈求区--------------------------------
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
#   --------------------------------代码区--------------------------------


import requests
import time
import os
import json
import hashlib
import random
import re
import logging
import sys
import string
from base64 import b64encode
import base64
import uuid
from urllib.parse import urlparse, parse_qs,quote
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] ===> %(message)s')
code = "点点赚_api版"
ver = "1.1"
envname = "yuanshen_api" 

debug = False #debug模式 开启即从脚本内部获取环境变量
debugcookie = "127.0.0.1:5000" #debug模式cookie

is_bulletin = True #公告开关
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

from functools import wraps


def retry(exceptions = Exception, tries=5, delay=2, backoff=2):
    """
    简单的重试 module，如果重试失败则抛出错误。
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 每次调用时初始化独立的重试计数和延迟时间
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"发生错误:[{e}], Retrying in {_delay} seconds ...")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            # 最后一次尝试
            return func(*args, **kwargs)
        return wrapper
    return decorator

class yuanshen:
    def __init__(self,cookie,apiurl) -> None:
        self.biz = ['MzA4MjQ5NDMwNg==','MzI2OTA0NzQ5OA==','MzU4OTQ3MDc0Mg==']
        self.apiurl = apiurl
        self.Wxid = cookie['Wxid']
        self.bz = cookie['wxname']
        logging.info(f'[{self.bz}]开始运行')


    def extract_url(self,url):
        # 解析URL
        parsed_url = urlparse(url)
        full_domain = parsed_url.netloc
        query_params = url.split('?')[1]
        

        if not query_params:
            query_params = None
        
        return full_domain, query_params
    
    def push(self):
        url = f"{self.apiurl}/zdgjc"
        data = {"url":self.acturl}
        r = requests.post(url,json=data).json()
        logging.info(f"遇到检测文章:推送结果[{r}]")
        
    @retry()
    def getreadurl(self):
        url = f"http://{self.baseurl}/index/mob/get_read_qr.html"
        r = requests.get(url,headers=self.headers,cookies=self.cookie).json()
        if r['code'] == 1:
            url_pattern = r"http[s]?://[^\s]+"
            urls = re.findall(url_pattern, r['web_url'])
            self.domain,self.readcode = self.extract_url(urls[0])
            if urls:
                logging.info(f"获取到阅读链接: [{self.domain}][{self.readcode}]")
                self.readh = {
    "Host": f"{self.domain}",
    "Connection": "keep-alive",
    "Content-Length": "47",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": ua,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": f"http://{self.domain}",
    "Referer": f"http://{self.domain}/?{self.readcode}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
                return True
            else:
                logging.warning("❌️未获取到阅读链接")
                return False
        else:
            logging.warning(f"❌️未获取到阅读链接[{r}]")
            return False
    @retry()
    def read(self):
        url = f"http://{self.domain}/index/index/get_article.html"
        url2 = f"http://{self.domain}/index/index/auth_record.html"

        while True:
            data = {
            'code': self.readcode,
            'uid':self.uid
        }
            r = requests.post(url,headers=self.readh,data=data,timeout=10).json()
            if r['code'] == 1:
                self.acturl = r["data"]["info"]["link2"]
                rid = int(r['data']['info']['rid'])
                logging.info(f"获取文章成功: [{r['msg']}]")
                if 'addtime' not in r['data']['info']:
                    logging.info("遇到检测文章 推送ing...")
                    self.push()
                    time.sleep(random.randint(18,28))
                else:
                    time.sleep(random.randint(9,18))
            else:
                logging.warning(f"❌️获取文章失败: [{r}]")
                break

            data = {
                'rid': rid,
                'time_is_gou':1
            }
            r = requests.post(url2,headers=self.readh,data=data,timeout=10).json()
            if r['code'] == 1:
                logging.info(f"第[{r['txt']}]篇文章阅读成功")
            else:
                logging.warning(f"❌️阅读文章失败: [{r['msg']}]")
                if '完成' in r['msg']:
                    url = f"http://{self.domain}/index/index/read_result.html"
                    data = {
                        'code':self.readcode
                    }
                    r = requests.post(url,headers=self.readh,data=data,timeout=10).json()
                    if r['code'] == 1:
                        logging.info(f"🔔结束阅读成功: [{r['msg']}]")
                    else:
                        logging.warning(f"❌️结束阅读失败: [{r}]")
                break
    
            time.sleep(random.randint(2,5))
    
    def userinfo(self):
        url = f'http://{self.baseurl}/index/mob/index.html'
        r = requests.get(url,headers=self.headers2,cookies=self.cookie)
        if r.status_code == 200:
            match = re.search(r'(?<=可用积分：)\d+', r.text)
            if match:
                points = int(match.group())
                logging.info(f"🔔当前账号剩余积分:[{points}]=[{points/10000}]元💵")
            else:
                logging.warning("❌️没有获取到积分❌️")
            if points > withdraw_points:
                url = f'http://{self.baseurl}/index/mob/tixian.html'
                r  = requests.get(url,headers=self.headers2,cookies=self.cookie,allow_redirects= False)
                loginurl = r.headers['Location']
                data = {'Wxid':self.Wxid,'url':loginurl}
                url = requests.post(self.apiurl+'/loginbyweb2',json=data).json()['url']
                code = url.split('code=')[1].split('&')[0]
                state = url.split('state=')[1]
                logging.info(f"🔔获取提现链接成功: [{url}]")
                url = f'http://{self.baseurl}/index/mob/fa_tx.html'
                wi_po = int(str(points)[:-3] + '000')
                wi_money = int(points/10000)
                alipays = os.getenv('yuanshen_ddz_alipay')
                if not alipays:
                    logging.warning('没有配置支付宝账号')
                    return
                alipays = alipays.split('#')
                data = {
  "code": code,
  "money": wi_money,
  "kou_credit": wi_po,
  "tx_type": "2",
  "ali_name":alipays[1],
  "ali_account": alipays[0]
}
                r = requests.post(url,headers=self.headers2,data=data,cookies=self.cookie).json()
                logging.info(f'提现结果[{r}]')
            else:
                logging.info('不提现')
                
                
    def login(self):
        
        url = 'http://sx.shuxiangby.cn/index/mob/index?cos=1&pid=16345'
        h = {
  "Host": "sx.shuxiangby.cn",
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.73 Mobile Safari/537.36 XWEB/1300057 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003035) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "X-Requested-With": "com.tencent.mm",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}
        r = requests.get(url,headers=h,allow_redirects= False)
        loginurl = r.headers['Location']
        data = {'Wxid':self.Wxid,'url':loginurl}
        url = requests.post(self.apiurl+'/loginbyweb',json=data).json()['url']#http://sx.shuxiangby.cn/index/mob/auth2.html?cos=1&pid=16345&code=011NZQ1w3OGAO33Ac44w3MxDwL2NZQ1S&state=STATE
        print(url)
        r = requests.get(url,headers=h,allow_redirects= False)
        loginurl = r.headers['Location']#http://41521229395.auth.dianqu33.cn/index/mob/auth.html?cos=1&pid=16345&code=011NZQ1w3OGAO33Ac44w3MxDwL2NZQ1S&state=STATE
        print(loginurl)
        domain = urlparse(loginurl).netloc
        h = {
  "Host": domain,
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.73 Mobile Safari/537.36 XWEB/1300057 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003035) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "X-Requested-With": "com.tencent.mm",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        r = requests.get(loginurl,headers=h,allow_redirects= False)
        self.cookie = r.headers['Set-Cookie']
        self.baseurl = f'{random_11_digits()}.sx.shuxiangby.cn'
        self.uid = self.cookie.split('uid=')[1].split(';')[0]
        user_openid = self.cookie.split('user_openid=')[1].split(';')[0]
        PHPSESSID = self.cookie.split('PHPSESSID=')[1].split(';')[0]
        self.cookie = {'uid':self.uid,'user_openid':user_openid,'PHPSESSID':PHPSESSID}
        logging.info('登录成功')
        self.headers = {
    "Host": self.baseurl,
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": ua,
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"http://{self.baseurl}/index/mob/index.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
    
        self.headers2 = {
    "Host": self.baseurl,
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": ua,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "com.tencent.mm",
    "Referer": f"http://{self.baseurl}/index/mob/mine.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        
        

             
    
    def main(self):
        try:
            self.login()
            if self.getreadurl():
                print("="*30)
                time.sleep(random.randint(3,5))
                self.read()
            time.sleep(random.randint(3,5))
            print("="*30)
            self.userinfo()
        except Exception as e:
            logging.error(f'发生错误：{e}')




def random_11_digits():
    first_digit = random.randint(1, 9)
    num = str(first_digit)
    for i in range(10):
        num += str(random.randint(0, 9))
    return num


if __name__ == '__main__':
    ua = os.getenv('yuanshen_useragent')
    #ua = 'Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240301 MMWEBID/4020 MicroMessenger/8.0.48.2580(0x28003035) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64'
    if not ua:
        logging.info("❌你还没有设置user_agent,请设置环境变量:yuanshen_useragent")
        exit()

    env().main()