import requests
from bs4 import BeautifulSoup

r = requests.get("http://store.steampowered.com/search/?specials=1&os=win")
soup = BeautifulSoup(r.content, "html.parser")

first = soup.find_all('span', {'class':'title'})
rel = soup.find_all('div', {'class':'col search_released responsive_secondrow'})
dis = soup.find_all('div', {'class':'col search_discount responsive_secondrow'})
amt = soup.find_all('div', {'class':'col search_price discounted responsive_secondrow'})
l = len(first)

file=open('SteamSale.txt','w')

for i in range(0,l):
	file.write("Name: "+first[i].text+'\n')
	file.write("Release Date: "+rel[i].text+'\n')
	d = dis[i].text
	file.write("Percentage Discount: "+d[1:len(d)-1]+'\n')
	a = amt[i].text
	sec=0
	flag=0
	j=2
	while flag==0:
		if a[j]=='₹':
			sec=j
			flag=1
		j+=1
	file.write("Original price: "+a[2:sec]+'\n')
	file.write("Discounted Price: "+a[sec+1:].rstrip()+'\n')
	file.write('\n')
file.close()
	

