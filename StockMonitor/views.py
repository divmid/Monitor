
# Create your views here.

from rest_framework.response import Response
from rest_framework import viewsets, views, permissions
from .models import User, Stock
from .serializers import UserSerializer, StockSerializer
from django.contrib import auth
from rest_framework.reverse import reverse
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        print(attrs)
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # Add extra responses here
        data['username'] = self.user.username
        data['user'] = reverse('user-detail', [self.user.id], request=self.context['request'])
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LoginView(views.APIView):
    """
    允许用户查看或编辑的API路径。
    """
    def post(self, request):
        """
        返回最新的图书信息
        """
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # return Response({"code": 200})
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return Response({"code": 20000})
        else:
            # Show an error page
            return Response({"code": 50008})


class LogoutView(views.APIView):

    def post(self, request):
        auth.logout(request)
        # Redirect to a success page.
        return Response({"code": 20000})


class UserView(views.APIView):
    """
    允许用户查看或编辑的API路径。
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)

    # def get(self, request):
    #     """
    #     返回最新的图书信息
    #     """
    #     print(request)
    #     return Response({"code": 50008})


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.JWTAuthentication,)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('-date_joined')
        return User.objects.filter(id=self.request.user.id).order_by('-date_joined')


class StockViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.JWTAuthentication,)

    queryset = Stock.objects.all().order_by('-id')
    serializer_class = StockSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Stock.objects.all().order_by('-id')
        return Stock.objects.filter(user=self.request.user).order_by('-id')

# curl   -X POST   -H "Content-Type: application/json"   -d '{"username": "乔赫", "password": "bupt1234"}'   http://localhost:8000/api/auth/token/obtain/
