from ftplib import FTP_TLS

#добавити чек часу.
def connect():
    ftp = FTP_TLS()
    ftp.debugging = 2
    ftp.connect('адрес', порт)
    ftp.login('логін', 'пароль')
    return ftp

ftp = connect()

warn = 0

l0 = '/LORA/3D1041818007100'
l1 = '/LORA/3D1041818007101'
l2 = '/LORA/3D1041818007102'
l3 = '/LORA/3D1041818007103'
l4 = '/LORA/3D1041818007104'
l5 = '/LORA/3D1041818007105'


def lori (stat):
    match stat:
        case 0 :
            return '/LORA/3D1041818007100'
        case 1 :
            return '/LORA/3D1041818007101'
        case 2 :
            return '/LORA/3D1041818007102'
        case 3 :
            return '/LORA/3D1041818007103'
        case 4:
            return '/LORA/3D1041818007104'
        case 5:
            return '/LORA/3D1041818007105'

ll0 = []

out = []

latest_name = ""

apii = []


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
    ufff = list(ll0 [2]) #батарея
    uif = ufff[:4]
    bubu = "".join(uif)

    nouf = list(ll0 [0]) #номер логера
    nouuf = nouf[10:25]
    nocupicupi = "".join(nouuf)
    out.append(nocupicupi)

    if nocupicupi == "3D1041818007100" : #доп пітаніе моста lora-lte
        ururu = list(ll0 [2])
        noururu = ururu[6:11]
        persik = "".join(noururu)
        persik1 = (int(persik) // 3)
        out.insert(1,persik1)

        bubu1 = int(bubu)
        out.append(bubu1)

    else:
        bubu1 = (int(bubu) // 3)
        out.append(bubu1)


while warn <6 :
    sort(l0)
    slist(ll0)
    warn = warn +1
    if warn == 1:
        l0 = l1
        ll0 = []
    elif warn == 2:
        l0 = l2
        ll0 = []
    elif warn == 3:
        l0 = l3
        ll0 = []
    elif warn == 4:
        l0 = l4
        ll0 = []
    elif warn == 5:
        l0 = l5
        ll0 = []
    else: print(out)


#def battaru
