from transformers import pipeline, AutoTokenizer
from newspaper import Article

# Initialize the summarization pipeline
summarizer = pipeline("summarization")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def fetch_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def extract_summary_with_transformers(url):
    try:
        article_text = fetch_article_text(url)
        
        # Tokenize the text and check the length
        inputs = tokenizer(article_text, return_tensors="pt", truncation=False, padding=False)
        token_length = len(inputs['input_ids'][0])

        # If the token length exceeds the max limit, split the text into smaller chunks
        max_token_length = 1024  # Standard for many models like DistilBART
        if token_length > max_token_length:
            # Split the article into chunks
            chunk_size = max_token_length - 100  # leaving some room for special tokens
            chunks = [article_text[i:i + chunk_size] for i in range(0, len(article_text), chunk_size)]
        else:
            chunks = [article_text]

        # Get summary for each chunk
        summary = ""
        for chunk in chunks:
            chunk_summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
            summary += chunk_summary[0]['summary_text'] + " "

        return summary.strip()

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
url = input("Enter the URL of the article: ")
summary = extract_summary_with_transformers(url)

print("\nArticle Summary:")
print(summary)
