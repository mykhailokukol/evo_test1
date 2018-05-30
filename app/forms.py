from django import forms

class ShowFreezersForm(forms.Form):
    ordering = forms.ChoiceField(label='Сортировать', required=False, choices=[
        ['-clicks', 'По кликам'],
    ])

class ShowTVsForm(forms.Form):
    ordering = forms.ChoiceField(label='Сортировать', required=False, choices=[
        ['-clicks', 'По кликам'],
    ])
