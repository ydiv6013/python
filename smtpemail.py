# send email using gmail smtp

import  smtplib as smtp

mail_server =""
mail_port = 465
mail_uname ="yogesh.dhameliya6013@gmail.com"
mail_pwd = ""
mail_sender = "yogesh.dhameliya6013@gmail.com"
mail_receiver = "yogesh.dhameliya@outlook.com"
mail_msg = "Subject : Python email \n\nPython smtp mail works"
# gmail app 

try :
    # connection is the smtp mail object
    with smtp.SMTP_SSL(host=mail_server,port=mail_port) as con :
        print(con)
        #login to smtp server
        login =con.login(user=mail_uname,password=mail_pwd)
        print(login)
        #send mail
        mail =con.sendmail(from_addr=mail_sender,to_addrs=mail_receiver,msg=mail_msg)

        print("status",mail)

except :
    print("Opps something went wrong !!!!")
