from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')


def movies_info(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'OG will come very soon.....'
    sub_msg2 = 'planning for Aashiqui-3 with Allu Arjun & Sam'
    sub_msg3 = 'Dont go for movies....pratice django....'
    type ='movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
	'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'IPL will conducted in March'
    sub_msg2 = 'T20 ENG and IND'
    sub_msg3 = 'India won the 3rd t20 with 15 runs yesterday'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
	'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'AP DyCM Pawan Kalyan'
    sub_msg2 = 'India PM was Modi'
    sub_msg3 = 'Upcoming AP CM...........?'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,
	'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
