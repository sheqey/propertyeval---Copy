from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.
def home(request):
   return render(request,'index.html')


def home2(request):
   return render(request,'index2.html')

def index(request,id):

  return render(request,'data.html')


def form(request):
   return render(request, 'form.html')



def about(request):
   return render(request, 'about.html')



def success(request):
   if request.method == 'POST':
      email = request.POST.get('email')
        # Do something with the email, like saving it to the database or sending an email
      location = request.POST.get('location')
      bedrooms = request.POST.get('bedrooms')
      print(location)
      print(bedrooms)
      price = predict_price_direct(location, bedrooms)
      return render(request, 'success.html', {'price': price})
   else:
     return render(request, 'form.html')


# def success(request):
#    if request.method == 'POST':
#       email = request.POST.get('email')
#         # Do something with the email, like saving it to the database or sending an email
#       location = request.POST.get('location')
#       bedrooms = request.POST.get('bedrooms')
#       print(location)
#       print(bedrooms)
#       price = predict_price_direct(location, bedrooms)
#       return render(request, 'success.html', {'price': price})
#    else:
#      return render(request, 'form.html')




def predict_price_direct(location, bedrooms):
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import LabelEncoder

    import os

    file_path = os.path.join(os.path.dirname(__file__), "data.csv")
  #  handle = open(file_path, "r")

    data = pd.read_csv(file_path)
    # Encode the 'location' column
    labelEncoder = LabelEncoder()
    data['location'] = labelEncoder.fit_transform(data['location'])
    X = data.drop(columns=['price'])
    y = data['price']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    location = labelEncoder.transform([location])[0]
    p = model.predict([[bedrooms, location]])
    return p