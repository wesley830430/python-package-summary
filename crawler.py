"""
show crawler relative package
1. requests
"""

import requests

# test 台灣證券交易所財報
url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04' # 綜合損益彙總表
# url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05' # 資產負債彙總表
# url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06' # 營益分析彙總表
data = {
    'encodeURIComponent':1,
    'step'              :1,
    'firstin'           :1,
    'off'               : 1,
    'TYPEK'             :'sii',
    'year'              :'110',
    'season'            :'1',
}
r = requests.post(url, data)

r.encoding = 'utf8'
print(r.text)

""" brief show result
<html>
<head>
	<title>公開資訊觀測站</title>
	
	
	<link href="css/css2.css" rel="stylesheet" type="text/css" Media="Screen"/> 
	
	<script type="text/javascript" src="js/mops2.js"></script>
</head>
...
"""
