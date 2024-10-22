import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the section for "Most viewed"
    most_read_section = soup.find('section', attrs={'data-testid': 'illinois-section-outer-10'})
    cards = most_read_section.find_all('div', attrs={'data-testid': 'cambridge-card'})

    news_dict = {}
    for card in cards:
        news_index = card.find('span', attrs={'data-testid': 'card-order'}).get_text(strip=True)
        headline = card.find('h2', attrs={'data-testid': 'card-headline'}).get_text(strip=True)
        link_tag = card.find('a', attrs={'data-testid': 'internal-link'})
        website = "https://www.bbc.com" + link_tag['href']
        
        # Fetch the article page
        article_response = requests.get(website)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        article_tag = article_soup.find('main', id='main-content').find('article')
        text_blocks = article_tag.find_all('div', attrs={'data-component': 'text-block'})
        content = ' '.join(block.get_text(strip=True) for block in text_blocks)

        news_dict[news_index] = {
            'headline': headline,
            'content': content,
            'website': website
        }

    return news_dict

#     url = 'https://news.now.com/home/local'
#     url = 'https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E'
