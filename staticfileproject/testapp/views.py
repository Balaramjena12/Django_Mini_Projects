from django.shortcuts import render

# Create your views here.
def result_view(request):
    subjects = {'s1':'Python','s2':'Django','s3':'REST_API','s4':'Numpy','s5':'Pandas','s6':'Matplotlib'}
    return render(request,'testapp/results.html',subjects)
