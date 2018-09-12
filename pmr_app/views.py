from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Rectangle
from . import serializers, forms

# Create your views here.
def home(request):
    context = {
        'site_title': settings.SITE_TITLE,
    }
    if request.user.is_authenticated:
        return render(request, 'pmr_app/app.html')
    else:
        return render(request, 'pmr_app/index.html', context=context)

def user_login(request, sign_up=False):
    if request.method == 'POST':
        if sign_up:
            form = forms.UserSignUpForm(request.POST)
        else:
            form = forms.UserLoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user_username = request.POST['username']
            user_password = request.POST['password']
            if sign_up:
                newUser = User.objects.create_user(username=user_username, password=user_password)

            user = authenticate(request, username=user_username, password=user_password)
            print(user)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/')

    else:
        if sign_up:
            form = forms.UserSignUpForm()
        else:
            form = forms.UserLoginForm()

    return render(request, 'pmr_app/login.html', { 'form': form })

def sign_up(request):
    return user_login(request, sign_up=True)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

# REST API Views
class RectangleListView(generics.ListAPIView):
    serializer_class = serializers.RectangleSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        return (Rectangle.objects.filter(user=user))

class RectangleCreateView(APIView):

    def post(self, request):
        serializer = serializers.RectangleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rectangle_delete_view(request, rectangle_id):
    try:
        rectangle = Rectangle.objects.get(id=rectangle_id)
        rectangle.delete()
        return HttpResponse('Success')
    except:
        return HttpResponse('Failed')
