def seconds_conversion(sec) :

	hours = sec // 3600
	rem_sec = sec % 3600
	minutes = rem_sec // 60
	seconds = rem_sec % 60

	print(f'Standard Time is : \n{hours} HOURS : {minutes} MINUTES : {seconds} SECONDS ')

#seconds_conversion(5000)



def minutes_conversion(mts):

	hours = mts // 60
	minutes = mts % 60

	print(f'Standard Time is : \n{hours} Hours : {minutes} Minutes ')

#minutes_conversion(122)


while True:
	print(' Enter 1 for seconds & 2 for Minutes & 3 to exit\n')
	choice = input()

	choicelist = ['1','2','3']
	if choice not in choicelist:
		print('Please enter 1 or 2 or 3')
		continue
	elif choice == '3':
		print('GoodBye User..!!! \n\n')
		break

	print('Enter the value you wish to convert : \n')
	value = int(input())
	
	if choice == '1' :
		seconds_conversion(value)
	elif choice == '2' :
		minutes_conversion(value)
	
	

	
	
	

	
		



