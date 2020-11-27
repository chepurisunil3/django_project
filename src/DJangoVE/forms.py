from django import forms

class TestForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input-field"}),label='')
    password = forms.CharField(label='')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # if not "gmail.com" in email:
        #     raise forms.ValidationError("Email has to be gmail")
        return email
