
# coding: utf-8

# In[6]:




import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://wealth.cib.com.cn/retail/onsale/index.html'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'}
cookies = {}

html = requests.get(url=DOWNLOAD_URL,headers = headers).content

soup = BeautifulSoup(html,'html.parser')
func_list = []
for func_info in soup.find_all('div',attrs = {'class':'middle'}):
    func_detial = func_info.find_all('td',attrs = {'align':'center'})
    for func_name in func_detial:
        func_list.append(func_name.string)

with codecs.open('cib_func','wb',encoding='utf-8')as cib:
    cib.write(str(func_list))


# In[ ]:




