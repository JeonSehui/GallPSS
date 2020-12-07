from django import forms
from .models import BoardItem

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['itemtitle'].label = '제목'
        self.fields['itemtitle'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = BoardItem
        fields = ['itemtitle', 'itemcontent']
        widgets = {
            'itemcontent': SummernoteWidget(),
        }