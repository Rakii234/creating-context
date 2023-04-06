from django.shortcuts import render

# Create your views here.
def context(request):
    d={'name':'Rakesh'}
    return render(request,'context.html',d)
