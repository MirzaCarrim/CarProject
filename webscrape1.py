
# coding: utf-8

# In[221]:


import bs4


# In[222]:


1+1


# In[223]:


from urllib.request import urlopen as ureq


# In[224]:


from bs4 import BeautifulSoup as soup


# In[244]:


my_url ='https://www.autotrader.co.za/cars-for-sale/bmw/1-series?pagenumber=2'


# In[245]:


print(my_url)


# In[246]:


import numpy as np


# In[23]:


h = ['1','2']
for u in h:
    
    my_url1 ='https://www.autotrader.co.za/cars-for-sale/bmw/1-series?pagenumber='+u 
    
    print(my_url1)
    
    


# In[24]:


u_client = ureq(my_url1)

page_html = u_client.read()

u_client.close()


# In[25]:


page_soup = soup(page_html , "html.parser")


# In[26]:


print (page_soup.h1)


# In[27]:


print(page_soup.p)


# In[28]:


containers = page_soup.findAll("span" , {"class" : "e-icons"})


# In[29]:


len(containers)


# In[253]:


print(containers[1].span.data-aut-id.itemPrice)


# In[31]:


print(containers[23].span.text)


# In[32]:


x = np.linspace(0,len(containers),len(containers))

o = list(range(len(containers)))
o


# In[34]:


i=np.array(o)

for p in i :
    print(containers[p].span.text)


# In[75]:


import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import numpy as np

def web (pages):
    
    w = pages
    
    for Q in w :
        
    
    # This  gets our web page info , we use the bs4 and urlib packages
        my_url ='https://www.autotrader.co.za/cars-for-sale/bmw/1-series?pagenumber='+Q

        u_client = ureq(my_url)

        page_html = u_client.read()

        u_client.close()

        page_soup = soup(page_html , "html.parser")
        
        
        # this searches through the Html file and finds the elements that we are looking for 

        containers = page_soup.findAll("span" , {"class" : "e-price"})
        
        Names = page_soup.findAll("span" , {"class" : "e-title"})
        
        Year =page_soup.findAll("span" , {"class" : "e-icons"})

       

        o = list(range(len(containers)))
        
        price = []
        
        Title = []
        price2=0
        
        years=[]

        i=np.array(o)

        for p in i :
            price.append(containers[p].text)  # im pretty sure these 2 lines are useless at the moment
            Title.append(Names[p].text)
           
            
            print(containers[p].text + ',' + Names[p].text + ',' + Year[p].span.text) 
          

   
    


# In[78]:


web(['1','2' , '3'])

