from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . import models


# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if(request.method=='POST'):
        email  = request.POST.get('email')
        password = request.POST.get('psw')      #user
        a = models.User(email=email,password=password)
        a.save()

        temp1 = request.POST.get('district')
        #dist = models.District.objects.filter(id=temp1)
        #dist.save()

        temp2 = request.POST.get('mandal')
        #print(type(temp2),temp2)
        b = models.Mandal.objects.get(name=temp2, district=int(temp1))
        #b.save()

        school_name = request.POST.get('sname') #school
        lat = request.POST.get('lat')
        long = request.POST.get('long')

        a = models.School(name=school_name,mandal=models.Mandal.objects.get(b.id),district=temp1)
        a.save()

        messages.success(request,('Task has been Added Successfully to Your List '))

        return render(request,'home.html')
    else:
        district = models.District.objects.all()
        mandal   = models.Mandal.objects.all()
        context  = {'mandal':mandal,'district':district}
        return render(request,'signup.html',context)

def login(request):
    if(request.method=='POST'):
        email = str(request.POST.get('email'))
        psw = str(request.POST.get('pass'))
        if(email == "loopmanager" and psw == "loopmanager"):
            #return render(request,'loop.html')
            return render(request,'layout.html')
        elif(models.User.objects.filter(email=email,password=psw,approved=True)):
            #obj = models.User.objects.filter(email=email and password=psw)
            request.session['email'] = email
            request.session['psw'] = psw

            print(request.session['email'])
            
            return render(request,'layout.html',context)
        else:
            return render(request,'error.html')

    return render(request,'login.html')
