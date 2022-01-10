Frist = input("请输入明文：")
Second = input("请输入密钥：")
Third = []
Z = 0
while Z < len(Frist):
    X = int(Frist[Z])+int(Second[Z%len(Second)])
    if X == 1:
        Third.append(X)
    elif X == 0:
        Third.append(X)
    else:
        Third.append(0)
    Z += 1
print(Third)