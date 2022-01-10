def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while a % b != 0:
        temp = b
        b = a % b
        a = temp
        return b
def main():
    # Z = int(input("请输入模X：（获取简化剩余系）"))
    # Z1 = []
    # for i in range(Z):
    #     Z1.append(i)
    # Z2 = []
    # Z2.append(1)
    # for i in range(1,Z):
    #     if gcd(Z, Z1[i]) == 1:
    #         Z2.append(Z1[i])
    # print("完全剩余系：" + str(Z1))
    # print("简化剩余系：" + str(Z2))
    a = 15
    b = 4
    if gcd(a, b) == 1:
        print('互质')
    else:
        print('不互质')
main()
