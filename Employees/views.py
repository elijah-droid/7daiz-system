from django.shortcuts import render
import plotly.graph_objects as go
from django.utils.timezone import now
from django.db.models import Sum
from datetime import datetime, timedelta
from django.db.models import Q
from Sales.models import Sale
from Printing.models import Printing
from .models import Employee
import plotly.express as px
import plotly.offline as opy
import pandas as pd


def dashboard(request):
    x_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    y_data = []
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    weekly_sales = Sale.objects.filter(Q(Date__date__gte=start_of_week) & Q(Date__date__lte=end_of_week) & Q(branch=request.user.employee.Branch))
    for day in x_data:
        total = weekly_sales.filter(Date__date__week_day=x_data.index(day)+2).aggregate(total=Sum('Money_Collected'))['total']
        if total:
            y_data.append(total)
        else:
            y_data.append(0)
    x_data[x_data.index(now().strftime('%A'))] = 'Today'
    # Create a trace
    trace = go.Scatter(x=x_data, y=y_data, mode='lines', name='Line Chart')

    # Create a layout
    layout = go.Layout(title='Weekly Sales', xaxis=dict(title='Weekdays'), yaxis=dict(title='Earnings'))

    # Create a figure and add trace(s)
    fig = go.Figure(data=[trace], layout=layout)

    # Convert the figure to HTML
    chart_html = fig.to_html(full_html=False)

    x_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    y_data = []
    weekly_printing = Printing.objects.filter(Q(Date__date__gte=start_of_week) & Q(Date__date__lte=end_of_week) & Q(Branch=request.user.employee.Branch))
    for day in x_data:
        total = weekly_printing.filter(Date__date__week_day=x_data.index(day)+2).aggregate(total=Sum('Amount_Paid'))['total']
        if total:
            y_data.append(total)
        else:
            y_data.append(0)
    x_data[x_data.index(now().strftime('%A'))] = 'Today'

    # Create a trace
    trace = go.Bar(x=x_data, y=y_data, name='Bar Chart')

    # Create a layout
    layout = go.Layout(title='Weekly Printing', xaxis=dict(title='Weekdays'), yaxis=dict(title='Weekdays'))

    # Create a figure and add trace(s)
    fig = go.Figure(data=[trace], layout=layout)

    # Convert the figure to HTML
    bar = fig.to_html(full_html=False)
    today_sales = request.user.employee.Branch.Sales.filter(Date__date=now().date(), Refunded=False).aggregate(total=Sum('Money_Collected'))['total']
    context = {
        'chart': chart_html,
        'bar': bar,
        'sales': today_sales
    }
    return render(request, 'employee_dashboard.html', context)


def staff(request):
    employees = Employee.objects.all()
    total_earnings = sum([staff.month_contribution() for staff in employees])

    data = {
        'Staff': [str(staff) for staff in employees],
        'Performance': [(staff.month_contribution()/total_earnings) * 100 for staff in employees]  # Monthly performance scores
    }

    df = pd.DataFrame(data)

    # Create a pie chart using Plotly Express
    fig = px.pie(df, values='Performance', names='Staff', title='Staff Monthly Performance')

    # Convert the plot to HTML
    plot_html = opy.plot(fig, auto_open=False, output_type='div')
    context = {
        'employees': employees,
        'chart': plot_html
    }
    return render(request, 'staff.html', context)