import smtplib                                                       #импорт сетевого протокола SMTP
from email.mime.text import MIMEText                                 #создание текстовых объектов


def send_email(message):                                             #создаем инструкию отправки сообщения  
    sender="pythonmailassistant@mail.ru"                             #отправитель и пароль от почты отправителя
    password="bJDZxDu4LJ1E1gLACBTC"
    addressee="pythonmailassistant@mail.ru"                          #получатель

    server = smtplib.SMTP("smtp.mail.ru", 587)                       #доменное имя smpt-сервера и его порт
    server.starttls()                                                #подключение к шифрованию TLS

    try:                                                             #обработка исключений
        server.login(sender, password)                               #логин и пароль отправителя
        msg = MIMEText(message)                                      #создание объекта - сообщения
        msg["Subject"] = "Фотоотчёт"
        server.sendmail(sender, addressee, msg.as_string())          #отправитель, получатель, заголовок (тема) и само сообщение
        return "Сообщение отправлено"                                #возврат сообщения в случае успешной отправки
    except Exception as _ex:                                         #обработка ошибок и возврат сообщения об ошибке
        return f"{_ex}\nНеверный логин или пароль."


def main():                                                          #функция отправки сообщения 
    message = input("Введите сообщение: ")                           #ввод сообщения
    print(send_email(message=message))                               #передача введенного сообщения 


if __name__ == "__main__":                                           #конструкция для контроля скрипта, скрипт выполняется только при его запуске
    main()



