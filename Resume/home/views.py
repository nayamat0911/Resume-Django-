from django.shortcuts import render

# Create your views here.
def Home_page(request):
    home_context={
        'title':'Home',
        'data':'My Home page for resume',
        'home':'active',
    }
    return render(request, 'home/home.html',context=home_context)