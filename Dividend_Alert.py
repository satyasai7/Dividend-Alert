





import requests
from datetime import date 
from twilio.rest import Client

from bs4 import BeautifulSoup

def format(lis):
	text = "\n\nName of the Company :  {0}\nType : {1}\n% : {2}\nAnnouncement : {3}\nRecord : {4}\nEx-Dividend : {5}\n\n\n"
	a = text.format(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5])
	return a


acc_sid = 'ACe7e7f9d51a297e660ba20ffc4bb9661d'
auth_token = 'cb6e661b326e7e9dc7a12e3381d88489'

client = Client(acc_sid,auth_token)
data = requests.get('https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php')

phone_num = ''#Enter your number 

soup = BeautifulSoup(data.text, 'html.parser')

div = soup.find('div',{'class':'FL PR20'})
div2 = div.find('div',{'class':'MT15'})
div3 = div2.find('table')
div4 = div3.find_all('tr')[2]


lis = []

for tr in div3.find_all('tr')[2:]:
	
	name = tr.find_all('td')[0].text.strip()
	typee = tr.find_all('td')[1].text.strip()
	percent = tr.find_all('td')[2].text.strip()
	ann = tr.find_all('td')[3].text.strip()
	record = tr.find_all('td')[4].text.strip()
	exdiv= tr.find_all('td')[5].text.strip()


	lis.append([name,typee,percent,ann,record,exdiv])


today = date.today()


datee = today.strftime("%d-%m-%Y")
print(datee)

ans = "DIVIDENDS\n\n"
for y in lis:
	if y[3]==d:
		a = format(y)
		ans = ans + a


message = client.messages.create(
    body=ans,
    from_='+12015145230',
    to=phone_num)
