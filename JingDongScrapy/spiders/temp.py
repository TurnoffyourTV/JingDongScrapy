import requests
from lxml import etree
headers = {
    'authority': 'search.jd.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://search.jd.com/Search?keyword=%E8%8D%89%E8%8E%93&enc=utf-8&pvid=a90da01e31a84a1ca62d0c1172099bc7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cookie': 'shshshfpb=shxO3D2Pdx1fxh3pn32BtOA%3D%3D; shshshfpa=7c8502d2-0075-bdd2-f31e-4941005ebd7a-1593842200; TrackID=13qWK-gk5VR-H_lom-EF8vZNa880899XWMLGbUMl9R3NYGGMa7UUQFxPNY2hdCbJD0nxRkiaWIvu4u8PHRzxLbDx7xZjKfV5iE7xTq5g_hSA; pinId=Ro7LRx1jaqfH2iniQChXULV9-x-f3wj7; qrsc=3; areaId=12; ipLoc-djd=12-984-53562-0; PCSYCityID=CN_320000_320200_320213; __jdc=122270672; wlfstk_smdl=hqa01ccj7uqto9ta9atku2n4edg8ek3w; cid=9; retina=1; wxa_level=1; wqmnx1=MDEyNjM1NHMub01sMG4gMFc7KWxLMyBNaWUgbS4xOWEzMUZmYWFCNFFFUylGKUg%3D; jxsid=16293739889121390817; webp=1; visitkey=7703795045962383; __jdv=122270672|google|hkbsc10|cpc|not set|1629373995047; __jda=122270672.1624846887632477341012.1624846888.1629373948.1629373995.7; shshshfp=41a7590ec2f565bd4aa46353e274f639; rkv=1.0; token=bec4e0c8bd0de70f191d8fce8538a336,1,905207; __tk=AURtAcaDkYeykrPuAzeEkYa0jYg5AUWDArj0AUWFAUa,1,905207; shshshsID=9b328a5eb9b9988bff04437523a3a4fd_4_1629374004700; __jdb=122270672.3.1624846887632477341012|7.1629373995; 3AB9D23F7A4B3C9B=5RR7MK52U2ZXTPZKFPDTX4MQQ35FRLDG6K2D6MEMWK5D2UQQ5K5ZRHKR4YJYUKYZXIPMIKDA6SGQJZBYBNYWITHBJY',
}

# params = (
#     ('keyword', '苹果'),
#     ('enc', 'utf-8'),
#     ('wq', 'p\'g'),
#     ('pvid', '755ad3b373a44bf6a60e34ba01009bdc'),
# )

response = requests.get('https://search.jd.com/Search?keyword=苹果', headers=headers,verify=False)
demo = etree.HTML(response.text)
print(demo.xpath("//div[@id='J_goodsList']/ul/li/div/div[@class='p-name p-name-type-2']/a/@href"))
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C&enc=utf-8&wq=p%27g&pvid=755ad3b373a44bf6a60e34ba01009bdc', headers=headers)