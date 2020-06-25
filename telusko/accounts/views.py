from django.shortcuts import render

# Create your views here.


def register(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']

    return render(request, 'register.html')