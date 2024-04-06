# views.py

from rest_framework import generics, status,serializers
from rest_framework.response import Response
from .models import Product, Customer, Employee, Sale
from .serializers import ProductSerializer, CustomerSerializer, EmployeeSerializer, SaleSerializer
from django.db.models import Count
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.hashers import make_password

from django.contrib.auth.hashers import check_password
from .models import Employee
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SignupForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            user = None
        print(user)
        print(user.password)
        print(password)

        if user is not None and password == user.password:
            login(request, user)
            return render(request, 'home.html')
        
        return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)
    elif request.method == 'GET':
        signup_form = SignupForm()
        print(signup)
        return render(request, 'signup.html', {'form': signup_form})

    # else:
    #     return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

# views.py

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            # Save the form data to create a new Employee object
            signup_form.save()
            return render(request, 'home.html') 
        else:
            return JsonResponse({'success': False, 'errors': signup_form.errors}, status=400)
    elif request.method == 'GET':
        signup_form = SignupForm()
        print(signup)
        return render(request, 'signup.html', {'form': signup_form})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def home(request):
    return render(request, 'login.html')
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
    print(employee__username)
    total_sales = serializers.IntegerField()

class AnalyticsAPIView(generics.ListAPIView):
    queryset = Sale.objects.values('employee__username').annotate(total_sales=Count('id')).order_by('-total_sales')
    serializer_class = EmployeeSerializer
