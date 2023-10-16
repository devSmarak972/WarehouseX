from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"warehouse/index.html",{})
def inventory(request,id):
    return render(request,"inventory.html",{})
def invoice(request,id):
    return render(request,"invoice.html",{})
def invoicelist(request):
    return render(request,"invoicelist.html",{})
def map(request):
    return render(request,"map.html",{})
def productgrid(request):
    return render(request,"productgrid.html",{})
def productpage(request,id):
    return render(request,"productpage.html",{})
def productslist(request):
    return render(request,"productslist.html",{})
def editproduct(request,id):
    return render(request,"edit-product.html",{})
def orders(request):
    return render(request,"current_order.html",{})
def warehouselist(request):
    return render(request,"warehouselist.html",{})
def login(request):
    return render(request,"login.html",{})
def register(request):
    return render(request,"register.html",{})