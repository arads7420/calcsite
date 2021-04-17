from django.shortcuts import render
from . import calculators as calc
from .forms import MatrixInput2x2
from .forms import MatrixInput3x3
from .forms import SingleMatrix2x2
from .forms import SingleMatrix3x3
from .forms import MatrixInput4x4
from .forms import MatrixInput5x5


# Create your views here.
base_site_name = 'Calculator Swift'
def calculators(request): 
    context = {
        'title': base_site_name + '| Calculators',
    }
    return render(request, 'calculators.html', context)

def addmatrices2x2(request):
    title = 'Add two 2x2 Matrices - CalculatorSwift'
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
    title = 'Add two 3x3 Matrices - CalculatorSwift'
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
    title = 'Multiply two 2x2 Matrices - CalculatorSwift'
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
    title = 'Multiply two 3x3 Matrices - CalculatorSwift'
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

def addmatrices4x4(request):
    title = 'Add two 4x4 Matrices - CalculatorSwift'
    if request.method == 'POST':
        form = MatrixInput4x4(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13'], data['a14']], 
                [data['a21'], data['a22'], data['a23'], data['a24']],
                [data['a31'], data['a32'], data['a33'], data['a34']],
                [data['a41'], data['a42'], data['a43'], data['a44']]]

            b = [[data['b11'], data['b12'], data['b13'], data['b14']], 
                [data['b21'], data['b22'], data['b23'], data['b24']],
                [data['b31'], data['b32'], data['b33'], data['b34']],
                [data['b41'], data['b42'], data['b43'], data['b44']]]

            result = calc.add4x4matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'addmatrices44.html', context)
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
            return render(request, 'addmatrices44.html', context)

    else:
        form = MatrixInput4x4()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'addmatrices44.html', context)

def addmatrices5x5(request):
    title = 'Add two 5x5 Matrices - CalculatorSwift'
    if request.method == 'POST':
        form = MatrixInput4x4(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13'], data['a14'], data['a15']], 
                [data['a21'], data['a22'], data['a23'], data['a24'], data['a25']],
                [data['a31'], data['a32'], data['a33'], data['a34'], data['a35']],
                [data['a41'], data['a42'], data['a43'], data['a44'], data['a45']], 
                [data['a51'], data['a52'], data['a53'], data['a54'], data['a55']]]

            b = [[data['b11'], data['b12'], data['b13'], data['b14'], data['b15']], 
                [data['b21'], data['b22'], data['b23'], data['b24'], data['b25']],
                [data['b31'], data['b32'], data['b33'], data['b34'], data['b35']],
                [data['b41'], data['b42'], data['b43'], data['b44'], data['b45']], 
                [data['b51'], data['b52'], data['b53'], data['b54'], data['b55']]]

            result = calc.add5x5matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'addmatrices55.html', context)
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
            return render(request, 'addmatrices55.html', context)

    else:
        form = MatrixInput5x5()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'addmatrices55.html', context)

def determinant2x2(request):
    title = 'Determinant of a 2x2 Matrix - CalculatorSwift'
    if request.method == 'POST':
        form = SingleMatrix2x2(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12']], [data['a21'], data['a22']]]


            result = calc.determinant2x2(a)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'determinant2x2.html', context)
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
            return render(request, 'determinant2x2.html', context)

    else:
        form = SingleMatrix2x2()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'determinant2x2.html', context)

def determinant3x3(request):
    title = 'Determinant of a 3x3 Matrix - CalculatorSwift'
    if request.method == 'POST':
        form = SingleMatrix3x3(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13']], 
                [data['a21'], data['a22'], data['a23']],
                [data['a31'], data['a32'], data['a33']]]


            result = calc.determinant3x3(a)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'determinant3x3.html', context)
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
            return render(request, 'determinant3x3.html', context)

    else:
        form = SingleMatrix3x3()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'determinant3x3.html', context)


def multiplymatrices4x4(request):
    title = 'Multiply two 4x4 Matrices - CalculatorSwift'
    if request.method == 'POST':
        form = MatrixInput4x4(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13'], data['a14']], 
                [data['a21'], data['a22'], data['a23'], data['a24']],
                [data['a31'], data['a32'], data['a33'], data['a34']],
                [data['a41'], data['a42'], data['a43'], data['a44']]]

            b = [[data['b11'], data['b12'], data['b13'], data['b14']], 
                [data['b21'], data['b22'], data['b23'], data['b24']],
                [data['b31'], data['b32'], data['b33'], data['b34']],
                [data['b41'], data['b42'], data['b43'], data['b44']]]

            result = calc.multiply4x4matrices(a, b)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'multiplymatrices44.html', context)
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
            return render(request, 'multiplymatrices44.html', context)

    else:
        form = MatrixInput4x4()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'multiplymatrices44.html', context)


def eigenvalues2x2(request):
    title = 'Eigen Values and Eigen Vectors of a 2x2 Matrix - CalculatorSwift'
    if request.method == 'POST':
        form = SingleMatrix2x2(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12']], [data['a21'], data['a22']]]


            result = calc.eigenvalues2x2(a)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                },
                'init': False
            }
            return render(request, 'eigenvalues2x2.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                },
            }
            return render(request, 'eigenvalues2x2.html', context)

    else:
        form = SingleMatrix2x2()
        form.fields["a11"].initial = 5
        form.fields["a12"].initial = 4
        form.fields["a21"].initial = 1
        form.fields["a22"].initial = 2

        result = {
            'val_1': '1',
            'val_2': '6',
            'vec1_1': '-1',
            'vec1_2': '1',
            'vec2_1': '4',
            'vec2_2': '1',
            'm_1': '1',
            'm_2': '2',
            'poly': '\lambda^{{2}} - 7 \lambda + 6'
        }
        context = {
            'title': title,
            'form': form,
            'default': {
                'result': result 
            },
            'init': True
        }
        return render(request, 'eigenvalues2x2.html', context)


def eigenvalues3x3(request):
    title = 'Eigen Values and Eigen Vectors of a 3x3 Matrix - CalculatorSwift'
    if request.method == 'POST':
        form = SingleMatrix3x3(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            a = [[data['a11'], data['a12'], data['a13']], 
                [data['a21'], data['a22'], data['a23']],
                [data['a31'], data['a32'], data['a33']]]


            result = calc.eigenvalues3x3(a)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                },
                'init': False
            }
            return render(request, 'eigenvalues3x3.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                },
            }
            return render(request, 'eigenvalues3x3.html', context)

    else:
        form = SingleMatrix3x3()
        form.fields["a11"].initial = 1
        form.fields["a12"].initial = 1
        form.fields["a13"].initial = 3
        form.fields["a21"].initial = 1
        form.fields["a22"].initial = 5
        form.fields["a23"].initial = 1
        form.fields["a31"].initial = 3
        form.fields["a32"].initial = 1
        form.fields["a33"].initial = 1

        result = {
            'val_1': '-2',
            'val_2': '3',
            'val_3': '6',
            'vec1_1': '-1',
            'vec1_2': '0',
            'vec1_3': '1',
            'vec2_1': '1',
            'vec2_2': '-1',
            'vec2_3': '1',
            'vec3_1': '1',
            'vec3_2': '2',
            'vec3_3': '1',
            'm_1': '1',
            'm_2': '1',
            'm_3': '1',
            'poly': '\lambda^{{3}} - 7 \lambda^{{2}} + 36'
        }
        context = {
            'title': title,
            'form': form,
            'default': {
                'result': result 
            },
            'init': True
        }
        return render(request, 'eigenvalues3x3.html', context)