from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, redirect, render
from requests import post
from registry.models import Profile,Report
from registry.forms import ProfileModelForm,ReportModelForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .permissions import IsAdminOrReadOnly
from django.http import JsonResponse
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
# def my_profile_view(request):
#     profile = Profile.objects.get(user = request.user)
#     reports = Report.objects.filter(author=request.user).order_by('-created')
#     form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)
#     r_form = ReportModelForm(request.POST or None,request.FILES or None)

#     comfirm = False
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             comfirm = True

            
#     if r_form.is_valid():
#         instance = r_form.save(commit=False)
#         instance.author = request.user
#         instance.save()
#         return redirect('home')
#     r_form = ReportModelForm()            
#     context = {
#         'profile':profile,
#         'form':form,
#         'confirm':confirm,
#         'reports':reports,
#         'r_form':r_form,


#     }
#     return render(request,'profiles/myprofiles.html',context)
def profile(request):
    return render(request,'profiles/myprofiles.html')

def home(request):
    reports = Report.objects.all()
    date = dt.date.today()

    context = {
        'reports':reports,
        'date':date
    }

    return render(request,'reports/home.html',context)

def search_results(request):

    if 'report' in request.GET and request.GET["report"]:
        search_term = request.GET.get("report")
        searched_articles = Report.search_by_report_name(search_term)
        message = f"{search_term}"
        context = {"message":message,
        "reports": searched_articles}

        return render(request, 'reports/search.html',context)
    else:
        message = "no reports found"
        context = {
            'message':message
        }
        return render(request, 'reports/home.html',context)  


def delete_project(request,pk): 
    report = Report.objects.get(pk = pk)
    if request.method == 'POST':
        report.delete()

        # return redirect('reports/home.html')

    return render(request, 'reports/delete_report.html',{})        


def update_project(request,pk):
    report = Report.objects.get(id = pk)
    form = ReportModelForm(instance = post)
    if request.method == 'POST':
        form = ReportModelForm(request.POST, request.FILES ,instance = post)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            report.save()
            # return redirect('reports/home.html',pk = pk )
   
    return render(request, 'reports/update_report.html',{'form' :form})


class ReportList(APIView):
    def get(self, request, format=None):
        allreports = Report.objects.all()
        serializers = ReportSerializer(allreports, many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ReportSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileList(APIView):
    def get(self, request, format=None):
        allprofiles = Profile.objects.all()
        serializers = ProfileSerializer(allprofiles, many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
