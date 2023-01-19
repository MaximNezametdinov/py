f = open('17.txt' , 'r')
sum = 0
count = 0
minel = 10001
mas=[]
for s in f:
    mas.append(int(s))
    a = int(s)
    minel = min(minel , a)
    if a % 4 == 0:
        count += 1
        sum += a
        sred = sum / count
count = 0
maxsum = 0
for i in range(len(mas) -1):
    sum = mas[i] + mas[i + 1]
    if(mas[i] % minel == 0 or mas [i + 1] % minel == 0) and sum < sred:
        count += 1
        maxsum = max(maxsum , mas[i] + mas [i + 1])
print(count , maxsum)
       
    
    
