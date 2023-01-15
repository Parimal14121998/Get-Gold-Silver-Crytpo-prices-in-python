#import libs --> please install with pip if required

import requests
import bs4
import random 

#bots used for webscraping because sometimes we get 404 error
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]


'''

Imp - This is a CLI based python program ; to run use command python p1.py on CMD.
1)Used try and except blocks for exception handling .
2)For choice == 1 and choice == 2 , I have adopted tag based searching using bs4. Request is done at below urls and with html parser we got desired text and printed msg as output.
3)For choice == 3 , we have done request to api of coinlayer to fetch crypto prices and from the fetched data{contains all crypto coins data in json}; I took into consideration three coins.Please read their documentation to know how to get apikey for personal purpose.
4)while is used for iterations and if else to evaluate conditions.

'''


try:
	choice = int(input("click 1 to Check Gold price\nClick 2 to Check Silver price\nClick 3 to Check Crypto prices\nClick 4 to Exit "))
	print("-----------------------------------")
	while True:
		if choice==1:		
			try:
				r_gold = requests.get('https://www.goodreturns.in/gold-rates/', headers={'User-Agent': random.choice(user_agents_list)})
				soup=bs4.BeautifulSoup(r_gold.text,"html.parser")
				price_gold=soup.select("strong")[0].text
				msg1="Gold per gm is " + str(price_gold).strip()
				print(msg1)
				print("-----------------------------------")
				break
			except Exception as e:
				print("Some issue :- " + str(e))
		elif choice == 2:
			try:
				r_silver = requests.get("https://www.goodreturns.in/silver-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29", headers={'User-Agent': random.choice(user_agents_list)})
				soup = bs4.BeautifulSoup(r_silver.text, 'html.parser')
				price = soup.find("div", class_="gold_silver_table right-align-content").find("tr", class_="odd_row").findAll("td")
				price_silver = price[1].text
				msg2 = "Silver per gm is " + str(price_silver) 
				print(msg2)
				print("-----------------------------------")
				break
			except Exception as e:
				print("Some issue :- " + str(e))
		elif choice == 3:
			try:
				a1="http://api.coinlayer.com/live"
				a2="?access_key=" + "7cf1f40966f385c2b7121d4bd4ef71d8"
				wa=a1+a2
				res=requests.get(wa)
				data=res.json()

				rate1=data["rates"]['BTC']
				rate2=data["rates"]['ETH']
				rate3=data["rates"]['DOGE']
		
				msg3="Bitcoin = $ "  + str(rate1) + "\nEthereum = $ " + str(rate2) + "\nDogecoin = $ " + str(rate3)
				print(msg3)
				print("-----------------------------------")
				break
			except Exception as e:
				print("Some issue :- " + str(e))
		elif choice ==4:
			print("Exit granted")
			print("-----------------------------------")
			break
		else:
			print("invalid option")
			print("-----------------------------------")
			break
except Exception as e:
	print("Some issue :- " + str(e))

