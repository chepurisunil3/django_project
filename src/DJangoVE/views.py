from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import TestForm
from django.contrib.auth import authenticate,login,get_user_model
User = get_user_model()
def index_page(request):
    testForm = TestForm(request.POST or None)
    if testForm.is_valid():
        print(testForm.cleaned_data)
        username = testForm.cleaned_data.get("username")
        password = testForm.cleaned_data.get("password")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return HttpResponse("Login Success")

    print(request.user.is_authenticated)
    templateData = {
        "form":testForm
    }
    #new_user = User.objects.create_user("sunil","cs@g.c","chepuri","sunil","12345")
    #print(new_user)
    return render(request,"index_page.html",templateData)

def sample_get_request(request):
    if request.method == "GET":
        requestParams = request.GET
        return HttpResponse("Hello")
    else:
        return HttpResponse("Error")