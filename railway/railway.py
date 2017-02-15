# -*- coding: utf-8 -*-

from splinter.browser import Browser
from time import sleep
import traceback
import sys

# username and passwd
username=sys.argv[1]
passwd=sys.argv[2]

#urls
ticket_url="https://kyfw.12306.cn/otn/leftTicket/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

#html ids
loginid="login_user"
unameid="loginUserDTO.user_name"
passwdid="userDTO.password"

#cookies
starts=u"%u6DF1%u5733%u5317%2CIOQ"
ends=u"%u5B9C%u660C%u4E1C%2CHAN"
dtime=u"2017-02-16"
order=2

browser=Browser('chrome')
browser.visit(ticket_url)

print browser.is_element_present_by_id(loginid)

while browser.is_element_present_by_id(loginid):
	sleep(1)

	# login
	browser.find_by_id(u"login_user").click()
	browser.fill(unameid, username)
	browser.fill(passwdid, passwd)

	while True:
		if browser.url != initmy_url:
			sleep
		else:
			break
	
	# login over
	if browser.url == initmy_url:
		break

browser.visit(ticket_url)

browser.cookies.add({"_jc_save_fromStation": starts})
browser.cookies.add({"_jc_save_toStation": ends})
browser.cookies.add({"_jc_save_fromDate": dtime})
browser.reload()

while browser.url == ticket_url:
	browser.find_by_id(u"query_ticket").click()
 	ticket=browser.find_link_by_href('javascript:')
	print ticket
	break


