import requests
from bs4 import BeautifulSoup

def check_exact_business_name(name):
    url = "https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults"
    params = {
        'searchTerm': name,
        'searchNameOrder': name + "%20%20%20%20%20%20%20%20%20%20%20%20",
        'entityType': 'ALL',
        'searchType': 'Search'
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error: Unable to reach Sunbiz website.")
        return False

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr')

    print("Rows Found:")
    for row in rows:
        cells = row.find_all('td')
        if cells:
            business_name_text = cells[0].get_text(strip=True)
            print(business_name_text)
            if business_name_text.upper() == name.upper():
                print(f"The business name '{name}' is already in use as an exact match.")
                return True

    print(f"The business name '{name}' is available as an exact match.")
    return False

def main():
    while True:
        business_name = input("enter business: ")
        if business_name.lower() == 'exit':
            print("Exiting the program.")
            break
        check_exact_business_name(business_name)

main()
