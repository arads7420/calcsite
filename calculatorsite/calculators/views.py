from django.shortcuts import render
from . import calculators as calc
from .forms import MatrixInput2x2
from .forms import MatrixInput3x3



# Create your views here.
base_site_name = 'Calculator Swift'
def calculators(request): 
    context = {
        'title': base_site_name + '| Calculators',
    }
    return render(request, 'calculators.html', context)

def addmatrices2x2(request):
    title = 'Calculators | Add two 2x2 Matrices'
    if request.method == 'POST':
        form = MatrixInput2x2(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12']], [data['a21'], data['a22']]]
            b = [[data['b11'], data['b12']], [data['b21'], data['b22']]]

            result = calc.add2x2matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'addmatrices22.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'addmatrices22.html', context)

    else:
        form = MatrixInput2x2()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'addmatrices22.html', context)

def addmatrices3x3(request):
    title = 'Calculators | Add two 3x3 Matrices'
    if request.method == 'POST':
        form = MatrixInput3x3(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13']], 
                [data['a21'], data['a22'], data['a23']],
                [data['a31'], data['a32'], data['a33']]]

            b = [[data['b11'], data['b12'], data['b13']], 
                [data['b21'], data['b22'], data['b23']],
                [data['b31'], data['b32'], data['b33']]]

            result = calc.add3x3matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'addmatrices33.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'addmatrices33.html', context)

    else:
        form = MatrixInput3x3()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'addmatrices33.html', context)


def multiplymatrices2x2(request):
    title = 'Calculators | Multiply two 2x2 Matrices'
    if request.method == 'POST':
        form = MatrixInput2x2(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12']], [data['a21'], data['a22']]]
            b = [[data['b11'], data['b12']], [data['b21'], data['b22']]]

            result = calc.multiply2x2matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'multiplymatrices22.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'multiplymatrices22.html', context)

    else:
        form = MatrixInput2x2()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'multiplymatrices22.html', context)

def multiplymatrices3x3(request):
    title = 'Calculators | Multiply two 3x3 Matrices'
    if request.method == 'POST':
        form = MatrixInput3x3(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13']], 
                [data['a21'], data['a22'], data['a23']],
                [data['a31'], data['a32'], data['a33']]]

            b = [[data['b11'], data['b12'], data['b13']], 
                [data['b21'], data['b22'], data['b23']],
                [data['b31'], data['b32'], data['b33']]]

            result = calc.multiply3x3matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'multiplymatrices33.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'multiplymatrices33.html', context)

    else:
        form = MatrixInput3x3()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'multiplymatrices33.html', context)

