from ftplib import FTP_TLS
import smtplib

def connect():
    ftp = FTP_TLS()
    ftp.debugging = 2
    ftp.connect('адрес', порт)
    ftp.login('логін', 'пароль'
    return ftp

ftp = connect()

dir_lor = ['/LORA/3D1041818007100','/LORA/3D1041818007101','/LORA/3D1041818007102','/LORA/3D1041818007103','/LORA/3D1041818007104','/LORA/3D1041818007105']

warn = 0
ll0 = []
out = []
latest_name = ""
time = []


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
        ufff = list(ll0 [2]) #батарея
        uif = ufff[:4]
        bubu = "".join(uif)

        zaratustra = ll0 [4]
        zaratyt = zaratustra[5:19]
        time.append(zaratyt)

        nouf = list(ll0 [0]) #номер логера
        nouuf = nouf[10:25]
        nocupicupi = "".join(nouuf)
        out.append(nocupicupi)

        if nocupicupi == "3D1041818007100" : #доп пітаніе моста lora-lte
            ururu = list(ll0 [2])
            noururu = ururu[6:10]
            persik = "".join(noururu)
            persik1 = (int(persik) // 3)
            out.insert(1,persik1)

            bubu1 = int(bubu)
            out.append(bubu1)

        else:
            bubu1 = (int(bubu) // 3)
            out.append(bubu1)

    except IndexError :
        if warn == 0:
            out.append("baaaark")
            out.append("baaark")
            out.append("baaark")
        else:
            out.append("cat_boris")
            out.append("mega_cat")

while warn <6 :
    sort(dir_lor[0])
    slist(ll0)
    warn = warn +1
    if warn == 1:
        dir_lor[0] = dir_lor[1]
        ll0 = []
    elif warn == 2:
        dir_lor[0] = dir_lor[2]
        ll0 = []
    elif warn == 3:
        dir_lor[0] = dir_lor[3]
        ll0 = []
    elif warn == 4:
        dir_lor[0] = dir_lor[4]
        ll0 = []
    elif warn == 5:
        dir_lor[0] = dir_lor[5]
        ll0 = []


def rediska (out):
    for i in out :
        match i:
            case '3D1041818007100' :
                print(f'LoRa Bridge: power bank- {out[1]}, LoRa- {out[2]}, -={time[0]}')
            case '3D1041818007101' :
                print(f"DataLoger 1 {out[4]}, -={time[1]}")
            case '3D1041818007102' :
                print(f"DataLoger 2 {out[6]}, -={time[2]}")
            case '3D1041818007103' :
                print(f"DataLoger 3 {out[8]}, -={time[3]}")
            case '3D1041818007104' :
                print(f"DataLoger 4 {out[10]}, -={time[4]}")
            case '3D1041818007105' :
                print(f"DataLoger 5 {out[12]}, -={time[5]}")
            case "baaaark" :
                print("LoRa Bridge EROR")
            case "cat_boris" :
                print("DataLoger EROR")

rediska(out)
