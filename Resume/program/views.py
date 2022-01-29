

from django.shortcuts import render

# Create your views here.
def Program(request):
    program_context={
        'title':'program',
        'data':'My program page for resume',
        'program':'active',

    }
    return render(request, 'program/program.html',context=program_context)