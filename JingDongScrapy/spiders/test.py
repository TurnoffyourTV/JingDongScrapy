import requests
import json
cookies = {
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

headers = {
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

params = (
    ('productId', '5038041'),
    ('isShadowSku', '0'),
    # ('callback', 'jQuery2409238'),
    ('page', '4'),
    ('pageSize', '10'),
    # ('_', '1629347538484'),
)

response = requests.get('https://club.jd.com/discussion/getProductPageImageCommentList.action', headers=headers, params=params, cookies=cookies)
print(response.status_code)
data=json.loads(response.text)
print(data)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://club.jd.com/discussion/getProductPageImageCommentList.action?productId=5038041&isShadowSku=0&callback=jQuery2409238&page=4&pageSize=10&_=1629347538484', headers=headers, cookies=cookies)
