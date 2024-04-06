from rest_framework import generics,serializers
from .models import Product, Customer, Employee, Sale
from .serializers import ProductSerializer, CustomerSerializer, EmployeeSerializer, SaleSerializer
from django.db.models import Count
from django.contrib.auth import  login, logout
from django.http import JsonResponse
from .models import Employee
from .models import Employee
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SignupForm


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
class EmployeeSerializer(serializers.Serializer):
    employee__username = serializers.CharField()
    total_sales = serializers.IntegerField()

class AnalyticsAPIView(generics.ListAPIView):
    queryset = Sale.objects.values('employee__username').annotate(total_sales=Count('id')).order_by('-total_sales')
    serializer_class = EmployeeSerializer
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            user = None
        if user is not None and password == user.password:
            login(request, user)
            return render(request, 'home.html')
        
        return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)
    elif request.method == 'GET':
        signup_form = SignupForm()
        return render(request, 'signup.html', {'form': signup_form})
def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            
            signup_form.save()
            return render(request, 'home.html') 
        else:
            return JsonResponse({'success': False, 'errors': signup_form.errors}, status=400)
    elif request.method == 'GET':
        signup_form = SignupForm()
        return render(request, 'signup.html', {'form': signup_form})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def home(request):
    return render(request, 'login.html')
