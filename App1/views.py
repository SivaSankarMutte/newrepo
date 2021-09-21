from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ExamPortal import settings
from django.core.mail import send_mail
from App1.forms import QuestionsForm,UserForm,MarksheetForm,UsgForm,Chgepwd,Rltype,Rlupd
from App1.models import Questions,User,Rolereq,Marksheet
# Create your views here.
def home(request):
	return render(request,'ht1/home.html')

# def questions(request):
# 	q=QuestionsForm()
# 	if request.method=="POST":
# 		m=QuestionsForm(request.POST,request.FILES)
# 		if m.is_valid():
# 			n=m.save(commit=False)
# 			messages.success(request,"{} question added successfully".format(n.q1))
# 			n.save()
# 		return render(request,'ht1/addQuestion.html',{'questionsform':q})
# 	return render(request,'ht1/addQuestion.html',{'questionsform':q})

def addQuestions(request):
	q=QuestionsForm()
	if request.method=="POST":
		m=QuestionsForm(request.POST,request.FILES)
		if m.is_valid():
			n=m.save(commit=False)
			messages.success(request,"{} question added successfully".format(n.q1))
			n.save()
		return render(request,'ht1/addQuestion.html',{'questionsform':q})
	return render(request,'ht1/addQuestion.html',{'questionsform':q})

# def marksUpdate(request,marks):
# 	m=MarksheetForm()
# 	user=User.objects.get(id=request.user.id)
# 	m.name=user.username
# 	m.regdno=user.regdno
# 	m.marks=marks
# 	if m.is_valid():
# 		m.save()
# 		return render(request,'ht1/examsuccess.html')
# 	else:
# 		return render(request,'ht1/submitfailed.html')
def exam(request):
	questions=Questions.objects.all()
	if request.method=="POST":
		marks=0
		for i in questions:
			ans=request.POST[i.q1]
			if((ans==i.opt1 and i.ans=='a') or (ans==i.opt2 and i.ans=='b') or (ans==i.opt3 and i.ans=='c') or (ans==i.opt4 and i.ans=='d')):
				marks+=1
		print(marks)

		#marksUpdate(request,count)
		m=MarksheetForm()
		user=User.objects.get(id=request.user.id)
		m.name=user.username
		m.regdno=user.regdno
		m.marks=marks
		print(user.username)
		print(user.regdno)
		if m.is_valid():
			m.save()
			return render(request,'ht1/examsuccess.html')
		else:
			print(m)
			return render(request,'ht1/submitfailed.html')
	# qs=[]
	# opts=[]
	# for i in questions:
	# 	qs.append(i.q1)
	# 	opts.append([i.opt1,i.opt2,i.opt3,i.opt4])
	# print(qs)
	# print(opts)
	context={'questions':questions}
	# dict1={'qs':qs,'opts':opts}
	return render(request,'ht1/exam.html',context)

def userRegistration(request):
	u=UsersForm()
	if request.method=="POST":
		m=UsersForm(request.POST,request.FILES)
		if m.is_valid():
			n=m.save(commit=False)
			messages.success(request,"{} registered successfully".format(n.username))
			n.save()
		return render(request,'ht1/userRegistration.html',{'userform':u})
	return render(request,'ht1/UserRegistration.html',{'userform':u})

def usrreg(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			n=d.save(commit=False)
			messages.success(request,"{} registered successfully".format(n.username))
			n.save()
			return redirect('/login')
		else:
			print("SOME ERROR in registration")
	d=UsgForm()
	return render(request,'ht1/userregister.html',{'t':d})

def pfle(request):
	userdata=User.objects.get(id=request.user.id)
	#k=Profile(instance=userdata)
	return render(request,'ht1/profile.html',{"u":userdata})


# def profileUpdate(request,id):
# 	userdata=User.objects.get(id=id)
# 	if request.method=="POST":
# 		userdata.username=request.POST.get('username')
# 		userdata.email=request.POST.get('email')
# 		userdata.mobilenumber=request.POST.get('mobile')
# 		userdata.age=request.POST.get('age')
# 		userdata.first_name=request.POST.get('fname')
# 		userdata.last_name=request.POST.get('lname')

# 		userdata.save()
		
# 		#d=Profile(request.POST,request.FILES,instance=userdata)
# 		#print(d)
# 		#userdata.username=request.POST['username']
# 		#userdata.first_name=request.POST['first_name']
# 	#k=Profile(instance=userdata)
# 		return pfle(request,id=id)
# 	return render(request,'ht1/profileupdate.html',{"us":userdata})
# def pfleupd(request):
# 	t=User.objects.get(id=request.user.id)
# 	if request.method=="POST":
# 		pfle=Pfupd(request.POST,request.FILES,instance=t)
# 		if pfle.is_valid():
# 			pfle.save()
# 			return redirect('/pfle')
# 	pfle=Pfupd(instance=t) 
# 	return render(request,'ht1/pfleupdate.html',{'u':pfle})


def changepwd(request):
	if request.method=="POST":
		k=Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			messages.success(request,"Password changed Successfully")
			k.save()
			return redirect('/login')
	k=Chgepwd(user=request)
	return render(request,'ht1/changepwd.html',{'t':k})

def rolereq(request):
	p=Rolereq.objects.filter(ud_id=request.user.id).count()

	if request.method=="POST":
		k=Rltype(request.POST,request.FILES)
		if k.is_valid():
			y=k.save(commit=False)
			y.ud_id=request.user.id
			y.uname=request.user.username
			y.save()
			return redirect('/')

	k=Rltype()
	return render(request,'ht1/rolereq.html',{'d':k,'c':p})
def gveperm(request):
	u=User.objects.all()
	r=Rolereq.objects.all()
	d={}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id!=m.ud_id:
				continue
			else:
				d[n.id]=m.uname,m.rltype,n.role,n.id
	return render(request,'ht1/givepermissions.html',{'h':d.values()})

def gvupdate(request,t):
	print("USER ID",t)
	y=Rolereq.objects.get(ud_id=t)
	d=User.objects.get(id=t)
	if request.method=="POST":
		n=Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked=1
			y.save()
		return redirect('/gvper')
	n=Rlupd(instance=d)
	#userrow=User.objects.get(id=row.ud_id)
	#if request.method=="POST":
	#	#row.uname=request.POST['uname']
	#	row.rltype=request.POST['rltype']
	#	userrow.role=request.POST['role']
	#	print(userrow.role)
	#	row.save()
	#	print("YESS")
	#	userrow.save()
	#	print("ALSO")
	#	return gveperm(request)
	#return render(request,'app/gvupdate.html',{'row':row,'u':userrow})
	return render(request,'ht1/gvupdate.html',{"n":n})

def feedback(request):
	if request.method=="POST":
		sd=request.POST['snmail'].split(',')
		sm=request.POST['sub']
		mg=request.POST['msg']
		rt=settings.EMAIL_HOST_USER
		#sen_mail(sub,msg,sender,receivers)
		dt=send_mail(sm,mg,rt,sd)
		if dt==1:
			messages.success(request,"Feedback sent Successfully")
			return render(request,'ht1/feedback.html')
		else:
			messages.danger(request,"Feedback failed to sent")
			return render(request,'ht1/feedback.html')
	return render(request,'ht1/feedback.html')


def deleteuser(request,id):
	u=User.objects.get(id=id)
	messages.success(request,"{} deleted Successfully".format(u.username))
	u.delete()
	return redirect(request.META['HTTP_REFERER'])