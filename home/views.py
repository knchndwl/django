from django.shortcuts import render
from .models import *
app_name = 'home'

# Create your views here.
def base():
    view={}
    view['feedbacks']= Feedback.objects.all()
    return view


def home(request):
    view = base()
    return render(request,'index.html',view)



def about(request):
    view = base()
    return render(request,'about.html',view)



def contact(request):
    if request.method== 'POST':
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']

        data= Contact.objects.create(
            name= name,
            email= email,
            subject= subject,
            message= message
        )
        data.save()
        return render(request,'contact.html',{'message':'success'})

    return render(request,'contact.html')



def portfolio(request):

    return render(request,'portfolio.html')



def price(request):

    return render(request,'price.html')



def services(request):
    view = base()
    return render(request,'services.html',view)