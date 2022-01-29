from django.shortcuts import render

# Create your views here.
def Edu(request):
    edu_context={
        'title':'Skill',
        'data':'My Edu page for Edu app',
        'edu':'active',

    }
    return render(request, 'edu/edu.html',context=edu_context)