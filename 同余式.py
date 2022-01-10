# a = int(input())
# print(divmod(a,9))
print("公式 x=b1(mod m1)")
m1=int(input("输入m1:"))
m2=int(input("输入m2:"))
m=m1*m2
M1=m/m1
M2=m/m2
print("m={}".format(m))
n = m1
j = 0
for i in range(2, n):
        a = n
        q = i
        r = a % i
        while r != 1 and r != 0:
            a = int(q)
            q = int(r)
            r = int(a) % int(q)
        """如果互素则计数+1"""
        if r == 1:
            j += 1
        elif r == 0:
            pass
## j=j

M1_dian=(M1**j)%m1
print("M1'={}".format(M1_dian))

##
n = m2
j = 0
for i in range(2, n):
        a = n
        q = i
        r = a % i
        while r != 1 and r != 0:
            a = int(q)
            q = int(r)
            r = int(a) % int(q)
        """如果互素则计数+1"""
        if r == 1:
            j += 1
        elif r == 0:
            pass
## j=j

M2_dian=(M2**j)%m2
print("M2'={}".format(M2_dian))
b1=int(input("输入b1："))
b2=int(input("输入b2："))
sum=(b1*M1*M1_dian+b2*M2*M2_dian)%m

print("X={}(mod{})".format(sum,m))





	
    

