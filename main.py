from src.scraper import scrape_bbc_news
from src.summarize import summarize_news

def main():
    bbc_news = scrape_bbc_news()
    bbc_news = summarize_news(bbc_news)

if __name__ == "__main__":
    main()