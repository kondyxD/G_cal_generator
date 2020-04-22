from API.GoogleCalAPI import GoogleCalAPI

API = GoogleCalAPI()

my_calendars = API.get_my_events()

print(my_calendars)
