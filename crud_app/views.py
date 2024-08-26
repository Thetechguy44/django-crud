from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Candidate

# Create your views here.

#this is the function for reading and displaying datas to the webpage
def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'index.html', {'candidates':candidates})

#this is the function for viewing the create page (form)
def create(request):
    return render(request,'create.html')

#this is the fuction for storing data to the database
def store(request):
    f = request.POST['firstname']
    l = request.POST['lastname']  
    e = request.POST['email']     
    p = request.POST['phone']     
    g = request.POST['gender']    
    a = request.POST['age']       
    c = request.POST['country']   

    if not all([f, l, e, p, g, a, c]):
        messages.error(request, "All fields are required. Please fill in all the information.")
        return redirect('create')

    candidate = Candidate(
        firstname=f,
        lastname=l,
        email=e,
        phone=p,
        gender=g,
        age=a,
        country=c
    )
    candidate.save()

    #success message
    messages.success(request, "Candidate saved successfully!")
    return redirect("/")

#this fuction for editing a user
def edit(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, 'edit.html', {'candidate':candidate})

#this fuction is for updating user info
def update(request, id):
    # Retrieve updated data from the form
    f = request.POST['firstname']
    l = request.POST['lastname']
    e = request.POST['email']
    p = request.POST['phone']
    g = request.POST['gender']
    a = request.POST['age']
    c = request.POST['country']

    # Get the candidate object from the database using the ID
    candidate = Candidate.objects.get(id=id)
    
    # Update the candidate's attributes
    candidate.firstname = f 
    candidate.lastname = l  
    candidate.email = e     
    candidate.phone = p     
    candidate.gender = g    
    candidate.age = a       
    candidate.country = c   
    
    # Save the updated candidate object
    candidate.save()

    # Success message
    messages.success(request, "Candidate updated successfully!")
    return redirect("/")

#this fuction is for deleting candidate from the application
def delete(request, id):
    candidate = Candidate.objects.get(id=id)
    candidate.delete()
    
    #success message
    messages.success(request, "Candidate deleted successfully!")
    return redirect("/")