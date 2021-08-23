import requests

headers = {
    'authority': 'search.jd.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.jd.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cookie': 'shshshfpb=shxO3D2Pdx1fxh3pn32BtOA%3D%3D; shshshfpa=7c8502d2-0075-bdd2-f31e-4941005ebd7a-1593842200; TrackID=13qWK-gk5VR-H_lom-EF8vZNa880899XWMLGbUMl9R3NYGGMa7UUQFxPNY2hdCbJD0nxRkiaWIvu4u8PHRzxLbDx7xZjKfV5iE7xTq5g_hSA; pinId=Ro7LRx1jaqfH2iniQChXULV9-x-f3wj7; qrsc=3; areaId=12; ipLoc-djd=12-984-53562-0; PCSYCityID=CN_320000_320200_320213; rkv=1.0; __jdv=122270672|google|hkbsc10|cpc|not set|1629377617013; user-key=d15965f3-8070-40fe-962e-d8f4f2099b8a; __jda=122270672.1624846887632477341012.1624846888.1629373948.1629373995.7; __jdb=122270672.31.1624846887632477341012|7.1629373995; __jdc=122270672; shshshfp=41a7590ec2f565bd4aa46353e274f639; shshshsID=9b328a5eb9b9988bff04437523a3a4fd_31_1629377642142; 3AB9D23F7A4B3C9B=5RR7MK52U2ZXTPZKFPDTX4MQQ35FRLDG6K2D6MEMWK5D2UQQ5K5ZRHKR4YJYUKYZXIPMIKDA6SGQJZBYBNYWITHBJY',
}

params = (
    ('keyword', '\u82F9\u679C'),
    ('enc', 'utf-8'),
    ('wq', '\u82F9\u679C'),
    ('pvid', 'a18608d575914ceaaab229a798c32dc2'),
)

response = requests.get('https://search.jd.com/Search', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C&enc=utf-8&wq=%E8%8B%B9%E6%9E%9C&pvid=a18608d575914ceaaab229a798c32dc2', headers=headers)
