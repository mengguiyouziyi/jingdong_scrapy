# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from random import choice
from scrapy import signals
from scrapy.exceptions import NotConfigured
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import os
# from selenium.webdriver.common.action_chains import ActionChains

class ProxyMiddleware(object):
    def __init__(self):
        # 代理服务器
        self.proxyServer = "http://proxy.abuyun.com:9020"
        # 代理隧道验证信息
        self.proxyUser = "H12BV7ZU2B66580D"
        self.proxyPass = "BF95270ABBEE5BF3"
        # for Python3
        self.proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((self.proxyUser + ":" + self.proxyPass), "ascii")).decode("utf8")

    def process_request(self, request, spider):
        request.meta["proxy"] = self.proxyServer
        request.headers["Proxy-Authorization"] = self.proxyAuth

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "jd_detail":
            print("PhantomJS is starting...")
            driver = webdriver.PhantomJS()  # 指定使用的浏览器
            driver.get(request.url)
            # driver = webdriver.Firefox()
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=20000"
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(10)

            data_opens = driver.find_elements_by_xpath('//a[@data-open]')
            for data_open in data_opens:
                print('展开更多前')
                data_open.click
                print('展开更多后')
                # print('显示更多+++++++++++++++++++', data_open.str)
            time.sleep(1)

            body = driver.page_source
            # print("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        elif spider.name == 'get_company':
            print("PhantomJS is starting...")
            driver = webdriver.PhantomJS()  # 指定使用的浏览器
            driver.get(request.url)
            try:
                element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.col-xs-10.search_repadding2.f18')))
            except Exception as e:
                print('没有找到元素或发生其他异常:' + e)
                pass
            finally:
                # print(driver.find_element_by_xpath('//a[@class="query_name search-new-color"]/@href').text())
                # driver.close()
                body = driver.page_source
                # print("访问" + request.url)
                return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)


class RotateUserAgentMiddleware(object):
    """Middleware used for rotating user-agent for each request"""
    def __init__(self, user_agents):
        self.enabled = False
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        """Get user agents from settings.py"""
        user_agents = crawler.settings.get('USER_AGENT_CHOICES', [])
        if not user_agents:
            raise NotConfigured("USER_AGENT_CHOICES not set or empty")
        ret = cls(user_agents)
        crawler.signals.connect(ret.spider_opened, signal=signals.spider_opened)
        return ret

    def spider_opened(self, spider):
        self.enabled = getattr(spider, 'rotate_user_agent', self.enabled)

    def process_request(self, request, spider):
        """Select user agent randomly on request"""
        if self.enabled and self.user_agents:
            request.headers['user-agent'] = choice(self.user_agents)




# class ProxyMiddleware(object):
#     def __init__(self):
#         self.proxys = []
#         ip_path = os.path.join(os.getcwd(), 'ip_list.txt')
#         with codecs.open(ip_path, 'r', 'utf-8') as f:
#             self.ip_list = f.readlines()
#             for ip in self.ip_list:
#                 self.proxy = {'ip_port': str(ip).strip(),'user_pass':b''}
#                 # print(self.proxy)
#                 self.proxys.append(self.proxy)
#
#     def process_request(self, request, spider):
#         self.proxy = random.choice(self.proxys)
#         if self.proxy['user_pass'] is not None:
#             request.meta['proxy'] = "http://%s" % self.proxy['ip_port']
#             request.meta['proxy'] = "https://%s" % self.proxy['ip_port']
#             encoded_user_pass = base64.b64encode(self.proxy['user_pass'])
#             request.headers['Proxy-Authorization'] = b'Basic ' + encoded_user_pass
#             print("**************ProxyMiddleware have pass************" + self.proxy['ip_port'])
#         else:
#             print("**************ProxyMiddleware no pass************" + self.proxy['ip_port'])
#             request.meta['proxy'] = "http://%s" % self.proxy['ip_port']
#
#     def process_response(self, request, response, spider):
#         response_status = response.status
#         request_url = request.url
#         if response_status == 200:
#             print(self.proxy['ip_port'] + '：代理ip正常················')
#             return response
#         else:
#             print(self.proxy['ip_port'] + '：代理ip不能用了··············')
#             self.proxys.pop(self.proxy)
#             self.process_request(self, request.replace(url=request_url), spider)

