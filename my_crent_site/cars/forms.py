from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)
    email = forms.EmailField(label='Email', required=False)
    review = forms.CharField(label='Please write your review here', max_length=100, required=False)
