from django import forms
from .models import  Home2, Home3

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['title', 'text']

class Home2Form(forms.Form):
    class  Meta:
        model = Home2
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'user_complaints',  # شکایات
            'user_questions',   # سوالات
            'criticisms',       # انتقادات
            'other_items',      # سایر موارد
            'subject',
            'message',
        ]
        labels = {
            'user_complaints': 'شکایات',
            'user_questions': 'سوالات',
            'criticisms': 'انتقادات',
            'other_items': 'سایر موارد',
        }


class Home3Form(forms.Form):
    class Meta:
        model = Home3
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'subject',
            'message',
        ]
