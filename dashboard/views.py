from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import LibraryModel
from .forms import SearchForm, AddBook
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, UpdateView

# Create your views here.

@login_required
def dashboard_index(request):
    return render(request,'dashboard/index.html',context={'title':'Dashboard'})



@login_required
def add_book(request):
    form = AddBook()

    if request.method == 'POST':
        form = AddBook(request.POST)
        
        if form.is_valid():
            form.save()
            
            context = {
                'result' : 'New Book Added successfully',
                'title':'Add Book',
            }
            return render(request,'dashboard/result.html',context=context)

        else:
            context = {
                'result' : 'ERROR',
                'title':'Add Book',
            }
            return render(request,'dashboard/result.html',context=context)

    context = {
        'form' : form,
        'title':'Add Book',
        }

    return render(request,'dashboard/add_book.html',context=context)


# search_Book
@login_required
def search_available_book(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            search_book = form.cleaned_data['search_form']
            
            all_books = LibraryModel.objects.filter(book_name = search_book).values()  
           
            context = {
                'all_books' : all_books,
                'title' : 'Search Result',
            }
            
            return render(request,'dashboard/view_available_book.html',context=context)


    context = {
        'form' : form,
        'title':'Search Book',
        }

    return render(request,'dashboard/search_book.html',context=context)




# view_available_book
def view_available_books(request):

    all_books = LibraryModel.objects.all()
    context = {
        'all_books' : all_books,
        'title' : 'All Books',
        }
            
    return render(request,'dashboard/view_available_book.html',context=context)


#update book
class UpdateBookView(UpdateView):
    model = LibraryModel
    fields = ('book_name','author_name')
    success_url = reverse_lazy("dashboard:view_available_books")
    template_name = 'dashboard/update_book.html'
    
    



class DeleteBookView(DeleteView):
    model = LibraryModel
    template_name = 'dashboard/confim_delete_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy("dashboard:view_available_books")

