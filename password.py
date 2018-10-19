password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pwd = input('please enter the password: ')
	if pwd == password:
		print('success!')
		break
	else:
		print ('wrong password, you have', x, 'more times to enter')
		if x > 0:
			print ('you have', x, 'more times to enter')
		else:
			print ('you have no more chances! Account will be closed')