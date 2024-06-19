from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'decision_tree_model.pkl')
model = joblib.load(model_path)

def home(request):
    return render(request, 'predictor/homepage.html')

def predict_eligibility(request):
    if request.method == 'POST':
        months_since_last_donation = int(request.POST.get('months_since_last_donation'))
        number_of_donations = int(request.POST.get('number_of_donations'))
        total_volume_donated = int(request.POST.get('total_volume_donated'))
        months_since_first_donation = int(request.POST.get('months_since_first_donation'))
        allergy = int(request.POST.get('allergy'))
        disease = int(request.POST.get('disease'))

        # Make prediction
        prediction = model.predict([[months_since_last_donation, number_of_donations, total_volume_donated, months_since_first_donation, allergy, disease]])
        eligible = bool(prediction[0])  # Convert to native Python boolean

        return JsonResponse({'eligible': eligible})
    return render(request, 'predictor/eligibility.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please sign in.')
            return redirect('signin')
        else:
            messages.error(request, 'There was an error in the form. Please check the details and try again.')
    else:
        form = UserCreationForm()
    return render(request, 'predictor/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'predictor/signin.html')
    else:
        return render(request, 'predictor/signin.html')

def logout_view(request):
    logout(request)
    return redirect('signin')

@login_required
def profile_view(request):
    return render(request, 'predictor/profile.html')

@login_required
def homepage(request):
    return render(request, 'predictor/homepage.html')
