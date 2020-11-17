import requests


print('''
██████╗██╗ ██████╗ ███████╗██████╗ 
╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗
   ██║   ██║██║  ███╗█████╗  ██████╔╝
   ██║   ██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ██║╚██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                     ''')
print("snapchat:(ar5824)")
print("for check number(1) for check email(2)")
uyy = input("enter option-->")

if uyy == '1':
    print()
    mounir = input('put the number:-->')

    aaa1 = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    info1 = "email_or_username=" + mounir + "&recaptcha_challenge_field=&flow="
    headers1 = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.instagram.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Origin": "https://www.instagram.com",
        "X-CSRFToken": "TnVNOReZSuQKaXRz8DOP5ajLrcWkkf4K",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "mid=X6GnKAALAAFpgeqDe6GeXRHLg9D5"
    }

    response = requests.request("POST", aaa1, data=info1, headers=headers1)
    if "email_or_sms_sent" in response.text:

        print("")
        print('The number is related', mounir)

    elif "message" in response.text:

        print("The number is not related", mounir)
elif uyy == '2':
    print('''
██████╗██╗ ██████╗ ███████╗██████╗ 
╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗
   ██║   ██║██║  ███╗█████╗  ██████╔╝
   ██║   ██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ██║╚██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                     ''')
    print("snapchat(ar5824)")
    mounir1 = input('put the email:-->')

    aaa1 = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    info1 = "email_or_username=" + mounir1 + "&recaptcha_challenge_field=&flow="
    headers1 = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.instagram.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Origin": "https://www.instagram.com",
        "X-CSRFToken": "TnVNOReZSuQKaXRz8DOP5ajLrcWkkf4K",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "mid=X6GnKAALAAFpgeqDe6GeXRHLg9D5"
    }

    response = requests.request("POST", aaa1, data=info1, headers=headers1)
    if "email_or_sms_sent" in response.text:

        print('The email is related', mounir1)

    elif "message" in response.text:

        print("The email is not related", mounir1)