from django import forms
from .models import Feedback

# class FeedbackForms(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=1, error_messages={
#         'max_length':'Слишком много символов',
#         'min_length':'Слишком мало символов',
#         'required':'Заполните поле хотя бы одним символом'
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":40}))

class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'feedback']
        fields = '__all__'
        labels = {
            'name':'Имя',
            'surname':'Фамилия',
            'feedback':'Отзыв'
        }
        error_messages = {
            'name': {
                'max_length': 'Слишком много символов',
                'min_length':'Слишком мало символов',
                'required':'Заполните поле хотя бы одним символом'
            },
            'surname': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Заполните поле хотя бы одним символом'
            },
            'feedback':{
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Заполните поле хотя бы одним символом'
            }
        }