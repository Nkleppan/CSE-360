from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from .models import SignUp, Event
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def newUser(request):
    args = {}
    args.update(csrf(request))
    if request.method =='POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=True)
            return render_to_response('user_created_success.html', args)
    args['form'] = SignUpForm()
    return render_to_response('signup.html', args)
    
    
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('home.html',c)




def auth_view(request):
    args = {}
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    profilePic = request.POST.get('profilePic','')
    args['username'] = username
    args['profilePic'] = profilePic
    user = auth.authenticate(username=username, password=password)
    events = Event.objects.all()
    args['events'] = events
    
    if user is not None:
        auth.login(request, user)
        return render_to_response('ticket_lists.html', args)
    else:
        return HttpResponse("<html><body>Invalid</body></html>")
    
    
def user_created_success_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('user_created_success.html',c)
    
            
    
    
def ticket_list(request):
#    template_name = 'ticket_lists.html'
 #   context_object_name = 'ticket_list'

    #add filter to remove previously purchased tickets from list
 #   def get_queryset(self):
 #       return ticket.objects
    username=request.user.username

    return render_to_response('ticket_list.html',context_instance=RequestContext(request))

def invalid(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')