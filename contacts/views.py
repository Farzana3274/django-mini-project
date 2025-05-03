from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contact_list')
        else:
            #if user already exist
            if 'username' in form.errors:
                messages.error(request, form.errors['username'][0])
            else:
                messages.error(request, 'Passwords not match.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def contact_list(request):
    search = request.GET.get('search')
    if search:
        contacts = Contact.objects.filter(user=request.user).filter(name__icontains=search) | Contact.objects.filter(user=request.user).filter(email__icontains=search)
    else:
        contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form, 'title': 'Add Contact'})

@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form, 'title': 'Edit Contact'})

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
    return redirect('contact_list')
