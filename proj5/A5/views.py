from django.shortcuts import render

# Create your views here.
def showlist(request):
    Students = ["Umang", "Piyush", "Sourav", "Prajwal"]
    Fruits = ["Mango", "Apple", "Banana", "JackFruit"]
    return render(request, 'showlist.html', {"Fruits": Fruits, "Students": Students})