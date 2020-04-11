from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        messages.success(request, "You are now logged out.")
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):

    if request.method == 'POST':
        #Getting form fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #validation
        #password check
        if password == password2:
            #username check
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already taken")
                return redirect('register')
            else:
                #email check
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email is already taken")
                    return redirect('register')
                else:
                    #creating user
                    user_details = {
                        'username':username,
                        'first_name':first_name,
                        'last_name': last_name,
                        'email': email,
                        'password': password,
                    }
                    user = User.objects.create_user(**user_details)
                    # #if we directly want to login after registeration
                    # auth.login(request, user)
                    # messages.success(request, "Account Created")
                    # return redirect('index')

                    #if we want to redirect user to login page
                    user.save()
                    messages.success(request, "User created successfully")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'accounts/register.html')
