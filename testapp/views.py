from django.shortcuts import render

# Create your views here.
def blue_print(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request,'blue_print.html',context)

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

