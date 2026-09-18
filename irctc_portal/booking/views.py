from django.shortcuts import render

# Create your views here.
def home(request):
    train = {
    "train_no": "12951",
    "train_name": "Mumbai Rajdhani Express",
    "source": "Mumbai Central",
    "destination": "New Delhi",
    "departure": "17:00",
    "arrival": "08:35"
    }
    return render(request,'home_page.html',train)

def trains_search(request):
    trains = [
    {
        "train_no": "12951",
        "train_name": "Mumbai Rajdhani Express",
        "source": "Mumbai Central",
        "destination": "New Delhi",
        "departure": "17:00",
        "arrival": "08:35"
    },
    {
        "train_no": "12002",
        "train_name": "Bhopal Shatabdi Express",
        "source": "New Delhi",
        "destination": "Bhopal",
        "departure": "06:00",
        "arrival": "14:00"
    },
    {
        "train_no": "12301",
        "train_name": "Howrah Rajdhani Express",
        "source": "New Delhi",
        "destination": "Howrah",
        "departure": "16:55",
        "arrival": "10:00"
    }
    ]
    return render(request,'train_search_page.html',{"trains":trains})

def passenger_details(request):
    passenger = {
    "name": "Rahul Sharma",
    "age": 21,
    "gender": "Male",
    "coach": "A2",
    "berth": "Upper"
    }
    return render(request,'passenger_details_page.html',passenger)

def booking_confirmation(request):
    booking = {
        "passenger_name": "Rahul Sharma",
        "train_no": "12951",
        "train_name": "Mumbai Rajdhani Express",
        "source": "Mumbai Central",
        "destination": "New Delhi",
        "coach": "A2",
        "berth": "Upper"
    }
    return render(request, "booking_confirmation_page.html", booking)