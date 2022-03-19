
from django.http import HttpResponse,JsonResponse


from restapi.models import Article
from restapi.serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime



# Create your views here.
@api_view(["POST"])
def login(request):
    if request.method=="GET":
        article=Article.objects.all()
        serializer=ArticleSerializer(article,many=True)
        return Response(serializer.data)
    elif request.method== "POST":
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(["GET","PUT","DELETE"])
def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse('no such article',status=404)
    if request.method =="GET":
        serializer=ArticleSerializer(article)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method =="PUT":
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method =="DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
