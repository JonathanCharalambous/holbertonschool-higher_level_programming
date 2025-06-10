import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')


    print("Status Code:", r.status_code)
    print(r.json())
    print(r.headers)

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    p = r.json()

    posts = [
        {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        for post in p
    ]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts)


if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
