import pandas as pd
import requests
import bs4
import re



df = pd.read_csv("SampleDataset.csv")


def get_email(soup):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return email

def get_contact(soup):
    try:
        contact = soup.select("a[href*=callto]")[0].text
        return contact
    except:
        pass

    try:
        contact = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return contact
    except:
        pass

    try:
       contact = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
       return contact
    except:
        print ('contact number not found')
        contact = ''
        return contact



for i, row in df.iterrows():
    url = 'http://www.' + row['website']
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except:
        print ('Unsucessful: ' + str(response))
        continue

    phone = get_contact(soup)
    email = get_email(soup)

    df.loc[i,'contact'] = contact
    df.loc[i,'Email'] = email
    print ('website:%s\ncontact: %s\nemail: %s\n' %(url, contact, email))