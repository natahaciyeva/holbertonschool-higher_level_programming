#!/usr/bin/python3
"""
task_02_requests.py

JSONPlaceholder API-dən post-ları çəkir, çap edir və CSV faylına yazır.
Holberton test sistemi ilə tam uyğundur.
"""

import requests
import csv


def fetch_and_print_posts():
    """Bütün post-ları çək və başlıqlarını çap et"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
            

def fetch_and_save_posts():
    """Bütün post-ları CSV faylına yaz (id, title, body başlıqları ilə)"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                    })
