k = int(input('Enter value:'))
if(k<10):
    print('21'+':'+'0'+str(k))
elif(k<60):
    print('21'+':'+str(k))
elif(k<70):
    print('22'+':'+'0'+str(k-60))
elif(k<=100):
    print('22'+':'+str(k-60))
