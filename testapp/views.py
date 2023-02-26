from django.shortcuts import render

# Create your views here.

def name_view(request):

    return render(request,'testapp/home.html')

def age_view(request):
    print(request.COOKIES)
    username = request.GET['name']
    response =  render(request,'testapp/age.html',{'name':username})
    response.set_cookie('name',username)
    return response

def gf_view(request):
    age = request.GET['age']
    username = request.COOKIES.get('name')
    response = render(request,'testapp/gf.html',{'name':username})
    response.set_cookie('age',age)
    return response

def results_view(request):
    username = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    gfname = request.GET['gfname']
    return render(request,'testapp/results.html',{'name':username,'age':age,'gfname':gfname})
