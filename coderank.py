#!/usr/bin.python
import requests
from BeautifulSoup import BeautifulSoup

user_name=raw_input("Enter a valid user name---  ")
respond = requests.get("http://codeforces.com/profile/"+user_name)
#print respond.content 

soup = BeautifulSoup(respond.content)

print soup.find('div',attrs={'class':'main-info '}).find('span',attrs={'class':'user-gray'}).text

