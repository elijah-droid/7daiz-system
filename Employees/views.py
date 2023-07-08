from django.shortcuts import render
import plotly.graph_objects as go
from django.utils.timezone import now
from django.db.models import Sum


def dashboard(request):
    x_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    y_data = [10000, 250000, 300000, 200000, 120000]

    # Create a trace
    trace = go.Scatter(x=x_data, y=y_data, mode='lines', name='Line Chart')

    # Create a layout
    layout = go.Layout(title='Weekly Sales', xaxis=dict(title='Weekdays'), yaxis=dict(title='Earnings'))

    # Create a figure and add trace(s)
    fig = go.Figure(data=[trace], layout=layout)

    # Convert the figure to HTML
    chart_html = fig.to_html(full_html=False)

    x_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    y_data = [400000, 500000, 350000, 270000, 350000]

    # Create a trace
    trace = go.Bar(x=x_data, y=y_data, name='Bar Chart')

    # Create a layout
    layout = go.Layout(title='Printing', xaxis=dict(title='Earnings'), yaxis=dict(title='Weekdays'))

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
