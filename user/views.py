from django.shortcuts import render
from user.models import User, Contact
from user.forms import ContactForm, LoginForm, RegisterForm
from hashlib import md5

# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            #hash the password
            user = User.objects.filter(email = email, password = password)
            context = {'email': email}
            if user:
                context['login_status'] = 'success'
            else:
                context['login_status'] = 'failure'
            return render(request, 'login.html', context)
        else:
            context = {'errors': ['Invalid form!']}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
        

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            telephone = form.cleaned_data['telephone']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']

            user = User(username = username, firstname = firstname, 
                lastname = lastname, email = email, password = password, 
                telephone = telephone, country = country, state = state
            )
            user.save()
            context = {'register_status': 'success'}
        else:
            context = {'register_status': 'failure', 'errors': ['Invalid form!']}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def contact_index(request, **kwargs):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'contact_index.html', context)

def contact_detail(request, contact_id):
    contact_info = Contact.objects.get(pk = contact_id)

    context = {
        'contact': {'username': contact_info.username, 'email': contact_info.email, 'message': contact_info.message, 'brief_message': contact_info.message[:30] + ('...' if len(contact_info.message) > 30 else '')}
    }

    return render(request, 'contact_detail.html', context)