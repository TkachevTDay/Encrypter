import handler


def main():
    handler.keyInit()
    forEncryption = input()
    handler.encryptC(forEncryption)


if __name__ == '__main__':
    main()
