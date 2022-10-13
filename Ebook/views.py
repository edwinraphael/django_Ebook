from django.shortcuts import render
from Ebook.serializers import UserSerializer,GenreSerializer,BookSerializer,ReviewSerializer
from Ebook.models import Genre,Books
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions,authentication

# Create your views here.
class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class GenreView(ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=GenreSerializer
    queryset = Genre.objects.all()

    @action(methods=["POST"],detail=True)
    def add_books(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        genre=Genre.objects.get(id=id)
        user=request.user
        serializer=BookSerializer(data=request.data,context={"user":user,"genre":genre})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    @action(methods=["GET"],detail=True)
    def get_books(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        genre=Genre.objects.get(id=id)
        books=genre.books_set.all()
        serializer=BookSerializer(books,many=True)
        return Response(data=serializer.data)
class BookView(ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=BookSerializer
    queryset = Books.objects.all()

    def list(self, request):



        genre_name = request.GET.get("genres",None)
        print(genre_name)
        if genre_name:

            genre = Genre.objects.get(genre_name=genre_name)
            self.queryset = self.queryset.filter(genre=genre)

        return super(BookView,self).list(request)

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book_name=Books.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"book_name":book_name})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)














