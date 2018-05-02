from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models
from . import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authentication import TokenAuthentication
# Create your views here

class HelloApiView(APIView):
	serilizer_class=serializers.HelloSerializer

	def get(self,request,format=None):
		an_apiview=[

		]
		return Response({'message':'Hello','an_apiview':an_apiview})
	def post(self,request):
		serializer=serializers.HelloSerializer(data=request.data)

		if(serializer.is_valid()):
			name=serializer.data.get('name')
			message='Hello '+name
			return Response({'message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_404_BAD_REQUESTS)


class HelloViewSet(viewsets.ViewSet):
	serializer=serializers.HelloSerializer
	def list(self,request):
		a_viewset=[]

		return Response({'message':'Hello','a_viewset':a_viewset})
	def create(self,request):
		serializer=serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name=serializer.data.get('name')
			message='Hello '+name
			return Response({'message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_404_BAD_REQUESTS)
	def retrieve(self,request,pk=None):
		return Response({'http_method':'get'})

class UserProfileViewSet(viewsets.ModelViewSet):
	serializer_class=serializers.UserProfileSerializer
	queryset=models.UserProfile.objects.all()
	# authentication_classes=(TokenAuthentication,)
	# permission_classes=(permissions.UpdateOwnProfile,)
class LoginViewSet(viewsets.ViewSet):
	serializer_class=AuthTokenSerializer

	def create(self,request):
		return ObtainAuthToken().post(request)
		