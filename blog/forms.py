from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ('author','title','text')

		# widgets = {
		# 	'title' : forms.TextInput(attrs={'class':'TextInputClass'})
		# 	'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
		# }
		widgets = {
            # The class here is a CSS class.
            'title' : forms.TextInput(attrs={'class':'TextInputClass'}), #TextInputClass is our class
            'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}), #postcontent class is our class
        }
		# connect wiegt to css classes

class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('author','text')

		# widgets = {
		# 	'author' : forms.TextInput(attrs={'class': 'textinputclass' }) 
		# 	'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),	
		# }

		widgets = {
            # The class here is a CSS class.
            'title' : forms.TextInput(attrs={'class':'TextInputClass'}), #TextInputClass is our class
            'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea'}), #postcontent class is our class
        }