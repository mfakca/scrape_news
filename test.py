from requests_html import HTMLSession
from bs4 import BeautifulSoup
import func
import time
import os


session = HTMLSession()


main_topic_list = ['gundem','turkiye','dunya','ekonomi','spor']
total_fail_page = 0


main_topic = 'gundem'

page_url = 'https://www.trthaber.com/haber/gundem/bakan-tunc-onceligimiz-deprem-bolgesi-795829.html'

page_url_extended = page_url.split('/')[-1].replace('.html','')


print(page_url)
#print(title)
#print(page_url_extended)

page_r = session.get(page_url)
page_soup = BeautifulSoup(page_r.content, "lxml")


a = page_soup.find('div',attrs={'class':'news-content'})


    
    
page_text = a.text.split('ETİKETLER')[0]
page_header = page_soup.find('h2',attrs={'class':'news-spot'}).text
    
    
#print(page_header)
#print(page_text)
            
            
            
    #page_text = page_soup.find('div',attrs={'class':'news-content'}).find('p').text #.split('ETİKETLER')[0]
    #page_header = page_soup.find('h2',attrs={'class':'news-spot'}).text
    #page_paragraph = func.edit_upper_text(page_text.find('div',attrs={'class':'news-content readingTime'}).text) 
    

page_paragraph = func.replace_text(page_text)

print(page_paragraph)
    
   

f = open(f"data/trt/{main_topic}/{page_url_extended}.txt", "w", encoding='utf-8')
f.write(page_paragraph)
f.close()
     
