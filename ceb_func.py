
# coding: utf-8

# In[30]:





# In[31]:


import requests


# In[32]:


url = 'http://www.cebbank.com/eportal/ui?moduleId=12073&struts.portlet.action=/app/yglcAction!listProduct.action'


# In[33]:


headers = {
    'Accept':'text/html, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'1297',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'ALLYESID4=0E431EBFBE182AC6; BIGipServerpool_nport=570927296.20480.0000; ADMINCONSOLESESSION=HjB1ZbYpwrkrp4DpnmD3JGXYLG3Pvbhv30HMxhsGQYhLp20Yl3mT!1191843562; WT_FPC=id=2eefcbee4e636d289ab1500861828642:lv=1503371161579:ss=1503369407438; iss_nu=0; iss_cc=true; iss_id=62634ef558c42df7b14324c9a34517d2; iss_ot=1503371161664; iss_sid=b2b5ea23dd6f1763e9fc8227edc241d7; iss_svid=67fa1e18a949254c825875a149416194',
    'Host':'www.cebbank.com',
    'Origin':'http://www.cebbank.com',
    'Referer':'http://www.cebbank.com/site/gryw/yglc/lccp49/index.html',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'}


# In[43]:


data = {
    'codeOrName':'',
    'TZBZMC':'RMB',
    'QGJE':'',
    'QGJELEFT':'',
    'QGJERIGHT':'',
    'CATEGORY':'',
    'CPQXLEFT':'',
    'CPQXRIGHT':'',
    'CPFXDJ':'',
    'SFZS':'Y',
    'CPTJLX':'',
    'qxrUp':'Y',
    'qxrDown':'',
    'dqrUp':'',
    'dqrDown':'',
    'qdjeUp':'',
    'qdjeDown':'',
    'qxUp':'',
    'qxDown':'',
    'yqnhsylUp':'',
    'yqnhsylDown':'',
    'page':'1',
    'pageSize':'5',
    'channelIds[]':['yxl94','ygelc79','hqb30','dhb2','cjh','gylc70','Ajh67',
                       'Ajh84','901776','Bjh91','Ejh99','Tjh70','tcjh96','ts43','ygjylhzhMOM25','yxyg87','zcpzjh64',
                         'wjyh1','smjjb9','ty90','tx16','ghjx6','wf36','ygxgt59','wbtcjh3','wbBjh77','wbTjh28',
                          'sycfxl','cfTjh','jgdhb','tydhb','jgxck','jgyxl','tyyxl','dgBTAcp','27637097','27637101','27637105',
                          '27637109','27637113','27637117','27637121','27637125','27637129','27637133']}


# In[46]:


re = requests.post(url,data = data,headers = headers)


# In[47]:


print(re.text)


# In[ ]:




