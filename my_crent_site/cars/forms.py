from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=30, required=False)
#     last_name = forms.CharField(label='Last Name', max_length=30, required=False)
#     email = forms.EmailField(label='Email', required=False)
#     review = forms.CharField(label='Please write your review here', 
#                              max_length=100, 
#                              required=False, 
#                              widget=forms.Textarea(attrs={'class':'myform',
#                                                           'rows':'2',
#                                                           'cols':'2'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']
        fields = "__all__"
        labels = {
            'first_name': 'YOUR FIRST NAME',
            'last_name': 'LAST NAME',
            'stars': 'Rating'
        }
        error_messages = {
            'stars': {
                'min_value': 'Yo! Min value is 1',
                'max_value': 'Yo! Yo! Max value is 5'
            }
        }