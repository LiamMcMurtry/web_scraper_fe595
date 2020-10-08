#!/usr/bin/env python
# coding: utf-8

# In[123]:


import requests
import pandas as pd
def Web_Scraping():
    com = pd.DataFrame(columns=['Name', 'Purpose'])
    for i in range(50):
        # Here we make a request using the URL provided. Every time this URL is executed, it will generate info for a new, random company
        req = requests.get('http://3.95.249.159:8000/random_company').text
        new = req.split('<ol>')[1].split('</ol>')[0].split('<li>')
        list = {}
        for n in new:
            data = n.replace('\n', '').replace('</li>', '').strip(' ')
            if 'Name:' in data:
                list['Name'] = data.split('Name: ')[1]
            if 'Purpose:' in data:
                list['Purpose'] = data.split('Purpose: ')[1]
        com = com.append(list, ignore_index = True)
    # Here we download the data to a CSV file
    com.to_csv(r'User Pathway \extracted_companies.csv', index = False)

if __name__ == '__main__':
    Web_Scraping()


# In[ ]:





# In[94]:





# In[104]:





# In[ ]:




