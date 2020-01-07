secInHour=60*60;
print('secInHour='+str(secInHour)+'\n');
secInDay=secInHour*24;
print('secInDay='+str(secInDay)+'\n');
countHours1=secInDay/secInHour;
countHours2=secInDay//secInHour;
print(countHours1);
print(countHours2);