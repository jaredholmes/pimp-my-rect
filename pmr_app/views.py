from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Rectangle
from . import serializers

# Create your views here.
def home(request):
    context = {
        'site_title': settings.SITE_TITLE,
    }
    # if request.user.is_authenticated:
    #     return render(request, 'pmr_app/app.html')
    # else:
    #     return render(request, 'pmr_app/login.html', context=context)
    return render(request, 'pmr_app/app.html')

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

# TODO: Improve returns and error handling
def rectangle_delete_view(request, rectangle_id):
    try:
        rectangle = Rectangle.objects.get(id=rectangle_id)
        rectangle.delete()
        return HttpResponse('Success')
    except:
        return HttpResponse('Failed')
        print(request.errors)
