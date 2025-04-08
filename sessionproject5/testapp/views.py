from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print(request.COOKIES)
    count = request.session.get('count',0)
    count += 1
    request.session.set_expiry(60)
    request.session['count'] = count
    #print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'testapp/pagecount.html',{'count':count})
