n,m,x,t,d = map(int, input("Enter values:").split())
# n=nth birthday, m=mth birthday, x=xth birthday, t=total height, d=change of height
if(m>=x):
    print(t)
else:
    print(t-d*x+m)