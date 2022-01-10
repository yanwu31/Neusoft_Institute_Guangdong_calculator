Frist_one = input("请输入明文(大写加空格)：").split()
Frist_twe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
             'O','P','Q','R','S','T','U','V','W','X','Y','Z']
Frist_tree = input("请输入密钥(大写加空格)：").split()

Second_one = []
Second_twe = []
Second_tree = []
for X in Frist_one:
    flag = 1
    Y = 0
    while (flag):
        if Frist_twe[Y] == X:
            flag = 0
            Second_one.append(Y)
        Y += 1
# print(Second_one)
for X in Frist_tree:

    flag = 1
    Y = 0
    while (flag):
        if Frist_twe[Y] == X:
            flag = 0
            Second_twe.append(Y)
        Y += 1

Z = 0
while Z < len(Frist_one):
    
    Second_one[Z] += Second_twe[Z%len(Second_twe)]
    Second_tree.append(Frist_twe[int(Second_one[Z])%26])
    Z += 1
    
# print(Second_one)
# print(Frist_twe[18])
print(Second_tree)

    

