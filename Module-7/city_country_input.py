from city_country import get_formated_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city =='q':
        break
    country = input("Please give me the city's country: ")
    if country == 'q':
        break
    population = input("(optional) Please enter the population: ")
    if population == 'q':
        break
    language = input("(optional) Please enter the language: ")
    if language == 'q':
        break

    formatted_city = get_formated_city(city, country)
    print(f"\tFormatted city info: {formatted_city}")