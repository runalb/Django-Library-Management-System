from django import forms
from .models import LibraryModel

class AddBook(forms.ModelForm):
    book_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Book Name'}))
    author_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}))

    class Meta():
        model = LibraryModel
        fields = '__all__'


class SearchForm(forms.Form):
    search_form = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Book Name','class':'form-control my-0 py-1'}))