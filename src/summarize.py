from src.utils import create_news_txt, call_cohere_api
from src.config import API_KEY, MODEL

def summarize_news(news_txt):
    news_txt = create_news_txt(news_txt)
    prompt = f"""
        # Role: 
        You are a professional and insightful journalist tasked with summarizing multiple news items.

        # Task Overview:
        You will receive a document containing 10 distinct news items, each marked with a sentence that says: "This is the start of news number {{i}}," where i ranges from 1 to 10.
        Your job is to summarize the Content for each news item while preserving the Headline as it is. 
        Each summary should concisely capture the essence of the content without introducing extraneous information.

        # Guidelines:
        ## Summarize based on the Headline and Content:

        1. Only use the relevant details found directly in the "Content" section to craft your summary.
        2. Ensure the summary reflects the core message or most important information from the Content.
        
        ## Restriction: 
        1. Keep each summary around 60 words.
        2. Be concise yet informative, ensuring that each summary communicates the key points effectively.
        
        ## Preserve the Headline:
        1. The Headline should remain unchanged. Only summarize the Content.
        2. Do not alter the format or remove the Headline.

        ## Focus on Accuracy:
        1. Ensure that the summarized content stays true to the original meaning.
        2. Avoid adding personal interpretations, opinions, or irrelevant details.
        
        ## Replacement of Original Content:
        1. After summarizing each news item, replace the original Content with your summary.
        2. The new text should consist of the unaltered Headline followed by your summarized Content.
        
        ## Example of Format:
        Headline: [Leave this exactly as it appears in the document]
        Content: [Insert your concise summary here]

        ## Additional Considerations:
        1. Consistency: Maintain a neutral and professional tone throughout the summaries.
        2. Avoid Redundancy: Ensure that no repetitive or unnecessary information is included.

        # Document for Summarization:
        Here is the text containing all 10 news items:
        {news_txt}
    """
    response, input_tokens, output_tokens = call_cohere_api(
        api_key=API_KEY,
        model=MODEL,
        message=prompt,
        temperature=0,
        seed=42
    )
    print(response)
    exit()
    return response, input_tokens, output_tokens