from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    # Retrieve the current visit count from the cookie, defaulting to 0 if not present
    visit_count = int(request.COOKIES.get('visit_count', 0))
    visit_count += 1  # Increment the visit count

    # Create a response object
    response = HttpResponse(f"Visit Count: {visit_count}")

    # Set the updated visit count in the cookie
    response.set_cookie('visit_count', visit_count, max_age=3600)  # Cookie valid for 1 hour

    return response

def get_cookie(request):
    # Retrieve the visit count from the cookie
    visit_count = request.COOKIES.get('visit_count', '0')

    return render(request, 'get_cookie.html', {'visit_count': visit_count})