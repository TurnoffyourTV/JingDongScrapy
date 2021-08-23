# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import settings
import os


class JingdongscrapyPipeline:
    def process_item(self, item, spider):
        return item


class JingdongImgDownloadPipeline(ImagesPipeline):
    headers = {
        'authority': 'img30.360buyimg.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        # 'if-modified-since': 'Thu, 19 Aug 2021 07:00:36 GMT',
    }

    def get_media_requests(self, item, info):
        self.headers['referer'] = item['image_url']
        yield Request(item['image_url'], headers=self.headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item

    def file_path(self, request, item,response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path=super(JingdongImgDownloadPipeline, self).file_path(request,response,info)
        category=item['image_category']
        # image_store=settings.IMAGES_STORE
        category_path=os.path.join(category)
        # if not os.path.exists(category_path):
        #     os.makedirs(category_path)
        image_name=path.replace("full/","")
        image_path=os.path.join(category_path,image_name)
        return image_path
