from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles import serializers
import articles
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method =="GET":
        articles=Article.objects.all()
        Serializer=ArticleSerializer(articles, many=True)
        return Response(Serializer.data)
    elif request.method == "POST":
        Serializer = ArticleSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(Serializer.errors)
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)