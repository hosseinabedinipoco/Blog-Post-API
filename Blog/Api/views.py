from django.shortcuts import render
from rest_framework import decorators, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerilizer
from django.shortcuts import get_object_or_404
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
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serilizer = PostSerilizer(post, data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class delete_blog(APIView):
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)

class get_blog(APIView):
    pass

class get_all_blog(APIView):
    pass