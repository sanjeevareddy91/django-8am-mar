from django.shortcuts import render
from django.http import HttpResponse
from .models import Team_Name
# Create your views here.

def hello_world(request):
    return HttpResponse("Welcome to Django")

def first_html(request):
    return render(request,'first.html')

def first_form(request):
    return render(request,'first_form.html')


def add_team(request):
    if request.method == "POST":
        team_name = request.POST['team_name']
        nick_name = request.POST['nick_name']
        captain_name = request.POST['captain_name']
        started_year = request.POST['started_year']
        team_logo = request.FILES['team_logo']
        Team_Name.objects.create(team_name=team_name,nick_name=nick_name,captain_name=captain_name,started_year=started_year,team_logo=team_logo)
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
        team_name = request.POST['team_name']
        nick_name = request.POST['nick_name']
        captain_name = request.POST['captain_name']
        started_year = request.POST['started_year']
        team_logo = request.FILES['team_logo']
        data.team_name = team_name
        data.nick_name = nick_name
        data.captain_name = captain_name
        data.started_year = started_year
        data.team_logo = team_logo
        data.save()
        return HttpResponse("Team Details Updated")
    return render(request,'update_team.html',{'data':data})

def delete_team(request,id):
    # data = Team_Name.objects.get(id=id)
    # data.delete()
    Team_Name.objects.get(id=id).delete()
    return HttpResponse("Team Deleted ")