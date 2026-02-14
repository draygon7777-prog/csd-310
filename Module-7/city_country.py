def get_formated_city(city, country, population='', language=''):
    """Generate a formatted city and country"""
    full_city = f"{city}, {country}"
    """population = kwargs.get('population')
    language = kwargs.get('language')"""
    if population:
        full_city = f"{full_city} - population {population}"
    if language:
        full_city = f"{full_city}, language={language}"
    return full_city