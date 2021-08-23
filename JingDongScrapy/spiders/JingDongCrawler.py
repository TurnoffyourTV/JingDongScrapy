import scrapy
from scrapy.spiders import CrawlSpider
import re
import json
from ..items import JingdongscrapyItem


class PictureCrawler(CrawlSpider):
    name = 'PictureCrawler'
    allowed_domains = ['search.jd.com', '360buyimg.com']

    def __init__(self):
        self.query_list = ['铁锅', '勺子']
        self.url = "https://search.jd.com/Search?keyword={0}"
        self.search_header = {
            'authority': 'search.jd.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.jd.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': 'shshshfpb=shxO3D2Pdx1fxh3pn32BtOA%3D%3D; shshshfpa=7c8502d2-0075-bdd2-f31e-4941005ebd7a-1593842200; TrackID=13qWK-gk5VR-H_lom-EF8vZNa880899XWMLGbUMl9R3NYGGMa7UUQFxPNY2hdCbJD0nxRkiaWIvu4u8PHRzxLbDx7xZjKfV5iE7xTq5g_hSA; pinId=Ro7LRx1jaqfH2iniQChXULV9-x-f3wj7; qrsc=3; areaId=12; ipLoc-djd=12-984-53562-0; PCSYCityID=CN_320000_320200_320213; rkv=1.0; __jdv=122270672|google|hkbsc10|cpc|not set|1629377617013; user-key=d15965f3-8070-40fe-962e-d8f4f2099b8a; __jda=122270672.1624846887632477341012.1624846888.1629373948.1629373995.7; __jdb=122270672.31.1624846887632477341012|7.1629373995; __jdc=122270672; shshshfp=41a7590ec2f565bd4aa46353e274f639; shshshsID=9b328a5eb9b9988bff04437523a3a4fd_31_1629377642142; 3AB9D23F7A4B3C9B=5RR7MK52U2ZXTPZKFPDTX4MQQ35FRLDG6K2D6MEMWK5D2UQQ5K5ZRHKR4YJYUKYZXIPMIKDA6SGQJZBYBNYWITHBJY',

        }
        self.comment_headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': 'https://item.jd.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        }
        self.comment_cookies = {
            'shshshfpb': 'shxO3D2Pdx1fxh3pn32BtOA%3D%3D',
            'shshshfpa': '7c8502d2-0075-bdd2-f31e-4941005ebd7a-1593842200',
            'TrackID': '13qWK-gk5VR-H_lom-EF8vZNa880899XWMLGbUMl9R3NYGGMa7UUQFxPNY2hdCbJD0nxRkiaWIvu4u8PHRzxLbDx7xZjKfV5iE7xTq5g_hSA',
            'pinId': 'Ro7LRx1jaqfH2iniQChXULV9-x-f3wj7',
            '__jdv': '122270672|google|kwhkccf03|cpc|not set|1629338241349',
            '__jdc': '122270672',
            'areaId': '12',
            'ipLoc-djd': '12-984-53562-0',
            'shshshfp': '85e60b6790c19b7729a69e5805f608aa',
            'jwotest_product': '99',
            '__jda': '122270672.1624846887632477341012.1624846888.1629338241.1629341351.5',
            '3AB9D23F7A4B3C9B': '5RR7MK52U2ZXTPZKFPDTX4MQQ35FRLDG6K2D6MEMWK5D2UQQ5K5ZRHKR4YJYUKYZXIPMIKDA6SGQJZBYBNYWITHBJY',
            'JSESSIONID': '95ABA0BA95D13079B710E028246546AC.s1',

        }
        self.picture_headers = {
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
        self.goods_num_re = re.compile('\d+')

    def start_requests(self):
        """
        Use the landing page to get cookies first
        """
        keyword_list = ['西瓜']
        request_list = []
        for keyword in keyword_list:
            url = self.url.format(keyword)
            url_request = scrapy.Request(url=url, headers=self.search_header, callback=self.parse_search_page,
                                         meta={"dont_merge_cookies": True, "category": keyword})
            request_list.append(url_request)
        return request_list

    def parse_search_page(self, response):
        url_lists = response.xpath(
            "//div[@id='J_goodsList']/ul/li/div/div[@class='p-name p-name-type-2']/a/@href").extract()

        for url in url_lists:
            goods_num = self.goods_num_re.search(url).group(0)
            # for page_index in range(1, 26):

            goods_comment_url = "https://club.jd.com/discussion/getProductPageImageCommentList.action?productId={0}&page=1&pageSize=20".format(
                goods_num)
            category = response.meta['category']
            yield scrapy.Request(url=goods_comment_url, headers=self.comment_headers, cookies=self.comment_cookies,
                                 callback=self.parse_comment_page, dont_filter=True, meta={'category': category})

    def parse_comment_page(self, response):
        data = json.loads(response.text)
        picture_entry_lists = data['imgComments']['imgList']
        for picture_entry in picture_entry_lists:
            image = JingdongscrapyItem()
            image['image_url'] = "https:" + picture_entry['imageUrl']
            image['image_category'] = response.meta['category']
            yield image
            # picture_url=picture_entry['imageUrl']
            # picture_id = picture_entry['Id']
