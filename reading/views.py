from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Book
from .aux import getBooksByTitle, getBookById, quotes
from datetime import date
import random

def index(request):

    context = {
        'quote': random.choice(quotes),
    }

    return render(request, "reading/index.html", context)


def topbooks(request):

    books = Book.objects.all()
    gids = []
    for book in books:
        if book.finished != None:
            gids.append(book.gid)

    counter = {i:gids.count(i) for i in gids}

    ranking = []
    for gid in counter.keys():
        ranking.append(getBookById(gid))

    context = {
        'books': ranking,
    }

    return render(request, "reading/top_books.html", context)


def topreaders(request):

    result = dict()
    for user in User.objects.all():
        counter = 0
        for book in user.readingList.all():
            if book.finished != None:
                counter += 1

        result[user] = counter

    context = {
        'result': sorted(result.items(), key=lambda x: x[1], reverse=True),
    }

    print(context['result'])

    return render(request, "reading/top_readers.html", context)


def user_view(request):

    if request.method == 'POST':
        try:
            gid = request.POST['book_gid']
            b = Book.objects.get(gid=gid)
            if b.started == None:
                b.started = date.today()
                b.save()
            else:
                b.finished = date.today()
                b.save()
        except:
            try:
                request.user.image = request.POST['userImage']
                request.user.save()
            except:
                pass

    books = []
    saved = 0
    reading = 0
    read = 0

    for book in request.user.readingList.all():
        dict = {'model': book, 'api': getBookById(book.gid)}
        books.append(dict)
        if book.started == None:
            saved += 1
        elif book.finished != None:
            read += 1
        else:
            reading += 1

    context = {
        'books': books,
        'saved': saved,
        'reading': reading,
        'read': read,
    }

    return render(request, "reading/user.html", context)


def search(request):
    if request.method == 'POST':
        searchkey = request.POST['search'];

        context = {
            'books': getBooksByTitle(searchkey),
        };

        return render(request, "reading/search.html", context)


def book(request, gid):
    if request.user.readingList.filter(gid=gid).count() != 0:
        is_in_readingList = True
    else:
        is_in_readingList = False

    context = {
        'book': getBookById(gid),
        'is_in_readingList': is_in_readingList,
    }

    return render(request, "reading/book.html", context)


def add_book(request, gid):
    if request.user.readingList.filter(gid=gid).count() != 0:
        Book.objects.filter(gid=gid, user=request.user).delete()
        # is_in_readingList = True
    else:
        book = Book.objects.create(gid=gid, user=request.user)
        print(book);
        # is_in_readingList = False

    return HttpResponseRedirect(reverse('book', args=(gid,)));


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "reading/login.html", {'message': "Invalid username and/or password"})

    else:
        return render(request, "reading/login.html")


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, "reading/register.html", {'message': "The passwords do not match."})

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "reading/register.html", {'message': "This username is already taken."})

        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, "reading/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
