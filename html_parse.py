"""
how to parse html
1. pandas
2. bs4
"""

# read html from 公開資訊
import requests
url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04' # 綜合損益彙總表
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

#1. use pandas to parse table
import pandas as pd
dfs = pd.read_html(r.text, header=None)
print(f"there are {len(dfs)} tables in response")
print(dfs[1].head())

"""
there are 7 tables in response
   公司代號 公司名稱    利息淨收益  利息以外淨損益  呆帳費用、承諾及保證責任準備提存     營業費用  繼續營業單位稅前淨利（淨損）  \
0  2801   彰銀  4806993  2087960            575554  3940985         2378414   
1  2809  京城銀  1379752  1356624           -613459   592774         2757061   
2  2812  台中銀  2247016  1041507            319727  1646104         1322692   
3  2820   華票   319400   472258             -5654   129203          668109   
4  2834  臺企銀  4321420  1241992           1099802  3165320         1298290   

   所得稅費用（利益）  繼續營業單位本期稅後淨利（淨損） 停業單位損益  ... 其他綜合損益（稅後）  合併前非屬共同控制股權綜合損益淨額  \
0     432509           1945905     --  ...     417173                 --   
1     333299           2423762     --  ...   -1032833                 --   
2     192448           1130244     --  ...     290829                 --   
3     137129            530980     --  ...    -301765                  0   
4     196637           1101653      0  ...     376394                 --   

   本期綜合損益總額（稅後） 淨利（損）歸屬於母公司業主  淨利（損）歸屬於共同控制下前手權益 淨利（損）歸屬於非控制權益 綜合損益總額歸屬於母公司業主  \
0       2363078       1945905                 --            --        2363078   
1       1390929       2423762                 --            --        1390929   
2       1421073       1130244                 --            --        1421073   
3        229215            --                 --            --             --   
4       1478047       1101653                  0             0        1478047   

  綜合損益總額歸屬於共同控制下前手權益 綜合損益總額歸屬於非控制權益 基本每股盈餘（元）  
0                 --             --      0.19  
1                 --             --      2.17  
2                 --             --      0.27  
3                 --             --      0.40  
4                  0              0      0.15  

[5 rows x 22 columns]
"""

# 2. use bs4 to parse html
from bs4 import BeautifulSoup

# 2-1. 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(r.text, 'html.parser')

# 2-2. 輸出排版後的 HTML 程式碼
print(soup.prettify())

"""
<html>
 <head>
  <title>
   公開資訊觀測站
  </title>
  <link href="css/css2.css" media="Screen" rel="stylesheet" type="text/css"/>
  <script src="js/mops2.js" type="text/javascript">
  </script>
 </head>
...
"""

# 2-3. 網頁標題 HTML 標籤
title_tag = soup.title
print(title_tag)
"""
<title>公開資訊觀測站</title>
"""

# 2-4. 網頁的標題文字
print(title_tag.string)
"""
公開資訊觀測站
"""

# 2-5. 所有的超連結
a_tags = soup.find_all('td')
for tag in a_tags[:5]:
  # 輸出超連結的文字
  print(tag.string)
  
"""
上市公司第一季資料
註：依證券交易法第36條及證券期貨局相關函令規定，財務報告申報期限如下：
1.一般行業申報期限：第一季為5月15日，第二季為8月14日，第三季為11月14日，年度為3月31日。
2.金控業申報期限：第一季為5月30日，第二季為8月31日，第三季為11月29日，年度為3月31日。
3.銀行及票券業申報期限：第一季為5月15日，第二季為8月31日，第三季為11月14日，年度為3月31日。
"""

for tag in a_tags[:5]:
  # 輸出超連結網址
  print(tag.get('style'))
  
"""
text-align:center !important;
text-align:left !important;
text-align:left !important;
text-align:left !important;
text-align:left !important;
"""

# 2-6. 搜尋所有超連結與粗體字
tags = soup.find_all(["h2", "td"])
print(tags[:5])

"""
[
  <td style="text-align:center !important;"><h2>上市公司第一季資料</h2></td>, 
  <h2>上市公司第一季資料</h2>, 
  <td style="text-align:left !important;">註：依證券交易法第36條及證券期貨局相關函令規定，財務報告申報期限如下：</td>, 
  <td style="text-align:left !important;">1.一般行業申報期限：第一季為5月15日，第二季為8月14日，第三季為11月14日，年度為3月31日。</td>, 
  <td style="text-align:left !important;">2.金控業申報期限：第一季為5月30日，第二季為8月31日，第三季為11月29日，年度為3月31日。</td>
]
"""

# 2-7. 限制搜尋結果數量
tags = soup.find_all(["h2", "td"], limit=2)
print(tags)

"""
[
  <td style="text-align:center !important;"><h2>上市公司第一季資料</h2></td>, 
  <h2>上市公司第一季資料</h2>, 
]
"""

# 2-8. 只抓出第一個符合條件的節點
a_tag = soup.find("td")
print(a_tag)

"""
<td style="text-align:center !important;"><h2>上市公司第一季資料</h2></td>
"""
