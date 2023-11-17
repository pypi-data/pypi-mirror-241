import datetime
import hashlib
import logging
import random
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse
from orbitkit.id_srv import get_random_short_id
import os
import csv
from urllib.parse import urlparse


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def get_file_md5(filepath):
    with open(filepath, 'rb+') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_code = md5obj.hexdigest()
        return str(hash_code).upper()


def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    return random.choice(user_agents)


class EasyDownloader:
    def __init__(self, download_urls=None, add_headers=None, concurrent=16, timeout=60, dir_download=''):
        if download_urls is None:
            download_urls = []
        if add_headers is None:
            add_headers = {}

        class MySpider(scrapy.Spider):
            name = 'myspider'
            handle_httpstatus_list = range(100, 600)
            has_ua = True

            custom_settings = {
                'CONCURRENT_REQUESTS': concurrent,
                'CONCURRENT_REQUESTS_PER_DOMAIN': concurrent,
                'DOWNLOAD_TIMEOUT': timeout,
                'LOG_LEVEL': logging.WARNING,
            }

            def start_requests(self):

                start_urls = download_urls
                headers_list = [x.lower() for x in add_headers]
                if 'user-agent' not in headers_list:
                    self.has_ua = False

                logging.warning(f'共 {len(start_urls)} 个文件需要下载...')

                if not dir_download:
                    dir_name = datetime.datetime.now().strftime('sd_%y%m%d_%H%M%S')
                    temp_dir = os.path.join(os.getcwd(), dir_name)
                    if not os.path.exists(temp_dir):
                        os.mkdir(temp_dir)
                    else:
                        raise Exception(f'下载文件夹创建失败！已存在同名文件夹：{dir_name}')
                    download_dir = os.path.join(temp_dir, 'downloads')
                    os.mkdir(download_dir)
                else:
                    dir_name = dir_download
                    temp_dir = os.path.join(os.getcwd(), dir_name)
                    if not os.path.exists(temp_dir):
                        os.mkdir(temp_dir)
                    download_dir = os.path.join(temp_dir, 'downloads')
                    if not os.path.exists(download_dir):
                        os.mkdir(download_dir)

                if os.path.exists(os.path.join(temp_dir, 'meta.csv')):
                    exist_urls = set()
                    with open(os.path.join(temp_dir, 'meta.csv'), 'r') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            exist_urls.add(row[0])
                    start_urls = list(set(start_urls) - exist_urls)
                    logging.warning(f'该文件夹中已存在 {len(exist_urls)} 个文件，仍需下载 {len(start_urls)} 个.')

                for index, url in enumerate(start_urls):
                    if not is_valid_url(url):
                        with open(os.path.join(temp_dir, 'meta.csv'), 'a+') as f:
                            writer = csv.writer(f)
                            writer.writerow([url, 'unknown', 'failed'])
                        continue
                    if not self.has_ua:
                        add_headers['User-Agent'] = get_random_user_agent()
                    logging.warning(f'任务 {index + 1} / {len(start_urls)} 启动.')
                    yield scrapy.Request(url,
                                         headers=add_headers,
                                         meta={'url': url, 'temp_dir': temp_dir, 'download_dir': download_dir},
                                         errback=self.handle_error)

            def parse(self, response: HtmlResponse, **kwargs):

                download_url = response.meta['url']
                temp_dir = response.meta['temp_dir']
                download_dir = response.meta['download_dir']

                if response.status == 200:
                    filename = get_random_short_id() + '_' + response.url.split('/')[-1]
                    file_path = os.path.join(download_dir, filename)
                    with open(file_path, 'wb') as f:
                        f.write(response.body)
                    md5 = get_file_md5(file_path)
                    file_type = filename.split('.')[-1]
                    new_filename = f'{md5}.{file_type}'
                    new_file_path = os.path.join(download_dir, new_filename)
                    os.rename(file_path, new_file_path)

                    with open(os.path.join(temp_dir, 'meta.csv'), 'a+') as f:
                        writer = csv.writer(f)
                        writer.writerow([download_url, new_filename, 'success'])

                    logging.warning(f'Saved file {new_filename}')
                else:
                    with open(os.path.join(temp_dir, 'meta.csv'), 'a+') as f:
                        writer = csv.writer(f)
                        writer.writerow([download_url, 'unknown', 'failed'])

            def handle_error(self, failure):
                fail_url = failure.request.url
                temp_dir = failure.request.meta['temp_dir']
                logging.warning(f'Failed to download {fail_url}')
                with open(os.path.join(temp_dir, 'meta.csv'), 'a+') as f:
                    writer = csv.writer(f)
                    writer.writerow([fail_url, 'unknown', 'failed'])

        self.process = CrawlerProcess()
        self.process.crawl(MySpider)

    def start(self):
        self.process.start()

