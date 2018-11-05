import random
from django.core.mail import send_mail

def Random(count):
    chars=['A','B','C','D','E','F','G''H''I','J','K',
           'L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

    return ''.join(random.sample(chars,4))

def SendForgetPasswordMail(email,verificationcode):
    title='【学生管理系统】忘记密码邮件'
    body='您好，您的验证码为%s,请妥善保管。' % verificationcode
    send_mail(subject=title,message=body,from_email='学生管理系统<jxjjyg@126.com>', recipient_list=[email])