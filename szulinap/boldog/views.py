from django.shortcuts import render
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'boldog/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # Check to see  form is valid
        if user_form.is_valid():

            user = user_form.save()  # Save User Form to Databas
            user.set_password(user.password)  # Hash the password
            user.save()  # Update with Hashed password
            registered = True  # Registration Successful!

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'boldog/register.html',
                  {'user_form': user_form,
                   'registered': registered,
                   })




def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('boldog:welcome'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'boldog/login.html', {})


@login_required
def welcome(request):
    usern = request.user.username


    return render(request, 'boldog/welcome.html', {'username':usern})





@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'boldog/login.html')

@login_required
def ajandek(request):
    usern = request.user.username
    return render(request, 'boldog/ajandek.html',{'username':usern})

def by(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'boldog/by.html')