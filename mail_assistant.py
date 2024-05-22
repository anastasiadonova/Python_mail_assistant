import smtplib                                                       #импорт сетевого протокола SMTP
from email.mime.text import MIMEText                                 #подключение модуля email.mime и его подсклассов
from email.mime.multipart import MIMEMultipart                       
from email.mime.application import MIMEApplication


def send_email(message):                                             #создаем инструкию отправки сообщения  
    sender="python@mail.ru"                                          #отправитель и пароль от почты отправителя
    password="12345"
    addressee="python@mail.ru"                                       #получатель

    server = smtplib.SMTP("smtp.mail.ru", 587)                       #доменное имя smpt-сервера и его порт
    server.starttls()                                                #подключение к шифрованию TLS

    try:                                                             #обработка исключений
        server.login(sender, password)                               #логин и пароль отправителя
        msg = MIMEMultipart()                                        #основной объект
        msg["Subject"] = "ВАЖНОЕ СООБЩЕНИЕ ДЛЯ ВАС!"                 #заголовок(тема) письма
        text = MIMEText(message)                                     #создание объекта - сообщения
        msg.attach(text)                                             #прикрепление к основному объекту
        
        file = MIMEApplication(open('image.jpg', 'rb').read())       #обработка, открытие и чтение изображения по байтам
        file.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        msg.attach(file)                                             #прикрепление к основному объекту

        server.sendmail(sender, addressee, msg.as_string())          #отправка сообщений

        return "Сообщение отправлено"                                #возврат сообщения в случае успешной отправки  
    except Exception as _ex:                                         #обработка ошибок и возврат сообщения об ошибке
        return f"{_ex}\nНеверный логин или пароль."


def main():                                                           
    message = input("Введите сообщение: ")                           #ввод сообщения
    print(send_email(message=message))                               #передача введенного сообщения 


if __name__ == "__main__":                                           #конструкция для контроля скрипта, скрипт выполняется только при его запуске
    main()



