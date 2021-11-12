import config


def keyInit():
    config.key = 5


# noinspection PyCallingNonCallable
def encryptC(forEnc):
    finall = ''
    forEnc.upper()
    for i in forEnc:
        index = config.alphabetUpper.find(i)
        newIndex = index + config.key
        if i in config.alphabetUpper:
            finall = finall + config.alphabetUpper[newIndex]
        else:
            finall = finall + i
    print(finall)
