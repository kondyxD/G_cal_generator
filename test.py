from API.GoogleCalAPI import GoogleCalAPI

API = GoogleCalAPI()

test = API.get_my_events('20-01-2020')

print(test)
