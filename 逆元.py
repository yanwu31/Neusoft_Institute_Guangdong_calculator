X = int(input("请输入N："))
Y = int(input("请输入Mod:"))
for i in range(1,100):
    if (X*i)%Y == 1:
        print(str(X) + " 的逆元为：" + str(i))
        # print(i)
        break
        
    # print(i)