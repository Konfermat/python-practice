from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'text']
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 40,
                'rows': 5,
                'placeholder': 'Введите ваш отзыв сдесть...',
                'class': 'form-control',
            }),
        }

