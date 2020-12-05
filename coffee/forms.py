from django import forms


class FunctionReview(forms.Form):
    review=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter the reviews',
    }))

    def clean_review(self):
        a=self.cleaned_data.get('review')

        if a.upper() != "FUCK" and a.upper() != "BITCH" :
            return a
        else:
            raise forms.ValidationError("Abusive Words Can't upload")

class FunctionOrder(forms.Form):
    food = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        'placeholder': 'Eg:Pepsi-5',

    }))
    number = forms.CharField()

    address=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter Your Address',
        'row':10,
        'col':10,
    }))


    def clean_number(self):
        a=self.cleaned_data.get('number')
        if len(a)==10:
            return a
        else:
            raise forms.ValidationError('Enter 10 numbers')