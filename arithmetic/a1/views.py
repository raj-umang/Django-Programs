from django.http import JsonResponse
from django.shortcuts import render
from .forms import ExpressionForm
from sympy import sympify

def evaluate_expression(request):
    # Check if the request is a POST and AJAX request
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ExpressionForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = sympify(expression)
                return JsonResponse({'result': str(result)})
            except Exception as e:
                return JsonResponse({'result': f"Error: {str(e)}"})
        else:
            return JsonResponse({'result': 'Invalid form'})
    else:
        form = ExpressionForm()
        return render(request, 'evaluate_expression.html', {'form': form})