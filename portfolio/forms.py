from django import forms as f
from portfolio.models import *
from shared.utils import *

class ImageForm(FormsetModelForm):
    class Meta:
        model   = Image
        exclude = "image width height category thumbnail1 thumbnail2".split()
        attrs   = dict(cols=70)
        widgets = dict( description=f.Textarea(attrs=attrs) )

class AddImageForm(f.ModelForm):
    class Meta:
        model   = Image
        exclude = "width height category thumbnail1 thumbnail2".split()
        attrs   = dict(cols=70, rows=2)
        widgets = dict( description=f.Textarea(attrs=attrs) )
