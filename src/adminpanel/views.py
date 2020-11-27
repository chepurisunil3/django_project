from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm
from rest_framework import viewsets
from .serializers import AdminSerializer

def index(request):
    data = Products.objects.availableProducts()
    quantity = Products.objects.quantityFilter(21)
    print(quantity)
    return render(request,"adminpanel/index.html",{'productDetails': data})
    # form = ProductForm
    # return render(request,"admin-index.html",{'form': form})

class rest_api(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Products.objects.all()

def add_product(request):
    if request.method == "POST":
        print("------------")
        print(request.POST)
        postForm = ProductForm(request.POST, request.FILES)
        if postForm.is_valid():
            try:
                postForm.save()
            except:
                return render(request, 'adminpanel/add-product.html', {'form': form, 'status': "success"})
            form = ProductForm
            return render(request, 'adminpanel/add-product.html', {'form': form, 'status': "success"})
    else:
        form = ProductForm
        return render(request,"adminpanel/add-product.html",{'form': form})

def update_quantity(request):
    if request.method == "GET":
        params = request.GET
        if 'quantity' in params and 'id' in params:
            id = params["id"]
            quantity = params["quantity"]
            print(id)
            print(quantity)
            return HttpResponse(id)
        else:
            return HttpResponse("Required")
        # if id != "" & quantity != "":
        #     resp = Products.objects.updateQuantity(id,quantity)
        #     print(resp)
        #     return HttpResponse(resp)
        # else:
        #     return HttpResponse("Empty")

