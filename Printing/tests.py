from django.test import TestCase, Client
from django.urls import reverse
import random
from django.contrib.auth.models import User
from Papers.models import Paper
from Products.models import Product
from Stock.models import Stock
from .forms import PrintingForm
from Employees.models import Employee
from Branches.models import Branch
from django.contrib.auth.hashers import make_password
from .models import Printing
from django.utils.timezone import now

class PrintingTests(TestCase):

    def setUp(self):
        self.branch = Branch.objects.create(
            Name='test-branch',
        )
        user = User.objects.create(
            first_name='test1',
            last_name='test2',
            username='testuser',
            email='test1@gmail.com',
            password=make_password('testpassword')
        )
        self.employee = Employee.objects.create(
            user=user,
            Branch=self.branch
        )
        self.branch.Cashier = self.employee
        self.branch.save()
        self.Product = Product.objects.create(
            Name='Artboard',
            Price=200
        )
        self.stock = Stock.objects.create(
            Branch=self.branch,
            Product=self.Product,
            Quantity=500,
            Price=200
        )
        self.Product.Stock.add(self.stock)
        self.paper = Paper.objects.create(
            product=self.Product,
            format='Any',
            Price=500,
        )
        self.client = Client()

    def test_registerprint(self):
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)
        post = self.client.post(reverse('register-print'), {'Paper': self.paper.id, 'No_of_Papers': 200, 'Amount_Paid': 3000})
        self.assertEqual(post.status_code, 302)
        left_stock = self.paper.product.Stock.all()[0].Quantity
        self.assertEqual(left_stock, 300)
        

    def test_printspage(self):
        print1 = Printing.objects.create(
            Branch=self.branch,
            Paper=self.paper,
            No_of_Papers=100,
            Amount_Paid=1000
        )
        print2 = Printing.objects.create(
            Branch=self.branch,
            Paper=self.paper,
            No_of_Papers=200,
            Amount_Paid=1000
        )
        self.branch.Printing.set([print1, print2])
        login = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(login)
        get = self.client.get(reverse("printing"))
        prints = get.context['printing'].count()
        self.assertEqual(prints, 2)


        