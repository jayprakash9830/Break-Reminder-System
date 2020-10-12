from plyer import notification
import time 
import os 
def checkTodaysBirthdays(): 
	fileName = open("./remind.txt", 'r') 
	today = time.strftime('%y-%m-%d') 
	flag = 0
	for line in fileName: 
		if today in line: 
			line = line.split(' ') 
			flag =1
			notification.notify(
			title = line[2],
			message = "Hello Sir Today Important Reminder is "+line[1]+" "+line[2],
			app_icon = "./image/clock.ico",
			timeout= 10
			)

if __name__ == '__main__': 
	checkTodaysBirthdays() 

