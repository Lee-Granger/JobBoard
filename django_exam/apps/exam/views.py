from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import bcrypt
# *****************************************************************************************************************************
def index(request):
    return render(request, 'exam/index.html')
# *****************************************************************************************************************************
def register_user(request):
    result = User.objects.validate_reg(request.POST)
    if len(result) > 0: 
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt())
        User.objects.create(First_name = request.POST['f_name'], Last_name = request.POST['l_name'], Email = request.POST['email'], Password = hash1)
        print('*' * 80)
        print('success')
    return redirect('/')

# *****************************************************************************************************************************
def login_user(request):
    errors = {}
    check = User.objects.filter(Email=request.GET['email'])
    if len(check) == 0:
        errors['email'] = 'Please enter a valid email'
    if len(errors) > 0:
        for key in errors.keys():
            messages.error(request, errors[key])
        return redirect('/')
    user = User.objects.get(Email = request.GET['email'])
    if bcrypt.checkpw(request.GET['pword'].encode(), user.Password.encode()):
        request.session['user_id'] = user.id
        print('*' * 80)
        print('success')
        print(user.First_name)
        request.session['user_id'] = user.id
        request.session['name'] = user.First_name
        request.session['last_name'] = user.Last_name
        return redirect('/dashboard')
    return redirect('/')
# *****************************************************************************************************************************
def dashboard(request):
    context = {
        'main_jobs' : Job.objects.filter(user = request.session['user_id']),
        'other_jobs' : Job.objects.all().exclude(user = request.session['user_id']),
    }
    return render(request, 'exam/dashboard.html', context)
# *****************************************************************************************************************************
def add_new_job(request):
    return render(request, 'exam/create_job.html')
# *****************************************************************************************************************************
def post_created_job(request):
    result = Job.objects.validate_job(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/jobs/new')
    Job.objects.create(Name=request.POST['title'], Description = request.POST['description'], Location = request.POST['location'], user = User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')
# *****************************************************************************************************************************
def delete(request, id):
    delete = Job.objects.get(id=id)
    delete.delete()
    return redirect('/dashboard')
# *****************************************************************************************************************************
def logout(request):
    request.session.delete()
    return redirect('/')
# *****************************************************************************************************************************
def edit_job(request, id):
    context = {
        'job' : Job.objects.get(id=id)
    }
    return render(request, 'exam/job_edit.html', context)
# *****************************************************************************************************************************
def post_edit_job(request, id):
    result = Job.objects.validate_job(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/jobs/edit/' + id)
    update = Job.objects.get(id=id)
    update.Name = request.POST['title']
    update.Description = request.POST['description']
    update.Location = request.POST['location']
    update.save()
    return redirect('/dashboard')
# *****************************************************************************************************************************
def view_job(request, id):
    context = {
        'job' : Job.objects.get(id=id)
    }
    return render(request, 'exam/view_job.html', context)