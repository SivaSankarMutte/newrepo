from App1.models import Questions,User,Marksheet,Rolereq
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class QuestionsForm(forms.ModelForm):
	class Meta:
		model=Questions
		fields="__all__"
		widgets={
			'q1':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter the Question',
				}),
			'opt1':forms.TextInput(attrs={
				'class':'form-control my-1',
				'placeholder':'Enter option1',
				}),
			'opt2':forms.TextInput(attrs={
				'class':'form-control my-1',
				'placeholder':'Enter option2',
				}),
			'opt3':forms.TextInput(attrs={
				'class':'form-control my-1',
				'placeholder':'Enter option3',
				}),
			'opt4':forms.TextInput(attrs={
				'class':'form-control my-1',
				'placeholder':'Enter option4',
				}),
			'ans':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter correct option for Evaluation (a or b or c or d)',
				}),
		}

class UsgForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm Password",
		}))
	class Meta:
		model=User
		fields=['username','clg','regdno','rollno','email','gender','branch']
		widgets={
		'username':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your Name',
				}),
		'clg':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Enter your college name',
			}),
		'regdno':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Enter your Register Number',
			}),
		'rollno':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Enter your Roll Number',
			}),
		'email':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Enter your email',
			}),
		'gender':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Select Gender',
			}),
		'branch':forms.TextInput(attrs={
			'class':'form-control my-2',
			'placeholder':'Select Branch',
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Old Password",
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter new Password",
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm new Password",
		}))

	class Meta:
		model=User
		fields=['old_password','new_password1','new_password2']
		

class UserForm(forms.ModelForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm Password",
		}))
	class Meta:
		model=User
		fields=['clg','regdno','rollno','email','gender','branch']
		widgets={
			'clg':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your clg',
				}),
			'regdno':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your Register Number',
				}),
			'rollno':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your Roll Number',
				}),
			'email':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your email',
				}),
			'gender':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Select Gender',
				}),
			'branch':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Select Branch',
				}),
		}

class MarksheetForm(forms.ModelForm):
	class Meta:
		model=Marksheet
		fields="__all__"
		widgets={
			'username':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your Name',
				}),
			'regdno':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Enter your Register Number',
				}),
			'marks':forms.TextInput(attrs={
				'class':'form-control my-2',
				'placeholder':'Marks obtained',
				}),

		}


class Rltype(forms.ModelForm):
	class Meta:
		model=Rolereq
		fields=['uname','rltype']
		widgets={
		"uname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,

			}),
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','role']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}