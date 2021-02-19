from django import forms


class SearchForm(forms.Form):
    zip_code = forms.IntegerField()
    date = forms.DateField()
