from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """ Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request,format=None):
        """Returns a list of API feautures"""
        an_apiview=[
            'Uses HTTP methods as functions(get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request, pk=None):
        """Handle updating/replacing an object """
        return Response({'method':'PUT'})

    def patch(self,request, pk=None):
        """Handle partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self,request, pk=None):
        """Handle deleting an object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ TEST API ViewSet """
    serializer_class =serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message"""
        a_viewset=[
            'User actions (list,crate,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """ Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message= f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,response,pk=None):
        """ Handle gettind an obj by its ID"""
        return Response({'http_method':'GET'})

    def update(seld,request,pk=None):
        """Handle updating an obj"""
        return Response({'http_method':'PUT'})

    def partial_update(seld,request,pk=None):
        """Handle updating a part of an obj"""
        return Response({'http_method':'PATCH'})

    def destroy(seld,request,pk=None):
        """Handle removing an obj"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
