from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QueryForm
from . import namegenerator

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)

        if form.is_valid():
            word_list = form.cleaned_data['query_input'].split(' ')
            data = namegenerator.gen_random_names(word_list, 100)
            context = {
                'form': form,
                'data': data,
            }
            return render(request, "index.html", context)
    else:
        form = QueryForm()
    return render(request, "index.html", {'form': form})
