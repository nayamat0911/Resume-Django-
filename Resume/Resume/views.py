

from django.shortcuts import render

# Create your views here.
def base_home(request):
    base_context={
        'title':'Base',
        'data':'My Base page for resume Project'

    }
    return render(request, 'base.html',context=base_context)