from django import forms
from django.contrib.auth.models import User


class ExpenseItemForm(forms.Form):
    TYPE_CHOICES = (
        ('Clothing', "Clothing"),
        ('Cosmetics', "Cosmetics"),
        ('Entertainment', "Entertainment"),
        ('Food', "Food"),
        ('Recharge', "Recharge"),
        ('Shopping', "Shopping"),
        ('Subscriptions', "Subscriptions"),
        ('Travel', "Travel"),
    )
    ACCOUNT_CHOICES = (
        ('Cash', "Cash"),
        ('Card', "Card"),
    )

    attr = {"class": "form-control-sm"}
    # attr = {}

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attr))
    type = forms.CharField(widget=forms.Select(choices=TYPE_CHOICES, attrs=attr))
    amount = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs=attr))
    account = forms.CharField(widget=forms.Select(choices=ACCOUNT_CHOICES, attrs=attr))
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(2017, 2021), attrs=attr))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs=attr), required=False)

    def clean(self):
        # if 'update' in self.data:
        #     print('update found')
        # if 'back' in self.data:
        #     print('back found')
        cleaned_data = super(ExpenseItemForm, self).clean()
        title = cleaned_data.get('title')
        type = cleaned_data.get('type')
        amount = cleaned_data.get('amount')
        account = cleaned_data.get('account')
        date = cleaned_data.get('date')
        description = cleaned_data.get('description')
        if not title and not amount:
            raise forms.ValidationError('Marked Fields cannot be blank !')


'''------------------------------------------- '''


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!',
        required=False
    )
    source = forms.CharField(  # A hidden input for internal use
        max_length=50,  # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError("Cannot submit empty form!")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']