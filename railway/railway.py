from selenium import webdriver
from splinter.browser import Browser
from time import sleep
import sys

# username and passwd
username=sys.argv[1]
passwd=sys.argv[2]

#urls
ticket_url="https://kyfw.12306.cn/otn/leftTicket/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

#html ids
loginid="login_user"
unameid="username"
passwdid="password"

#cookies
starts=u'%u6DF1%u5733%u5317%2CIOQ'
ends=u'%u5B9C%u660C%u4E1C%2CHAN'
dtime=u'2017-02-16'
order=2

driver=webdriver.Chrome()
driver.get(ticket_url)

while driver.find_element_by_id(loginid):
 	# login
	driver.find_element_by_id(loginid).click()
	filluname=driver.find_element_by_id(unameid)
	filluname.send_keys(username)
	fillpasswd=driver.find_element_by_id(passwdid)
	fillpasswd.send_keys(passwd)

	while True:
		if driver.current_url != initmy_url:
			sleep
		else:
			break
	
	# login over
	if driver.current_url == initmy_url:
		break

driver.get(ticket_url)

driver.add_cookie({'name':'_jc_save_fromStation','value':starts})
driver.add_cookie({'name':'_jc_save_toStation','value':ends})
driver.add_cookie({'name':'_jc_save_fromDate','value':dtime})
driver.refresh()

while driver.current_url == ticket_url:
	driver.find_element_by_id(u"query_ticket").click()
	tickets=driver.find_elements_by_class_name(u"btn72")
	while len(tickets)==0:
		sleep(1)
		tickets=driver.find_elements_by_class_name(u"btn72")
	tickets[1].click()
	break
# 
# 
