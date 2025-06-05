import webbrowser
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(error_message):
    print(f"Error: {error_message}")

def display_search_options():
    options = """
1 - Username
2 - Last Name, First Name
3 - General Search
    """
    print(options)

def get_search_input(search_type):
    if search_type in ['1', '01']:
        return input("Enter Username: ")
    elif search_type in ['2', '02']:
        last_name = input("Enter Last Name: ")
        first_name = input("Enter First Name: ")
        return f"{last_name} {first_name}"  # Return as a single string
    elif search_type in ['3', '03']:
        return input("Enter Search Query: ")
    else:
        raise ValueError("Invalid search type")

def display_site_options():
    options = """
1 - Facebook.com
2 - Youtube.com
3 - Twitter.com
4 - Tiktok.com
5 - Peekyou.com
6 - Tumblr.com
7 - PagesJaunes.fr
    """
    print(options)

def generate_search_url(site, search_terms):
    base_urls = {
        '1': "https://www.facebook.com/search/top/?init=quick&q=",
        '2': "https://www.youtube.com/results?search_query=",
        '3': "https://twitter.com/search?f=users&vertical=default&q=",
        '4': "https://www.tiktok.com/search?q=",
        '5': "https://www.peekyou.com/",
        '6': "https://www.tumblr.com/search/",
        '7': "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="
    }
    
    url = base_urls.get(site, '')
    
    if site == '5':
        # Peekyou has a different URL structure
        url = f"{url}{search_terms.replace(' ', '_')}"
    else:
        url += search_terms
    
    webbrowser.open(url)

def main():
    try:
        while True:  # Added loop to allow multiple searches
            clear()
            display_search_options()
            search_type = input("Select Search Type (or 'q' to quit): ")
            
            if search_type.lower() == 'q':
                break
                
            search_terms = get_search_input(search_type)
            
            while True:
                clear()
                display_site_options()
                site_choice = input("Select Site (or 'b' to go back): ")
                
                if site_choice.lower() == 'b':
                    break
                elif site_choice in ['1', '2', '3', '4', '5', '6', '7']:
                    generate_search_url(site_choice, search_terms)
                else:
                    print("Invalid site choice. Please select a valid option.")
                    input("Press Enter to continue...")
    
    except Exception as e:
        handle_error(e)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
