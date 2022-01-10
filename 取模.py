while 1:
    X = int(input("请输入被除数："))
    Y = int(input("请输入取模数："))
    # print("商为： " + str((51-(51%Y))/Y))
    # print("余数为： " + str(X-(X%Y)))
    print("取模为：" + str(X%Y))
    print("商为： " + str((51-(51%Y))/Y))
