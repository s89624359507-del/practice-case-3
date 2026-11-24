from django import forms
from .models import UserName


class NameForm(forms.ModelForm):
    """Форма на основе модели UserName с валидацией пустого поля."""

    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите ваше имя',
                'class': 'name-input',
                'autocomplete': 'off',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Поле имени не может быть пустым.')
        if len(name) > 50:
            raise forms.ValidationError('Имя слишком длинное (максимум 50 символов).')
        return name
