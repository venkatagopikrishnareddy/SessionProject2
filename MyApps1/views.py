from django.shortcuts import render
# Create your views here.
#session-apllication-1
def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'MyApps1/pagecount.html',{'count':newcount})
#session-Appliation-2
from django.shortcuts import render
from MyApps1.forms import *
def name_view(request):
    formobj1=NameForm();
    return render(request,'MyApps1/name2.html',{'formobj1':formobj1})
def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    formobj2=AgeForm();
    return render(request,'MyApps1/age2.html',{'formobj2':formobj2})
def parrent_view(request):
    age=request.GET['age']
    request.session['age']=age
    formobj3=ParentForm()
    return render(request,'MyApps1/parent2.html',{'formobj3':formobj3})
def result_view(request):
    parent=request.GET['parent']
    request.session['parent']=parent
    return render(request,'MyApps1/results.html');
#Session-Application-3
from django.shortcuts import render
from MyApps1.forms import *
def add_item_view(request):
    formobj=AdditemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(30)
    return render(request,'MyApps1/additem2.html',{'formobj':formobj})
def display_items_views(request):
    return render(request,'MyApps1/displayitems.html')