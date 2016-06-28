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
            if response['next']:
                while response['next']:
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
                                filmresponse = requests.get(newurl).json()
                                print(filmresponse['title'])
                            # Species
                            print("""
Species
                                        """)
                            species = people['species']
                            for url in species:
                                urlresponse = requests.get(url).json()
                                print(urlresponse['name'])

                            # Vehicles
                            print("""
Vehicles
                                        """)
                            vehicleslist = people['vehicles']
                            for url in vehicleslist:
                                vehicleresponse = requests.get(url).json()
                                print(vehicleresponse['name'])
                            # Starships
                            print("""
Starships
                                        """)
                            starshipslist = people['starships']
                            for url in starshipslist:
                                starshipresponse = requests.get(url).json()
                                print(starshipresponse['name'])
                    url = response['next']
                    response = requests.get(url).json()

            else:
                for people in response['results']:
                    if people['name'] == namesearch:
                        print(people['name'])
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
                                    filmresponse = requests.get(newurl).json()
                                    print(filmresponse['title'])
                                # Species
                                print("""
    Species
                                            """)
                                species = people['species']
                                for url in species:
                                    urlresponse = requests.get(url).json()
                                    print(urlresponse['name'])

                                # Vehicles
                                print("""
    Vehicles
                                            """)
                                vehicleslist = people['vehicles']
                                for url in vehicleslist:
                                    vehicleresponse = requests.get(url).json()
                                    print(vehicleresponse['name'])
                                # Starships
                                print("""
    Starships
                                            """)
                                starshipslist = people['starships']
                                for url in starshipslist:
                                    starshipresponse = requests.get(url).json()
                                    print(starshipresponse['name'])

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
            url = 'http://swapi.co/api/vehicles/'
            response = requests.get(url).json()
            if response['next']:
                while response['next']:
                    for vehicle in response['results']:
                        if vehicle['name'] == vehiclesearch:
                            vehicleurl = vehicle['url']
                            vresponse = requests.get(vehicleurl).json()
                            print('Name')
                            print(vresponse['name'])
                            print('Model')
                            print(vresponse['model'])
                            print('Manufacturer')
                            print(vresponse['manufacturer'])
                            print('Cost in Credits')
                            print(vresponse['cost_in_credits'])
                            print('Length')
                            print(vresponse['length'])
                            print('Max Atmosphering Speed')
                            print(vresponse['max_atmosphering_speed'])
                            print('Crew')
                            print(vresponse['crew'])
                            print('Passengers')
                            print(vresponse['passengers'])
                            print('Cargo capacity')
                            print(vresponse['cargo_capacity'])
                            print('Consumables')
                            print(vresponse['consumables'])
                            print('Vehicle Class')
                            print(vresponse['vehicle_class'])
                            print('Pilots')
                            pilotsurl = vresponse['pilots']
                            for item in pilotsurl:
                                pilotresponse = requests.get(item).json()
                                print(response['name'])
                            print('Films Appeared In')
                            filmsurl = vresponse['films']
                            for item in filmsurl:
                                pilotresponse = requests.get(item).json()
                                print(pilotresponse['title'])
                            break
                    newurl = response['next']
                    response = requests.get(newurl).json()
            else:
                for vehicle in response['results']:
                    if vehicle['name'] == vehiclesearch:
                        vehicleurl = vehicle['url']
                        response = requests.get(vehicleurl).json()
                        print('Name')
                        print(response['name'])
                        print('Model')
                        print(response['model'])
                        print('Manufacturer')
                        print(response['manufacturer'])
                        print('Cost in Credits')
                        print(response['cost_in_credits'])
                        print('Length')
                        print(response['length'])
                        print('Max Atmosphering Speed')
                        print(response['max_atmosphering_speed'])
                        print('Crew')
                        print(response['crew'])
                        print('Passengers')
                        print(response['passengers'])
                        print('Cargo capacity')
                        print(response['cargo_capacity'])
                        print('Consumables')
                        print(response['consumables'])
                        print('Vehicle Class')
                        print(response['vehicle_class'])
                        print('Pilots')
                        pilotsurl = response['pilots']
                        for item in pilotsurl:
                            pilotresponse = requests.get(item).json()
                            print(pilotresponse['name'])
                        print('Films Appeared In')
                        filmsurl = response['films']
                        for item in filmsurl:
                            filmresponse = requests.get(item).json()
                            print(filmresponse['title'])
search_or_list()
