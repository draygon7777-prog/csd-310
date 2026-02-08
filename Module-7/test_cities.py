from city_country import get_formated_city

def test_city_country_info():
    """Do city and country entries work?"""
    formatted_city = get_formated_city('Santiago', 'Chile')
    assert formatted_city == 'Santiago, Chile'