import random

# Function to generate a random string of 6 characters
def generate_short_url():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(6))

# Dictionary to store the original URLs and their shortened versions
url_dict = {}

# Function to create a shortened URL and store it in the dictionary
def shorten_url(url):
    short_url = generate_short_url()
    url_dict[short_url] = url
    return short_url

# Function to retrieve the original URL from the dictionary
def get_original_url(short_url):
    return url_dict.get(short_url)

# Example usage:
url = "https://www.example.com/very/long/url/to/be/shortened"
short_url = shorten_url(url)
print("Shortened URL:", short_url)
original_url = get_original_url(short_url)
print("Original URL:", original_url)
