while 1 :
    
    X = int(input("RSA加解密（1 加密 2 解密 3 密钥生成）"))
    if X == 1 :
        m = int(input("请输入明文m："))
        e = int(input("请输入e："))
        n = int(input("请输入n："))
        print("密文 c = " + str(m**e%n))
    elif X == 2:
        c = int(input("请输入密文c："))
        d = int(input("请输入d："))
        n = int(input("请输入n："))
        print("明文 m = " + str(c**d%n))
    else :
        print("公式： e*d = 1 mod p(n)")
        print("p*q = n")
        n = int(input("请输入欧拉（n）[(e,φ(n))=1]："))
        e = int(input("请输入e："))
        d = 0
        for i in range(100):
            if i*e%n == 1:
                d = i
                break
            
        print("d = " + str(d))