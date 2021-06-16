def fun(s):
    a=[]
    for i in s:
        a.append(i)
    r=0
    s1=a[r]
    for j in range(1,len(a)):
        if a[j]==a[r]:
            s1=s1+'*'
        else:
            s1=s1+a[j]
            r=j
    print(s1)
s='SRMMMUNIVERSITYYY'
fun(s)
#output : SRM**UNIVERSITY**
