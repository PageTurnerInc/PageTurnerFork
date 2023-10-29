from django import forms
from review.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'book', 'rating', 'comment']
        widgets = {'book': forms.HiddenInput(), 
                'user': forms.HiddenInput(),
                'comment': forms.Textarea(attrs={'rows': 5, 'cols': 25}),}
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = True
        self.fields['comment'].required = False
