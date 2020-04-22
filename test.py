from API.GoogleCalAPI import GoogleCalApi

API = GoogleCalAPI()

my_calendars = API.get_my_calendars()

print(my_calendars)
