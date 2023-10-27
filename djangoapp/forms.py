from django import forms
from .models import todo

class Todoform(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['player', 'club', 'value']

    player=forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"text" ,"class":"form-control", "placeholder":"player name" }))
    club=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"type":"text" ,"class":"form-control", "placeholder":"club" }))
    value=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"type":"text" ,"class":"form-control", "placeholder":"value" }))


  