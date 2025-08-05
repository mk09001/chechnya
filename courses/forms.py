from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[
                (1, '1 - Очень плохо'),
                (2, '2 - Плохо'),
                (3, '3 - Удовлетворительно'),
                (4, '4 - Хорошо'),
                (5, '5 - Отлично'),
            ]),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваш отзыв о курсе'}),
        } 