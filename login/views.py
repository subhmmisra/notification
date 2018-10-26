from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from fcm_django.models import FCMDevice
from django.utils.decorators import method_decorator
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
        else:
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


class UsernameValidator(View):
    def get(self, request):
        flag = False
        try:
            user = User.objects.get(username = request.GET['user'])
            flag = True
        except ObjectDoesNotExist:
            flag = False
        return HttpResponse(json.dumps({'result': flag}), content_type="application/json")

class EmailValidator(View):
    def get(self, request):
        flag = False
        try:
            user = User.objects.get(email = request.GET['email'])
            flag = True
        except ObjectDoesNotExist:
            flag = False
        return HttpResponse(json.dumps({'result': flag}), content_type="application/json")


class Home(View):
    def get(self, request):
        devices = FCMDevice.objects.all();
        users=[]
        for i in devices:
            print(User.objects.get(id=i.user_id).id)
            users.append(User.objects.get(id=i.user_id))
        return render(request, 'home.html', {"user": request.user, "users":users})

class AddUserDevice(View):
    def post(self, request):
        bound_form = AddUserDeviceForm(request)
        if bound_form.is_valid():
            bound_form.save()
            return JsonResponse({'Success': "User Created"})
        else:
            return JsonResponse({'Error': "Form Validation Failed"})

class SendNotification(View):
    def get(self, request):
        device = FCMDevice.objects.first()
        device.send_message(title="Greeting", body="hy there, i am shubham")
        return JsonResponse({'Success': "Notification Sent"})
    def post(self, request):
        data = request.POST
        device = FCMDevice.objects.get(user_id=data['user'])
        print(device)
        if data['all']:
            devices = FCMDevice.objects.all()
            print(devices)
            devices.send_message(title=data['title'], body=data['description'], icon=['data.link'])
            return JsonResponse({'sucess':'Notification Sent'})
        device.send_message(title=data.title, body=data.description, icon=data.link)
        return JsonResponse({'Success': "Notification Sent"})
