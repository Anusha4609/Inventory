from django.shortcuts import redirect, render
from .services import *
from .models import *


#fetching the books and saving them to our Books table
def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        button=request.POST.get('buttonval')
        if(button=='search'):
            try:
                books = get_books_data(query)
                context = {'books': books, 'q' : query}
                return render(request, 'Inventory/books_list.html', context)
            except:
                print("No book found")
        else:
            id = request.POST.get('dropdown')
            books = get_books_data_ById(id)
            bookname = books['volumeInfo']['title']
            qty = request.POST.get('qty')
            Books.objects.create(name = bookname, googleid = id, quantity = qty)
            return redirect('list')
    else:
        return render(request, 'Inventory/books_list.html')
    return render(request, 'Inventory/books_list.html')

def list(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'Inventory/list.html', context)

def details(request, id):
    books = get_books_data_ById(id)
    context = {'books': books}
    return render(request, 'Inventory/details.html', context)

def edit(request, id):
    if request.method == "POST":
        singleBook = Books.objects.get(id=id)
        singleBook.quantity = request.POST.get('qty')
        singleBook.save()
        return redirect('list')
    else:
        singleBook = Books.objects.get(id=id)
        books = get_books_data(singleBook.googleid)
        context = {'singleBook': singleBook, 'books': books}
        return render(request, 'Inventory/edit.html', context)

def delete(request, id):
    singleBook = Books.objects.get(id=id)
    singleBook.delete()
    return redirect('list')