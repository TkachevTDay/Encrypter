import config


def keyInit():
    config.key = 3


def transform(forTrans):
    listT = []
    for i in forTrans:
        listT.append(i)
    return listT


def encryptC(forEnc):
    listChar = forEnc.transform()
    print(listChar)
