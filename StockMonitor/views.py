from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, Stock
from .serializers import UserSerializer, StockSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class StockViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Stock.objects.all().order_by('-id')
    serializer_class = StockSerializer


