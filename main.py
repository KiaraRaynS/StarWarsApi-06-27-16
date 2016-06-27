import requests

# base url for reference: http://swapi.co/api/

userresponse = int(input("""What do you wish to view?
(1) - Characters
(2) - Films
(3) - Vehicles
"""))

list_choices = {
        1: ["http://swapi.co/api/people/", 'name'],
        2: ['http://swapi.co/api/films/', 'title'],
        3: ['http://swapi.co/api/vehicles/', 'name'],
        }


def print_results(response, printkey):
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[printkey])
            nextpage = input('Do you wish to see the next page of results? Y/N ').upper()
            if nextpage == 'Y':
                url = response['next']
                response = requests.get(url).json()
            else:
                break
    else:
        for item in response['results']:
            print(item[printkey])

# characters
if userresponse == 1:
    url = 'http://swapi.co/api/people/'
    response = requests.get(url).json()
    printkey = 'name'
    print_results(response, printkey)


# films
if userresponse == 2:
    url = 'http://swapi.co/api/films/'
    response = requests.get(url).json()
    printkey = 'title'
    print_results(response, printkey)

# vehicles
if userresponse == 3:
    url = 'http://swapi.co/api/vehicles/'
    response = requests.get(url).json()
    printkey = 'name'
    print_results(response, printkey)
