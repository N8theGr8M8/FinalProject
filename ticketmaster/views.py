from django.shortcuts import render, redirect
from .models import EventData
import requests
from datetime import datetime
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        classification = request.POST['searchTerm']
        city = request.POST['place']
        print(classification)
        print(city)



        if not classification or not city:
            messages.info(request, 'Both city and classification are required fields.')
            return redirect('ticketmaster-base')
            # Add code to handle or display the error_message as needed.

        # call get_events function() to get the data from the API
        results = get_results(city, classification)

        # If the request to fetch data was unsuccessful or returned None
        if results['page']['totalElements'] == 0:
            # Set up an error message using Django's message utility to inform the user
            messages.info(request, 'No results were found. Sorry!')
            # redirect user
            return redirect('ticketmaster-base')

        else:
            # print the response for testing purpose (open "Run" at the bottom to see what is printed)
            print(results)
            # Store each user's information in a variable
            events = results['_embedded']['events']

            # Initialize an empty list to store user data
            event_list = []

            # Iterate through each user in the 'users' list coming from the api
            # Rather than directly passing the "users" array to the template,
            # the following approach allows server-side processing and formatting of specific data (e.g., date).
            # So, the template only needs to plug in the preprocessed information.
            for event in events:
                # Extract relevant information from the user dictionary
                name = event['name']
                most_pixels = 0
                best_image = ""
                for image in event['images']:
                    if image['height'] * image['width'] > most_pixels:
                        best_image = image['url']
                        most_pixels = image['height'] * image['width']

                # date_time = event['dates']['start']['dateTime']
                start_date = event['dates']['start']['localDate']
                if event['dates']['start']['noSpecificTime'] == False:
                    start_time = event['dates']['start']['localTime']
                else:
                    start_time = "No Specific Time"
                venue_name = event['_embedded']['venues'][0]['name']
                venue_address = event['_embedded']['venues'][0]['address']['line1']
                venue_city = event['_embedded']['venues'][0]['city']['name']
                venue_state = event['_embedded']['venues'][0]['state']['name']
                link = event['url']

                # Create a new dictionary to store user details
                event_details = {
                    'name': name,
                    'image': best_image,
                    'time': start_time,
                    'date': start_date,
                    'venue': venue_name,
                    'address': venue_address,
                    'city': venue_city,
                    'state': venue_state,
                    'link': link
                }

                # Append the user details dictionary to the user_list
                event_list.append(event_details)

            # Create a context dictionary with the user_list and render the 'index.html' template
            context = {'events': event_list}
            return render(request, 'ticketmaster/index.html', context)

        # all other cases, just render the page without sending/passing any context to the template
    return render(request, 'ticketmaster/index.html')


def get_results(city, classification):
    try:
        # Construct the URL with parameters
        url = "https://app.ticketmaster.com/discovery/v2/events.json"
        params = {
            "apikey": "avzKHs5iReHE4MkC3J6AhKRFsak9nrr0",
            "classificationName": classification,
            "city": city,
            "sort": "date,asc"
        }
        # Send a GET request to the specified URL with parameters
        response = requests.get(url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network issues, timeouts)
        print(f"Request failed: {e}")

        # Return None to indicate failure
        return None


def lister(request):
    if request.method == 'POST':
        savedEvent = request.POST['savedEvent']
        print(savedEvent)
        EventData.objects.create(name=savedEvent)
        return redirect('ticketmaster-base')
    else:
        events = EventData.objects.all()
        context = {'events' : events}
        return render(request, 'ticketmaster/list.html', context)
