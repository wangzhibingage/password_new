password = 'a12345'
x = 0
while x < 3:
	psw = input('请输入密码： ')
	if psw == password:
		print('登入成功')
		break
	else:
		x = x + 1
		y = 3 -x
		print('密码错误')
		if x < 3:
			print('密码错误，请重新输入，还有', y,'次机会')
		else:
			print('没有机会了，您的账户被锁住了！')
