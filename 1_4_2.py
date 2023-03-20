from ftplib import FTP_TLS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def connect():
    ftp = FTP_TLS()
    ftp.debugging = 0
    ftp.connect('адрес', порт)
    ftp.login('логін', 'пароль')
    print('FTP login OK')
    return ftp


smtplib = smtplib.SMTP_SSL('mail', 465)
dir_lor = ['/LORA/3D1041818007100','/LORA/3D1041818007101','/LORA/3D1041818007102','/LORA/3D1041818007103','/LORA/3D1041818007104','/LORA/3D1041818007105']

warn = 0
ll0 = []
out = []
latest_name = ""
timeD = []
message = ""
meg = ""

def milo (message) :
    msg = MIMEMultipart()

     password = "пароль"
    msg['From'] = "від"
    msg['To'] = "кому"
    msg['Subject'] = "not cat"

    msg.attach(MIMEText(message, 'plain'))

    smtplib.login(msg['From'], password)
    smtplib.sendmail(msg['From'], msg['To'], msg.as_string())
    print("\nSend mail ok")
    smtplib.quit()

def sort (l0) :
    entries = list(ftp.mlsd(l0))
    entries.sort(key = lambda entry: entry[1]['modify'], reverse = True)
    latest_name = entries[0][0]

    ftp.cwd(l0)
    ftp.retrbinary(f"RETR {latest_name}", open(latest_name,"wb").write)

    with open(f'{latest_name}',  'r') as fp:
        lines = fp.readlines()
        for line in lines:
            ll0.append(line)


def slist (ll0) :
    try :
        bubu = "".join(list(ll0 [2])[:4]) #батарея

        timeD.append(ll0[4] [5:19]) #час

        nocupicupi = "".join(list(ll0 [0])[10:25]) #номер логера
        out.append(nocupicupi)

        if nocupicupi == "3D1041818007100" : #доп пітаніе моста lora-lte
            out.insert(1,(int("".join(list(ll0 [2]) [6:10])) // 3))
            out.append(int(bubu))
            print("Begin")
        else:
            try:
                out.append(int(bubu) // 3)
                print('uffff')

            except ValueError :
                out.append("cat_boris")

    except IndexError :
        if warn == 0:
            out.append("baaaark")
            out.append("baaark")
            out.append("baaark")
        else:
            out.append("cat_boris")
            #out.append("mega_cat")


def rediska (out):
    global meg
    for i in out :
        match i:
            case '3D1041818007100' :
                meg += f'\nLoRa Bridge: Power bank- {out[1]}, LoRa- {out[2]}, -={timeD[0]}\n'
            case '3D1041818007101' :
                meg += f"DataLoger 1 {out[4]}, -={timeD[1]}\n"
            case '3D1041818007102' :
                meg += f"DataLoger 2 {out[6]}, -={timeD[2]}\n"
            case '3D1041818007103' :
                meg += f"DataLoger 3 {out[8]}, -={timeD[3]}\n"
            case '3D1041818007104' :
                meg += f"DataLoger 4 {out[10]}, -={timeD[4]}\n"
            case '3D1041818007105' :
                meg += f"DataLoger 5 {out[12]}, -={timeD[5]}\n"
            case "baaaark" :
                meg += "LoRa Bridge EROR\n"
            case "cat_boris" :
                meg += "DataLoger EROR\n"


while True:
    global ftp
    now = datetime.datetime.now()

    if now.hour == 12 and now.minute == 10:
        ftp = connect()

        while warn < 6:
            sort(dir_lor[0])
            slist(ll0)
            warn = warn + 1
            if warn < 6:
                dir_lor[0] = dir_lor[warn]
            ll0 = []

        rediska(out)
        meg = meg + '\n' + time.asctime()
        print(meg)
        milo(meg)

        warn = 0
        time.sleep(24 * 60 * 60)
    else:
        time.sleep(60)
