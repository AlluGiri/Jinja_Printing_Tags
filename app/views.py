from django.shortcuts import render

# Create your views here.

def Login(request):
    data='This data is our assumption'
    d={'assumption':data}
    return render(request,'Login.html',context=d)
