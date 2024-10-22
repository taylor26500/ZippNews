import cohere

def create_news_txt(news_dict):
    all_news_string = ""
    for index, news in news_dict.items():
        all_news_string += f"The is the start of the number {index} news:\nHeadline: {news['headline']}\nContent: {news['content']}\n\n"
    return all_news_string

def call_cohere_api(api_key, model, message, temperature=0, seed=None):
    co = cohere.Client(api_key=api_key)
    response = co.chat(
        model=model,
        message=message,
        temperature=temperature,
        preamble="Please start your response by providing direct answers immediately, omitting any introductory phrases.",
        seed=seed
    )
    input_tokens = response.meta.tokens.input_tokens
    output_tokens = response.meta.tokens.output_tokens
    return response.text, input_tokens, output_tokens
