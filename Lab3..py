c=15
c=c+5
one=[15,25,15,10]
two=[15,15,20,20,20]
three=[25,20]
name1=['н','о','ф','д']
name2=['п','б','а','к','р']
name3=['в','т']
part1=['и']
part2=[]
part3=[]
summa=sum(one)+sum(two)+sum(three)+5 #сумма всего
#print(sum(one)+sum(two)+sum(three)+5)
x = zip(one,name1)
y = zip(two,name2)
z = zip(three,name3)
xs = sorted(x, reverse=True)
ys = sorted(y, reverse=True)
zs = sorted(z, reverse=True)
print(xs,ys,zs)
c1=xs[0][0]+xs[1][0]
c2=ys[0][0]
#print(c1,c2, xs[0][0],xs[1][0])
if c1>c2:
    c+=c1
    part1+=xs[0][1]+xs[1][1]
    #print()
    xs.reverse()
    xs.pop()
    xs.pop()
    xs.reverse()
else:
    c+=c2
    part1+=ys[0][1]+ys[0][1]
    ys.reverse()
    ys.pop()
    ys.reverse()

print(part1)
c2=ys[0][0]+xs[0][0]
c3=zs[0][0]
if c3>c2:
    c+=c3
    part2 += zs[0][1]+zs[0][1]+zs[0][1]
    zs.reverse()
    zs.pop()
    zs.reverse()
else:
    c+=c2
    part2 += ys[0][1]+ys[0][1]+xs[0][1]
    ys.reverse()
    ys.pop()
    ys.reverse()
    xs.reverse()
    xs.pop()
    xs.reverse()
print(part2  )
c2=ys[0][0]+xs[0][0]
c3=zs[0][0]
if c3>c2:
    c+=c3
    part3 += zs[0][1]+zs[0][1]+zs[0][1]
    zs.reverse()
    zs.pop()
    zs.reverse()
else:
    c+=c2
    part3 += ys[0][1]+ys[0][1]+xs[0][1]
    ys.reverse()
    ys.pop()
    ys.reverse()
    xs.reverse()
    xs.pop()
    xs.reverse()
print(part3)
# т.к. сумма того, что взяли == 110, а того, что не взяли == 95, значит
if c>(summa-(c-15)):
    #с сумма того что взяли и 15
    print('TRUE',  c, c-(summa-(c-15)))