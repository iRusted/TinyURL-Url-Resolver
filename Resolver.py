import random
import requests 
import time

request_count = 0 
valid_urls_found = 0

letters_and_numers = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",

    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def get_url_end():
    url_end = random.choices(letters_and_numers, k=8)
    
    
    url_end = ''.join(url_end)
    
    return url_end

def create_url():
    url_end = get_url_end()
    
    url = "https://www.tinyurl.com/" + url_end
    
    return url 

def check_url():
    url = create_url()
    global valid_urls_found
    global request_count
    
    try: 
        response = requests.get(url, timeout=30)
    except requests.exceptions.Timeout:
        print(f"URL {url} Has Timed Out! Aborting Attempts for this URL!\n")
        request_count += 1   
        return 
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}. Skipping {url}\n")
        request_count += 1   
        return
    
    if response.status_code == 404:
        with open("invalid_urls.txt", "a", encoding="utf-8") as file: 
            file.write(f"{url}\n")
        request_count += 1     
    elif response.status_code == 200:
        with open("valid_urls.txt", "a", encoding="utf-8") as file: 
            file.write(f"{url}\n")
        print(f"Found one! URL: {url} is Valid!\n")
        valid_urls_found += 1
        request_count += 1
            
    elif response.status_code == 429:
        print("CRITICAL ALERT: RATE LIMIT HIT. PAUSING FOR 5 MINUTES")
        time.sleep(300)
        
    else:
        with open("other_urls.txt", "a", encoding="utf-8") as file: 
            file.write(f"{url}\n")
            request_count += 1   

try:
    while True:
        check_url()
        time.sleep(2.5)

except KeyboardInterrupt:
    print(f"\nExperiment stopped by user.")
    print(f"Total attempts: {request_count}")
    print(f"Total Number of Valid URLs: {valid_urls_found}")