from django.shortcuts import render

# Create your views here.
def Contact(request):
    contact_context={
        "title":"contact",
        'data':'Contact page',
        'contact':'active',

    }
    return render(request, 'contact.html',context=contact_context)

