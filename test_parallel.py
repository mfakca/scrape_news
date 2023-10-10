from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import func
import time
import os
import asyncio





main_topic_list = ['turkiye','dunya','ekonomi','spor','gundem']
total_fail_page = 0

counter = 0




async def get_url(s,main_topic, min_range, max_range):
    
    urls = []
    
    
    
    for page_idx in range(min_range,max_range):

        start_url = f"https://www.trthaber.com/haber/{main_topic}/{page_idx}.sayfa.html"
        #print(start_url)
        r = await s.get(start_url)
        
        news =  r.html.find('div [class=news-container]')

        for x in news:
            
            for i in x.find('a[class=site-url]'):
                #print(i)
                #print(i.find('a', first=True))
                
                urls.append(list(i.find('a', first=True).links)[0])
                
    
    return urls


async def get_page_content(s,urls,main_topic):
    
    for url in urls:
    
        r = await s.get(url)
        
        for i in r.html.find('div[class=news-content]'):
            
            if i is None: 
                continue
            
            else: 
                text = i.text.split('ETİKETLER')[0]
                
        with open(f'data/trt/{main_topic}/{url.split("/")[-1].replace(".html","")}.txt', "w",encoding= 'utf-8') as out:
            out.write(text)
            
            
    
start_time = time.time()   

async def main(x):
    s = AsyncHTMLSession()
    links_spor_1 = await get_url(s,'spor',1,10)
    links_gundem_1 = await get_url(s,'gundem',1,10)
    links_turkiye_1 = await get_url(s,'turkiye',1,10)
    links_ekonomi_1 = await get_url(s,'ekonomi',1,10)
    links_dunya_1 = await get_url(s,'dunya',1,10)
    
    links_spor_2 = await get_url(s,'spor',10,20)
    links_gundem_2 = await get_url(s,'gundem',10,20)
    links_turkiye_2 = await get_url(s,'turkiye',10,20)
    links_ekonomi_2 = await get_url(s,'ekonomi',10,20)
    links_dunya_2 = await get_url(s,'dunya',10,20)
    
    links_spor_3 = await get_url(s,'spor',20,30)
    links_gundem_3 = await get_url(s,'gundem',20,30)
    links_turkiye_3 = await get_url(s,'turkiye',20,30)
    links_ekonomi_3 = await get_url(s,'ekonomi',20,30)
    links_dunya_3 = await get_url(s,'dunya',20,30)
    
    tasks = (get_page_content(s,links_spor_1, 'spor'), get_page_content(s,links_gundem_1, 'gundem'), get_page_content(s,links_turkiye_1, 'turkiye'), get_page_content(s,links_ekonomi_1, 'ekonomi'), get_page_content(s,links_dunya_1,'dunya'),
             get_page_content(s,links_spor_2, 'spor'), get_page_content(s,links_gundem_2, 'gundem'), get_page_content(s,links_turkiye_2, 'turkiye'), get_page_content(s,links_ekonomi_2, 'ekonomi'), get_page_content(s,links_dunya_2,'dunya'),
             get_page_content(s,links_spor_3, 'spor'), get_page_content(s,links_gundem_3, 'gundem'), get_page_content(s,links_turkiye_3, 'turkiye'), get_page_content(s,links_ekonomi_3, 'ekonomi'), get_page_content(s,links_dunya_3,'dunya')) #, get_page_content(s,get_url(s,'turkiye')), get_page_content(s,get_url(s,'ekonomi')), get_page_content(s,get_url(s,'dunya')))
    return await asyncio.gather(*tasks)

start_time = time.time()   
results = asyncio.run(main(1))
print(time.time() - start_time)
print(results)