import requests
from bs4 import BeautifulSoup

def scrape_duke_classes():
    base_url = "https://www.coursicle.com/duke/courses/"

    try:
        response = requests.get(base_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        class_sections = soup.find_all('div', class_='course')

        with open("duke_classes.txt", "w", encoding="utf-8") as file:
            for course in class_sections:
                title = course.find('h2').text if course.find('h2') else "Unknown Title"
                description = course.find('p').text if course.find('p') else "No Description"

                file.write(f"Course Title: {title}\n")
                file.write(f"Description: {description}\n\n")

        print("Scraping complete. Data saved to 'duke_classes.txt'.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_duke_classes()