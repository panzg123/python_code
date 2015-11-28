#encoding:utf-8
'''
Created on 2015年11月28日
爬虫去哪儿网站上的机票信息
参考：https://github.com/lining0806/QunarSpider/blob/master/QunarSpider.py
@author: pan

'''

import time
import datetime
import codecs
import multiprocessing as mp
from os import makedirs
from os.path import exists
from selenium import webdriver

site='http://flight.qunar.com'
hot_city_list=[u'上海',u'北京',u'广州',u'深圳']
num=len(hot_city_list)


def one_driver_ticket(driver,from_city,to_city):
    date=datetime.date.today()
    tomorrow=date+datetime.timedelta(days=1)
    #将date格式转化为string格式
    tomorrow_string=tomorrow.strftime('%Y-%m-%d')
    
    driver.find_element_by_name('fromCity').clear()
    driver.find_element_by_name('fromCity').send_keys(from_city)
    driver.find_element_by_name('toCity').clear()
    driver.find_element_by_name('toCity').send_keys(to_city)
    driver.find_element_by_name('fromDate').clear()
    driver.find_element_by_name('fromDate').send_keys(tomorrow_string)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(5) #控制间隔时间，等待浏览器反应
    
    flag=True
    page_num=0
    while flag:
        #保存页面
        #print driver.page_source
        source_code=driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        print type(source_code)
        dstdir=u'./ticket/'
        if not exists(dstdir):
            makedirs(dstdir)
        #新建文件from_city+to_city+日期
        f=codecs.open(dstdir+from_city+u','+to_city+unicode(tomorrow_string)+u','+unicode(str(page_num+1))+u'.html', 'w+', 'utf-8')
        #写入页面信息
        f.write(source_code)
        f.close()
        
        next_page=None
        try:
            next_page=driver.find_element_by_id('nextXI3')
        except Exception as e:
            print e
            pass
        print "page: %d" % (page_num+1)
        if next_page:
            try:
                next_page.click()
                time.sleep(2)
                page_num+=1
            except Exception as e:
                print 'next_page could not be clicked'
                print e
                flag=False
        else:
            flag=False

def ticket_worker(city):
    driver=webdriver.Firefox()
    driver.get(site)
    driver.maximize_window() #将浏览器最大化
    time.sleep(5)
    for i in xrange(num):
        if city==hot_city_list[i]:
            continue
        from_city=city
        to_city=hot_city_list[i]
        one_driver_ticket(driver, from_city, to_city)
    driver.close()

def all_ticket_no_proxy():
    pool = mp.Pool(processes=1)
    pool.map(ticket_worker,hot_city_list)
    pool.close()
    pool.join()

if __name__=='__main__':
    print "start"
    start = datetime.datetime.now()
    # all_ticket_proxy() # proxy
    all_ticket_no_proxy() # no proxy
    end = datetime.datetime.now()
    print "end"
    print "time: ", end-start