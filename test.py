from API.GoogleCalAPI import GoogleCalAPI

API = GoogleCalAPI()

test = API.create_event('20-01-2020', 'testuju', 1, 'hours', ['test','jeb'],'test@gmail.com',
                        'hele zkouším')

print(test)
