#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        print(f"Status code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(f"{post['id']}")
            print(f"{post['title']}")
            print(f"{post['body']}")
            print("--------------------")
    else:
        print(f"Status code: {response.status_code}")


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        header = posts[0].keys()
        with open('posts.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(header)

            for post in posts:
                writer.writerow(post.values())
    else:
        print(f"Status code: {response.status_code}")
