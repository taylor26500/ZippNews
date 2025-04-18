# ZippNews
ZippNews is a Python application designed to scrape, summarize, and display news articles. This project utilizes web scraping techniques to gather news data and leverages the Cohere API to generate concise summaries of each article.

## Features
- **News Scraping**: Fetches the latest news.
- **News Summarization**: Summarizes the news articles using a pre-trained model from Cohere, focusing on key content while preserving the original headlines.

## Project Structure
```plaintext
ZippNews/
├── src/
│   ├── scraper.py        # Module to scrape news
│   ├── summarize.py      # Module to summarize the scraped news content
│   └── utils.py          # Utility functions supporting news text formatting and API communication
└── main.py               # Main application script
```

## Usage
To run the ZippNews application, execute the following command from the root directory of the project:

```bash
python main.py
```

This will scrape the news, summarize it, and print the summaries to the console.

## Installation

To set up the project environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github/ZippNews.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. For more details, see the [LICENSE.md](LICENSE.md) file.
