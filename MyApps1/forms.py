from django import forms
class NameForm(forms.Form):
    name=forms.CharField()
class AgeForm(forms.Form):
    age=forms.IntegerField()
class ParentForm(forms.Form):
    parent=forms.CharField()
class AdditemForm(forms.Form):
    name=forms.CharField();
    quantity=forms.IntegerField();

