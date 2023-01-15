Title :- Get Gold-Silver-Crytpo prices in python

About :- This is a CLI based Data Extraction project written in python using both the prominent ways :- API requests and webscraping for extracting relevant information and displayng on CMD.

Important :- This is a CLI based python program ; to run use command python p1.py on CMD.

Overview :-
Data Extraction is a technique of extracting information from websites.
Python requests is used to send HTTP request and response utilizing get().

1)During API requests; most API servers send their response in JSON ; so we use .json() to get the content as python object .
API is used to retrieve data from remote websites by making a request to web server.
API is useful when data is changing quickly and we need only small piece of data from larger set of data.

2)During Webscraping ; data is embedded within the structure and style of websites ; so we use BeautifulSoup library and implement tag based searching .
BeautifulSoup is used for parsing HTML and xml documents . It creates a parse tree amd then we extract relevant data after finding element from relevant tags .


Requirements :-
Python 3.6,pip install request,pip install bs4,cmd.

Procedure/Working :-
1)Used try and except blocks for exception handling .
2)For choice == 1 and choice == 2 , I have adopted tag based searching using bs4. Request is done at below urls and with html parser we got desired text and printed msg as output.
Webpage for Gold price -> 'https://www.goodreturns.in/gold-rates/'
Webpage for Silver price -> https://www.goodreturns.in/silver-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29"

3)For choice == 3 , we have done request to api of coinlayer to fetch crypto prices and from the fetched data{contains all crypto coins data in json}; I took into consideration three coins.Please read their documentation to know how to get apikey for personal purpose.
API -> "http://api.coinlayer.com/live"
4)while is used for iterations and if else to evaluate conditions.






