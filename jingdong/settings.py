# -*- coding: utf-8 -*-

# Scrapy settings for tianyancha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jingdong'

SPIDER_MODULES = ['jingdong.spiders']
NEWSPIDER_MODULE = 'jingdong.spiders'



DOWNLOADER_MIDDLEWARES = {
    # 'jingdong.middlewares.ProxyMiddleware': 100,#代理中间件
    'jingdong.middlewares.RotateUserAgentMiddleware': 200,#请求头中间件
    # 'jingdong.middlewares.JavaScriptMiddleware': 543,  # 键为中间件类的路径，值为中间件的顺序
    # 'scrapy_crawlera.CrawleraMiddleware': 600,  # crawlera代理用到
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 禁止内置的中间件
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': "http://" + CRAWLERA_USER + ":" + CRAWLERA_PASS + "@proxy.crawlera.com:8010/",
}

# CRAWLERA_ENABLED = True
# CRAWLERA_APIKEY = '8293dc6c926d49c6bd3fe6f89549733c'
# CRAWLERA_USER = '775618369@qq.com'
# CRAWLERA_PASS = '3646287'

#禁用cookies
COOKIES_ENABLED=False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#302 Problem
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3  # 间隔时间,两次下载的间隔
RANDOMIZE_DOWNLOAD_DELAY = True  # 开启随机延迟
# CRAWLERA_PRESERVE_DELAY = True

DEFAULT_REQUEST_HEADERS = {
    'Host': 'book.jd.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'http://book.jd.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

USER_AGENT_CHOICES = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
]

LOG_STDOUT = True

LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    'jingdong.pipelines.MongodbPipeline': 800,
    'jingdong.pipelines.DuplicatesPipeline': 700,

}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'jd'
MONGODB_COLECNAME = 'url'

# PROXIES = [
#     {'ip_port': '92.222.146.67:9999','user_pass':''},
#     {'ip_port': '111.13.7.122:80','user_pass':''},
# ]

DOWNLOAD_TIMEOUT = 240
RETRY_TIMES = 10