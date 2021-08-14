from django.shortcuts import render

# Create your views here.
def dolly(request):
    return render(request,'dolly.html')