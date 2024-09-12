from django.shortcuts import render
from rest_framework import decorators, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerilizer
# Create your views here.
class create_blog(APIView):
    def post(self, request):
        data = request.data
        serilizer = PostSerilizer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

class update_blog(APIView):
    pass

class delete_blog(APIView):
    pass

class get_blog(APIView):
    pass

class get_all_blog(APIView):
    pass