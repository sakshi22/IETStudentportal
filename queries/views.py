from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Query, Answer
from django.db.models import Q
from .forms import QueryForm
from datetime import date


@login_required(login_url='login')
def queryPage(request):
    # q = request.GET.get('q') if request.GET.get('q') != None else ''
    queries = Query.objects.all()
    form = QueryForm()

    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.author = request.user
            query.save()
            return redirect('queries')

    context = {'queries' : queries, 'form' : form}
    return render(request, 'queries/queries.html', context)


@login_required(login_url='login')
def deleteQuery(request, qid):
    query = Query.objects.get(id=qid)

    if request.user != query.author:
        return HttpResponse('You are not authorized to delete this query')

    if request.method == 'POST':
        query.delete()
        return redirect('queries')

    return render(request, 'home/delete.html', {'obj' : query})
    


@login_required(login_url='login')
def query(request, qid):
    query = Query.objects.get(id=qid)
    answers = query.answer_set.all()

    context = {'query' : query, 'answers' : answers} 

    if request.method == "POST":
        answer = Answer.objects.create(
            author=request.user,
            query=query,
            body=request.POST.get('body')
        )
        return redirect('query', qid=query.id)

    return render(request, 'queries/query.html', context)
