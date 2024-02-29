from django import forms
from book.models import BookStoreModel

class BookStoreFrom(forms.ModelForm):
    class Meta:
        model=BookStoreModel
        #exclude=['first_pub','last_pub'] # it will totally cancel these data.so we need to take fields
        fields=['id','book_name','author','category']
        