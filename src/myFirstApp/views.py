from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import FirstApp
# Create your views here.
class ProductsView(ListView):
    model = FirstApp
    context_object_name = 'querySet'
    template_name='firstApp/index_page.html'
    querySet = FirstApp.objects.all()

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return FirstApp.objects.all()

def productsView_URL(request):
    querySet = FirstApp.objects.all()
    context = querySet
    return render(request,"firstApp/index_page.html",context)

class ProductsDetails(DetailView):
    template_name='firstApp/details.html'
    context_object_name = 'querySet'
    model = FirstApp
    def get_context_data(self,*args,**kwargs):
        context = super(ProductsDetails,self).get_context_data(*args,**kwargs)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        context = FirstApp.objects.get_by_id(pk)
        if context is None:
            return HttpResponse("Item not Found")
        else:
            return context

    # model = FirstApp
    # context_object_name = 'querySet'
    # template_name='firstApp/details.html'
    # pk = 1
    # querySet = get_object_or_404(FirstApp,id=pk)

def productsView_URL(request,pk):
    # --- 1st method ---
    # instance = get_object_or_404(FirstApp,id=pk)
    # context = instance
    # return render(request,"firstApp/details.html",context)

    # --- 2nd method ---
    # qs = FirstApp.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Doesn't exists")
    # return render(request,"firstApp/details.html",{"querySet":instance})

    # --- 3rd Method ---
    #context = FirstApp.objects.get_by_id(pk)
    context = FirstApp.objects.isAvailable()
    if context is None:
        return HttpResponse("Item not with true not Found")
    else:
        return render(request,"firstApp/details.html",{"querySet":context})