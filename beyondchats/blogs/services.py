from blogs.scraper import scrape_beyondchats
from blogs.models import Article

def save_articles_to_db():
    scraped_articles = scrape_beyondchats()

    for item in scraped_articles:
        Article.objects.get_or_create(
            title=item["title"],
            defaults={
                "content": "",
                "source_url": item["link"]
            }
        )

    return "Articles saved successfully"
