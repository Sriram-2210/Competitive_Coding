K = int(input('Enter input btw 0-100:'))
time_min = 0
time_hr = 21
if 0<=K<10:
    time_min +=K
    time = (str(time_hr)+':'+'0'+ str(time_min))
    print('The time is ' + '' + time)
elif 10<=K<60:
    time_min +=K
    time = (str(time_hr)+':'+ str(time_min))
    print('The time is ' + '' + time)
elif K == 60:
    time = ('22:00')
    print('The time is ' + '' + time)
elif 60<K<70:
    time_min +=K-60
    time_hr += 1
    time = (str(time_hr)+':'+ '0'+ str(time_min))
    print('The time is ' + '' + time)
elif 70<=K<100:
    time_min +=K-60
    time_hr += 1
    time = (str(time_hr)+':'+ str(time_min))
    print('The time is ' + '' + time)
elif K ==100:
    time = ('22:40')
    print('The time is ' + '' + time)
else:
    print('Invalid Number, Choose btw 0-100')
