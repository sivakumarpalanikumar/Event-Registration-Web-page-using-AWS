from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from myapp.models import formcontact

def form(request):

    if request.method=="POST":
        name=request.POST['name']
        rollno=request.POST['rollno']
        email=request.POST['email']
        phone=request.POST['phone']
        part=request.POST['part']
        dept=request.POST['dept']
        year=request.POST['Year']
        sect=request.POST['sect']
        v1=False
        v2=False
        v3=False
        v4=False
        v5=False
        
        val=request.POST.getlist('tag[]')
        if '1' in val:
            v1 = True
        if '2' in val:
            v2 = True
        if '3' in val:    
            v3 = True
        if '4' in val:    
            v4 = True
        if '5' in val:
            v5 = True
        


        print(name,rollno,email,phone,part,dept,year,sect,v1,v2,v3,v4,v5)
        ins=formcontact(name=name,rollno=rollno,email=email, phone=phone,part=part,dept=dept,year=year,sect=sect,paperpresentation=v1,projectpresentation=v2,quiz=v3,coding=v4,nontechnical=v5)
        ins.save() 
        print("Data saved sucessfully")
    return render(request, 'main.html')
   


