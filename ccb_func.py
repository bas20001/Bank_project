
# coding: utf-8

# In[1]:





# In[2]:


import requests


# In[3]:


url = 'http://finance.ccb.com/cc_webtran/queryFinanceProdList.gsp?jsoncallback=jQuery19104241771066635531_1503378491298'


# In[4]:


headers = {
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'64',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'',
    'Host':'finance.ccb.com',
    'Origin':'http://finance.ccb.com',
    'Referer':'http://finance.ccb.com/cn/finance/product.html',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'}


# In[5]:


data = {
    'queryForm.provinceId':'110',
    'queryForm.brand':'03',
    'pageNo':'1',
    'pageSize':'12'
   }


# In[6]:


re = requests.post(url,data = data,headers = headers)


# In[7]:


print(re.text)


# In[ ]:




