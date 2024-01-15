from django import forms
from .models import Company, Product

class FormCreate(forms.Form):
    name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'name'}))
    price = forms.IntegerField(required=True, label='', widget=forms.TextInput(attrs={'name': 'price'}))

    companies = Company.objects.all().values_list()
    company = forms.ChoiceField(choices=(companies), label='', widget=forms.Select(attrs={'name': 'company'}))

class FormEdit(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'