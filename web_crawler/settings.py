# Scrapy settings for web_scawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "hhh"

SPIDER_MODULES = ["web_scawler.spiders"]
NEWSPIDER_MODULE = "web_scawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "web_scawler (+http://www.yourdomain.com)"
# settings.py
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
   "Accept-Encoding":"gzip, deflate, br, zstd",
   "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
   "Cookie": "PHPSESSID=8lcubl8qoh43r8ffpja9g81arv; __cf_bm=Yxz6u_gulgDIPh9khAXAjZd55d2ECKDfjd6lYxkvoYk-1723626858-1.0.1.1-LF4h3bjPyCvR5MkhL5gFWndNLlF5nhVRcgfZQDxmF5MQOtbXsrp0s43FwRWESbeJRZFmrf4UgohNlTJ7lBm.jg; cf_clearance=.6O2tfaKIyIHtIrwKhV5YVGSKwgY1dCdPBIOZ8PWS0A-1723626859-1.0.1.1-sitdWU8XTBMK7Ywruc.x4lxVfuEIEql4uzsRSs_VaUiO64RtEp0l8IgRlxH8m1A1s0mnGLmtdq6WFhIu8ecdnA; __PPU_tuid=7402920989914575242; __PPU_ppucnt=1; UGVyc2lzdFN0b3JhZ2U=%7B%22CAIFRQ%22%3A%22ACZLEAAAAAAAAAAE%22%2C%22CAIFRT%22%3A%22ACZLEAAAAABmvOKQ%22%7D",
   "Priority":"u=0, i",
   "Referer":"https://doujindesu.tv/",
   "Sec-Ch-Ua":'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
   "Sec-Ch-Ua-Mobile":'?0',
   "Sec-Ch-Ua-Platform":'Windows',
   "Sec-Fetch-Dest" : 'document',
   "Sec-Fetch-Mode" : 'navigate',
   "Sec-Fetch-Site" : 'same-origin',
   "Sec-Fetch-User":'?1',
   "Upgrade-Insecure-Requests": "1",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "web_scawler.middlewares.WebScawlerSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "web_scawler.middlewares.WebScawlerDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "web_scawler.pipelines.WebScawlerPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
