from django.shortcuts import render
from django.views.generic import View
from .models import *


class HomepageView(View):
    def get(self,request):
        department = Department.objects.all()
        context = {"departments":department}

        return render(request,'index.html',context)








