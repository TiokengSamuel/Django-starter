from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email = email, first_name= firstname, last_name = lastname)
        user.save();
        print('creatied user')
        return redirect('/')

    else: 
         return render(request, 'register.html')

         # One more day without commiting normally :)
    
        # I met nervis nzometia today! Amazing
