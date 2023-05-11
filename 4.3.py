import json

log = input('Введите логин:')
passwd = input('Введите пароль:')
data_in = {}
def login_function(log, passwd):
	with open('1.json', 'r') as f:
		data_in = json.load(f)
		if log not in data_in.keys():
			print('Повторте попытку!')
		else:
			print('Вход выполнен!')

login_function(log, passwd)	