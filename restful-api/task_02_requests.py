import requests
import csv


def fetch_and_print_posts():
    """Fetches posts and prints titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        for post in response.json():
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts and saves them to a CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(response.json())
