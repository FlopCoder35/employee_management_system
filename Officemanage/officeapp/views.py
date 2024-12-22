from django.shortcuts import render,HttpResponse,redirect
from .models import Member,role,department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_member(request):
   mems=Member.objects.all()
   context={
      'mems':mems 
    }
  
   return render(request,'all_member.html',context)
@login_required(login_url='login')
def add_member(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        dept=request.POST['dept']
        role=request.POST['role']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        newmem=Member(firstname=firstname,lastname=lastname,dept_id=dept,role_id=role,phone=phone,salary=salary,bonus=bonus,hire_date=datetime.now())
        newmem.save()
        return HttpResponse('Member Added Successfuly ')
    elif request.method=='GET':
          return render(request,'add_member.html')
    else:
        return HttpResponse('An Exception Occured ')
@login_required(login_url='login')  
def remove_member(request ,mem_id=0):
    if mem_id:
        try:
            to_be_removed=Member.objects.get(id=mem_id)
            to_be_removed.delete()
            return HttpResponse('Member removed successfuly ')
        except:
            return HttpResponse('Enter a valid id ')    

    mems=Member.objects.all()
    context={
      'mems':mems 
    }
    return render(request,'remove_member.html',context)
def filter_member(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        dept=request.POST['dept']
        role=request.POST['role']
        mems=Member.objects.all()
        if firstname:
            mems=mems.filter(Q(firstname__icontains=firstname))
        if lastname:
            mems=mems.filter(Q(lastname__icontains=lastname))
        if dept:
            mems=mems.filter(dept__name__icontains=dept)
        if role:
             mems=mems.filter(role__name__icontains=role)
        context={
            'mems':mems
        }  
        return  render(request,'all_member.html',context)
    elif request.method=='GET':
          return render(request,'filter_member.html')
    else:
        return HttpResponse('Error')
    
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('index')  # Redirect to any page
        else:
            return HttpResponse('Invalid credentials or not a superuser')
    return render(request, 'login.html')
def custom_logout(request):
    logout(request)
    return redirect('login') 