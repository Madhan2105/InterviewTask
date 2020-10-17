from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View 
from .forms import  FilterForm
from .models import LeadModel,FollowUpModel
# Create your views here.
class FilterView(View):
    def get(self,request):
        context = {}
        context['form'] = FilterForm()
        return render(request,"index.html",context)
        # return HttpResponse("hey")
    def post(self,request):
        print("inide post")
        print(request.POST)
        headers = request.POST
        print(request.POST['start_date'])
        # print(request.POST.getlist('contact_person_name'))
        date_range = [request.POST['start_date'],request.POST['end_date']]
        data = FollowUpModel.objects.filter(follow_up_date__range=date_range)
        # print(data.follow_up_date)
        context = {}
        context['data'] = data
        context['columns'] = request.POST
        return render(request,"lead.html",context)