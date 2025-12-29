import requests
from bs4 import BeautifulSoup
from .models import Article

def scrape_beyondchats():
    url = "https://beyondchats.com/blogs/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch page")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select("article")[-5:]  # last 5 (oldest)

    saved_articles = []

    for article in articles:
        title_tag = article.find("h2")
        link_tag = article.find("a")

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]

        # Avoid duplicates
        if Article.objects.filter(source_url=link).exists():
            continue

        obj = Article.objects.create(
            title=title,
            content="Content will be scraped later",
            source_url=link
        )

        saved_articles.append(obj.title)

    return saved_articles
