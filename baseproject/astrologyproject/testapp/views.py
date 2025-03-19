from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    msg_list = [
    'The golden days ahead',
    'better to sleep more time even in class',
    'Tomorrow is the perfect date to propose ur GF',
    'Very soon you will get job'
    ]
    name_list = ['Sunny', 'Mallika','Katrina', 'Kareena', 'Deepika','Samantha']
    time  = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astr.html',my_dict)
