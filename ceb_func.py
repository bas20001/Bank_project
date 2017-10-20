# coding: utf-8

# In[37]:


# encoding=utf-8


# In[38]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[39]:


def download_url(url,data,headers):
    
    html = requests.post(url,data = data,headers = headers).text
    return html


# In[59]:



def html_parse(html):
    ceb_func_name_list = []
    ceb_func_shouyi_list = []
    ceb_func_shijian_list = []
    soup = BeautifulSoup(html,'html.parser')
    content = soup.find('div',attrs={'class':'lccp_main_content_tx'})
    all_li = content.find_all('li')
    page = soup.find('div',attrs={'lccp_page'})
    currentpage = page.find('span',attrs={'id':'currentPage'}).text
    totalpage = page.find('span',attrs={'id':'totalpage'}).text
    global shouyi
    while currentpage != totalpage:
        for li in all_li:
            name = li.find('a').text.replace('\r','').replace('\n','').replace('\t','')
            ceb_func_name_list.append(name)
            specifics = li.find_all('p')
            d1 = specifics[0].find_all('span')
            shijian = specifics[1].find('span').text.replace('\r','').replace('\n','').replace('\t','')
            ceb_func_shijian_list.append(shijian)
            if shijian != "--" :
                shouyi = d1[1].text.replace('\r','').replace('\n','').replace('\t','')
            else :
                shouyi = " "    
            ceb_func_shouyi_list.append(shouyi)
        currentpage = int(currentpage) + 1
        data['page']=currentpage
        return ceb_func_name_list,ceb_func_shouyi_list,ceb_func_shijian_list,data
    else :
        for li in all_li:
            name = li.find('a').text.replace('\r','').replace('\n','').replace('\t','')
            ceb_func_name_list.append(name)
            specifics = li.find_all('p')
            d1 = specifics[0].find_all('span')
            shijian = specifics[1].find('span').text.replace('\r','').replace('\n','').replace('\t','')
            ceb_func_shijian_list.append(shijian)
            if shijian != "--" :
                shouyi = d1[1].text.replace('\r','').replace('\n','').replace('\t','')
            else :
                shouyi = " "    
            ceb_func_shouyi_list.append(shouyi)
            
        return ceb_func_name_list,ceb_func_shouyi_list,ceb_func_shijian_list,None
        



# In[65]:


def main():
    url = 'http://www.cebbank.com/eportal/ui?moduleId=12073&struts.portlet.action=/app/yglcAction!listProduct.action'
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
    data = {
        'SFZS':'Y',
        'TZBZMC':'RMB',
        'pageSize':'12',
        'page':'1',
        'qxrUp':'Y',
        'qdjeUp':'',
        'channelIds[]':['yxl94','ygelc79','hqb30','dhb2','cjh','gylc70','Ajh67',
                       'Ajh84','901776','Bjh91','Ejh99','Tjh70','tcjh96','ts43','ygjylhzhMOM25','yxyg87','zcpzjh64',
                       'wjyh1','smjjb9','ty90','tx16','ghjx6','wf36','ygxgt59','wbtcjh3','wbBjh77','wbTjh28',
                       'sycfxl','cfTjh','jgdhb','tydhb','jgxck','jgyxl','tyyxl','dgBTAcp','27637097','27637101','27637105',
                       '27637109','27637113','27637117','27637121','27637125','27637129','27637133']}
    
    ceb_func_name_all = []
    ceb_func_shouyi_all = []
    ceb_func_shijian_all = []
    while data:
        html = download_url(url,data,headers)
        ceb_func_name_list,ceb_func_shouyi_list,ceb_func_shijian_list,data = html_parse(html)
        ceb_func_name_all.extend(ceb_func_name_list)
        ceb_func_shouyi_all.extend(ceb_func_shouyi_list)
        ceb_func_shijian_all.extend(ceb_func_shijian_list)
        dataframe = pd.DataFrame({'理财名称':ceb_func_name_all,'理财收益':ceb_func_shouyi_all,'理财时间':ceb_func_shijian_all})
        dataframe.to_csv("ceb_20171020.csv",index=False,sep=",")


# In[66]:


data = {
    'SFZS':'Y',
    'TZBZMC':'RMB',
    'pageSize':'12',
    'page':'1',
    'qxrUp':'Y',
    'qdjeUp':'',
    'channelIds[]':['yxl94','ygelc79','hqb30','dhb2','cjh','gylc70','Ajh67',
                       'Ajh84','901776','Bjh91','Ejh99','Tjh70','tcjh96','ts43','ygjylhzhMOM25','yxyg87','zcpzjh64',
                         'wjyh1','smjjb9','ty90','tx16','ghjx6','wf36','ygxgt59','wbtcjh3','wbBjh77','wbTjh28',
                          'sycfxl','cfTjh','jgdhb','tydhb','jgxck','jgyxl','tyyxl','dgBTAcp','27637097','27637101','27637105',
                          '27637109','27637113','27637117','27637121','27637125','27637129','27637133']}


# In[67]:


if __name__ == '__main__':
    main()

