while 1:
    print("EIGamal公钥加解密（1：加密 2：解密 3：公钥生成）：")
    print("EIGamal"
        "密钥生成 hA Ξ a^Xa mod p"
        "加密 u Ξ a^k mod p   v Ξ hA^k * m mod p"
        "解密 v u^-Xa Ξ m mod p"
        "(-Xa = p - 1 - Xa)")
    X = input()
    if int(X) == 1 :
        a = input("请输入原根a:")
        k = input("请输入k：")
        hA = input("请输入hA:")
        p = input("请输入素数p：")
        m = input("请输入m：")
        print("密文如下：")
        print("u = " + a + "^" + k + "mod" + p + "  u=" + str(int(a)**int(k)%int(p)))
        print("v = " + hA + "^" + k + "*" + m + "mod" + p + "  v=" + str(int(hA)**int(k)*int(m)%int(p)))
    elif int(X) == 2:
        v = int(input("请输入v："))
        u = int(input("请输入u："))
        Xa = int(input("请输入Xa:"))
        p = int(input("请输入素数p："))
        print("明文m=" + str(v*u**(p-Xa-1)%p))
    else:
        a = input("请输入a：")
        Xa = input("请输入Xa：")
        p = input("请输入素数p：")
        Y = int(a)**int(Xa)
        Y = Y%int(p)
        print("公钥hA = " + str(Y))