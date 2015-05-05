# -*- coding: utf-8 -*-

# Scrapy settings for patent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'patent'

SPIDER_MODULES = ['patent.spiders']
NEWSPIDER_MODULE = 'patent.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'patent (+http://www.yourdomain.com)'
