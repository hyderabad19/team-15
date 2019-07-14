from django.shortcuts import render
from . import models
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def test(request):
    if(request.method == "POST"):
        date = request.POST.get('date')
        st = request.POST.get('start')
        st = datetime.strptime(st,'%I:%M')
        end = request.POST.get('end')
        end = datetime.strptime(end,'%I:%M')
        qs = models.Report.objects.filter(date=date)
        for i in qs:
            if((datetime.strptime(i.start_time,'%I:%M') < st and datetime.strptime(i.end_time,'%I:%M') > st) or (datetime.strptime(i.start_time,'%I:%M') < end and datetime.strptime(i.end_time,'%I:%M') > end)):
                return HttpResponse('No')
        return HttpResponse('Done')



    else:
        return render(request,'request.html')