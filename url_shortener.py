#encoding:utf-8
import uuid
import redis

r = redis.Redis(host='localhost',port=6379,db=0)

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
BASE = len(ALPHABET)
#短地址前缀
STATIC_URL="http://yoururl/"

#生成唯一id
def generate_id():
    return uuid.uuid1().int
#编码
def encode(num):
    ret_str=''
    while num:
        index = num % BASE
        ret_str += ALPHABET[index]
        num /= BASE
    return ret_str[::-1]

#解码
def decode(str):
    num=0
    length = len(str)
    index=0
    while index < length:
        num = num*BASE + ALPHABET.index(str[index])
        index += 1
    return num

#获取短url
def url_short(url):
    url_id = generate_id()
    encode_url = encode(url_id)
    r.set(url_id,url)
    return STATIC_URL+encode_url

#返回长url
def url_long(short_url):
    short_url = short_url[-22:]
    url_id = decode(short_url)
    long_url = r.get(url_id)
    return long_url

#example
if __name__ == "__main__":
    url ="http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener"
    url_short_str = url_short(url)
    url_long_str = url_long(url_short_str)
    print url_short_str
    print url_long_str