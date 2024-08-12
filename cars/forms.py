from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100,widget=forms.TextInput(attrs={'class': 'form','placeholder': 'Please enter your name',  'required': 'True'}))
    email = forms.EmailField(label="Your email",widget=forms.TextInput(attrs={'class': 'form','placeholder': 'Please enter your email'}))
    review = forms.CharField(label="Your review", widget=forms.Textarea(attrs={'class': 'form','placeholder': 'Please enter your review..','rows': 5,'cols': 30}))
# widgets/attrs for styling with css or bootstrap
    # validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            raise forms.ValidationError(
                "Name should only contain alphabetic characters."
            )
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Add any custom validation for email if needed
        if "@" not in email:
            raise forms.ValidationError("Please  Enter a valid email")
        return email

    def clean_review(self):
        review = self.cleaned_data.get("review")
        # Add any custom validation for message if needed
        return review

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional cross-field validation here if needed
        return cleaned_data
