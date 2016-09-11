from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import Book, Review
from ..login_reg.models import User
from collections import Counter

def index(request):
    return render(request, 'book_review/index.html')

def add(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'book_review/add.html', context)

def user(request, user_id):
    user = User.objects.get(id = user_id)
    reviews = Review.objects.filter(user_id = user_id)
    # repeat = []
    # for y in (0,len(reviews)-1):
    #     if any(reviews[y].book_id.title in s for s in repeat):
    #         reviews[y].book_id.title=''
    #     repeat.append(reviews[y].book_id.title)
    #     print reviews[y].book_id.title
    total = Review.objects.filter(user_id = user_id).count()
    context = {'user':user, 'reviews': reviews, 'total': total}
    return render(request, 'book_review/user.html', context)

def books(request):
    books = Book.objects.all()
    recent = Review.objects.all().order_by('-created_at')[:3]
    context = {'books':books, 'recent':recent}
    return render(request, 'book_review/books.html', context)

def specific(request, book_id):
    book = Book.objects.get(id = book_id)
    reviews = Review.objects.filter(book_id=book_id)
    context = {'book':book, 'reviews': reviews}
    return render(request, 'book_review/specific.html', context)


def add_book(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        errors = []
        if len(request.POST['title']) < 1:
            errors.append('Title can not be empty')
        if len(request.POST['author2']) < 1:
            if request.POST['author1'] == 'select':
                errors.append('Author can not be empty')
            author = request.POST['author1']
        else:
            author = request.POST['author2']
        if len(request.POST['review']) < 1:
            errors.append('Review can not be empty')
        if len(errors) > 0:
            print_messages(request, errors)
            return redirect(reverse('add'))
        book = Book.objects.create(title = request.POST['title'], author = author, user_id = user)
        review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user_id = user, book_id = book)
        return redirect(reverse('books_specific', kwargs={'book_id':book.id}))
    else:
	    return redirect(reverse('books_index'))

def add_review(request, book_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        book = Book.objects.get(id=book_id)
        review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user_id = user, book_id = book)
        return redirect(reverse('books_specific', kwargs={'book_id':book_id}))
    else:
	    return redirect(reverse('books_index'))

def delete_review(self, review_id):
    review = Review.objects.get(id = review_id)
    page = review.book_id.id
    print page
    Review.objects.filter(id = review_id).delete()
    return redirect(reverse('books_specific', kwargs={'book_id':page}))
