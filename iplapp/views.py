from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Team_Name,UserInfo
from .forms import TeamModelForm,TeamNormalForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
import random

from django.views import View

from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# from django.contrib.auth import set_password

# Create your views here.

def hello_world(request):
    return HttpResponse("Welcome to Django")

def first_html(request):
    return render(request,'first.html')

def first_form(request):
    return render(request,'first_form.html')


def add_team(request):
    if request.method == "POST":
        ## 1st Way
        # team_name = request.POST['team_name']
        # nick_name = request.POST['nick_name']
        # captain_name = request.POST['captain_name']
        # started_year = request.POST['started_year']
        # team_logo = request.FILES['team_logo']
        # Team_Name.objects.create(team_name=team_name,nick_name=nick_name,captain_name=captain_name,started_year=started_year,team_logo=team_logo)

        ### 2nd way
        data = request.POST
        data = {ele:value for ele,value in data.items() if ele != 'csrfmiddlewaretoken'}
        data['team_logo'] = request.FILES['team_logo']
        Team_Name.objects.create(**data)
        return HttpResponse("Team Saved")
    return render(request,'add_team.html')

def list_team(request):
    data = Team_Name.objects.all()
    return render(request,'list_team.html',{'data':data})

def single_team(request,id):
    data = Team_Name.objects.get(id=id)
    return render(request,'single_team.html',{'data':data})

def update_team(request,id):
    data = Team_Name.objects.get(id=id)
    if request.method == "POST":
        ## 1st Way
        # team_name = request.POST['team_name']
        # nick_name = request.POST['nick_name']
        # captain_name = request.POST['captain_name']
        # started_year = request.POST['started_year']
        # team_logo = request.FILES['team_logo']
        # data.team_name = team_name
        # data.nick_name = nick_name
        # data.captain_name = captain_name
        # data.started_year = started_year
        # data.team_logo = team_logo
        # data.save()

        ## 2nd Way
        data = request.POST
        data = {ele:value for ele,value in data.items() if ele != 'csrfmiddlewaretoken'}
        data['team_logo'] = request.FILES['team_logo']
        Team_Name.objects.filter(id=id).update(**data)
        messages.success(request,'Team Updated Successfully')
        return redirect('list_team')
    return render(request,'update_team.html',{'data':data})

def delete_team(request,id):
    # data = Team_Name.objects.get(id=id)
    # data.delete()
    Team_Name.objects.get(id=id).delete()
    messages.success(request,"Team Deleted")
    return redirect('list_team')

# Forms are divided in 3 types in django:
    # HTML FORM - where everyhting is done by the user..
    # Model FORM - Where displaying the form html and saving the data is done internal by django..
    # Normal FORM - Where displaying the form html and saving the data is done internal by django..

def model_add_team(request):
    form = TeamModelForm()
    if request.method == "POST":
        form = TeamModelForm(request.POST,request.FILES)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request,'Team Added Successfully')
        return redirect('list_team')
    return render(request,'model_add_team.html',{'form':form})

def normal_add_team(request):
    form = TeamNormalForm()
    if request.method == "POST":
        form = TeamNormalForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form)
            # print(form.data)
            # print(form.cleaned_data)
            data = form.cleaned_data
            print(data)
            print(request.FILES['team_logo'])
            saved_team = Team_Name.objects.create(**data)
            saved_team.team_logo = request.FILES['team_logo']
            saved_team.save()
            return redirect('list_team')
            # print(dir(form))
    return render(request,'normal_add_team.html',{'form':form})


def register_user(request):
    if request.method == "POST":
        data = request.POST
        data = {ele:value for ele,value in data.items() if ele != 'csrfmiddlewaretoken'}
        print(data)
        user_data = User.objects.create(username=data['username'],email=data['email'],is_staff=True)
        user_data.set_password(data['password'])
        user_data.save()
        UserInfo.objects.create(user_data=user_data,mobile_no=data['mobile'])
        send_mail('Confirmation EMail','Hi You have successfully registered in IPLProject Application','gsanjeevreddy91@gmail.com',[data['email']])
        messages.success(request,'User Added!')
        # return HttpResponse("Team Saved")
    return render(request,'register_user.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_info = authenticate(username=username,password=password)
        print(user_info)
        if user_info:
            login(request,user_info)
            messages.success(request,f'{user_info} logged in successfully')
            return redirect('list_team')
        else:
            messages.error(request,"username and password mismatch")
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,"Logged Out!")
    return redirect('login_user')

def forgot_password_email_check(request):
    if request.method == "POST":
        email = request.POST['email']
        email_check = User.objects.filter(email=email)
        if email_check:
            otp = random.randint(100000,999999)
            user_info = UserInfo.objects.get(user_data=email_check.first())
            user_info.verify_code = otp 
            user_info.save()
            message = f"""Please you the below otp for your password change action \n
            OTP : {otp}"""
            send_mail('Password Change Verification Code',message,'gsanjeevreddy91@gmail.com',[email])
            messages.success(request,"OTP has been sent to registered email")
            return redirect('verify_otp')
        else:
            messages.error(request,"User with this email doesnot exist!")
    return render(request,'forgot_password_email_check.html')


def verify_otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        check = UserInfo.objects.filter(verify_code=otp)
        if check:
            # print(check)
            user_id = check.first().user_data.id
            # import pdb;pdb.set_trace()
            messages.success(request,"OTP verified successfully")
            return redirect('change_password',user_id)
        else:
            messages.error(request,"OTP Mismatched,please check it clearly")
    return render(request,'otp_verification.html')


def change_password(request,pk):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request,"Entered password mismatch")
        else:
            user_data = User.objects.get(id=pk)
            user_data.set_password(password)
            user_data.save()
            messages.success(request,"Password Changed successfully")
            return redirect('login_user')
    return render(request,'change_password.html')


# Class based Views 

class HelloCBV(View):
    def get(self,request):
        return HttpResponse("Hello World")

class RegisterTeamCBV(CreateView):
    model = Team_Name
    fields = "__all__"
    success_url = reverse_lazy('list_team')


class ListTeamCBV(ListView):
    model = Team_Name

class UpdateTeamCBV(UpdateView):
    model = Team_Name
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_team')

class DetailTeamCBV(DetailView):
    model = Team_Name


# Django rest framework Topics

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def hello_api(request):
    if request.method == "GET":
        return Response({
            'message' : "Hello World"
        })
    else:
        try:
            name = request.data['name']
            message = f"Hi {name},Very Gud mrng"
        except:
            message = ""
        return Response({
            'message' : message
        })

@api_view(['GET','POST'])
def team_name_api(request):
    if request.method == "GET":
        all_data = Team_Name.objects.all()
        data = []
        # import pdb;pdb.set_trace()

        # Method1
        # for ele in all_data:
        #     dict1 = {}
        #     dict1['team_name'] = ele.team_name
        #     dict1['nick_name'] = ele.nick_name
        #     dict1['team_logo'] = ele.team_logo.url
        #     dict1['captain_name'] = ele.captain_name
        #     dict1['started_year'] = ele.started_year
        #     data.append(dict1)
        # import pdb;pdb.set_trace()

        # Method2
        converted_data = all_data.values()
        print(converted_data)
        for ele in converted_data:
            data.append(ele)
        print(all_data)
        return Response({
            'teams' : data 
        })
    elif request.method == "POST":
        data = request.data
        data = {ele:value for ele,value in data.items()}
        print(request.data)
        obj_data = Team_Name.objects.create(**data)
        data['team_logo'] = obj_data.team_logo.url
        # import pdb;pdb.set_trace()
        return Response({
            "message":"Team created successfully!",
            'team':data
        })

# Class Based APIVIEW.

    # APIVIew
    # Generic APIview
    # Viewsets
from rest_framework.views import APIView
from .serializers import TeamNameSerializer
class TeamNameAPIView(APIView):

    def get(self,request):
        data = Team_Name.objects.all()
        serializer = TeamNameSerializer(data,many=True)
        return Response({
            'Teams':serializer.data
        })

    def post(self,request):
        serializer = TeamNameSerializer(data=request.data)
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            data = serializer.save()
            # import pdb;pdb.set_trace()
            serializer.data['team_logo'] = data.team_logo.url
            return Response({
                "message" : "Team Added",
                "Team" : serializer.data
            })
        return Response({
            "message":"Data is not valid"
        })

class TeamNameDetailAPIView(APIView):

    def get(self,request,id):
        get_data = Team_Name.objects.get(id=id)
        serializer = TeamNameSerializer(get_data)
        return Response({
            "Team":serializer.data
        })

    def put(self,request,id):
        get_data = Team_Name.objects.get(id=id)
        serializer = TeamNameSerializer(get_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message":"Team Details Updated"
            })
        return Response({
            "message" : "Invalid data"
        })

    def delete(self,request,id):
        get_data = Team_Name.objects.get(id=id)
        get_data.delete()
        return Response({
            "message":"Team Deleted"
        })


# Generic APIview 


# get - list
# post - create
# put - update
# delete - destroy
# get - retrieve

from rest_framework import generics
class TeamNameCreateListAPIView(generics.ListCreateAPIView):
    queryset = Team_Name.objects.all()
    serializer_class = TeamNameSerializer

    def list(self,request):
        return Response({
            "message":"Team List API"
        })
    
    # def create()