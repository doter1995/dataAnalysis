import time
import random
import logging

def get_random_proxy():
    '''随机从文件中读取proxy'''
    while 1:
        f = open(
            '/Users/wdzhang/sourceCode/dataAnalysis/analysis/meituan_hotel/meituan_hotel/proxies1.txt', 'r')
        proxies = f.readlines()
        if proxies:
            break
        else:
            time.sleep(1)
    proxy = random.choice(proxies).strip()
    logging.info("重新生成ip代理:"+proxy)
    return proxy
