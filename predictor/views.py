from django.shortcuts import render
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
