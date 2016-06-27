import requests

# base url for reference: http://swapi.co/api/


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

list_choices = {
        1: ["http://swapi.co/api/people/", 'name'],
        2: ['http://swapi.co/api/films/', 'title'],
        3: ['http://swapi.co/api/vehicles/', 'name'],
        }


def search_or_list():
    startresponse = int(input("""What would you like to do?
    (1) - View list
    (2) - Search for specific item
    """))
    # View List Options
    if startresponse == 1:
        userresponse = int(input("""What do you wish to view?
        (1) - Characters
        (2) - Films
        (3) - Vehicles
        """))

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
    # Search Options
    if startresponse == 2:
        searchresponse = int(input("""What would you like to search for?
        (1) - Character
        (2) - Film
        (3) - Vehicle
        """))
        # Search for Character
        if searchresponse == 1:
            url = 'http://swapi.co/api/people/'
            response = requests.get(url).json()
            namesearch = input("Who do you wish to see? ").title()
            for people in response['results']:
                if people['name'] == namesearch:
                    print(people['name'])
                    # Films they were in
                    print("""
Films
                            """)
                    filmslist = people['films']
                    for filmurl in filmslist:
                        newurl = filmurl
                        response = requests.get(newurl).json()
                        print(response['title'])
                    # Species
                    print("""
Species
                            """)
                    species = people['species']
                    for url in species:
                        response = requests.get(url).json()
                        print(response['name'])
                    # Vehicles
                    print("""
Vehicles
                            """)
                    vehicleslist = people['vehicles']
                    for url in vehicleslist:
                        response = requests.get(url).json()
                        print(response['name'])
                    # Starships
                    print("""
Starships
                            """)
                    starshipslist = people['starships']
                    for url in starshipslist:
                        response = requests.get(url).json()
                        print(response['name'])
        # Search for Movie
        if searchresponse == 2:
            titlesearch = input('What movie do you wish to see? ').title()
            url = 'http://swapi.co/api/films/'
            response = requests.get(url).json()
            for film in response['results']:
                if film['title'] == titlesearch:
                    print('Found')
                    filmurl = film['url']
                    response = requests.get(filmurl).json()
                    # Opening Crawl
                    print("""
Opening Crawl
                            """)
                    print(response['opening_crawl'])
                    # Release Date
                    print("""
Release Date
                    """)
                    print(response['release_date'])

        # Search for Vehicle
        if searchresponse == 3:
            vehiclesearch = input('What vehicle do you wish to see? ')
            print(vehiclesearch)

search_or_list()
