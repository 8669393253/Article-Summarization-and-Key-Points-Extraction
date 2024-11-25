import spacy
import pytextrank
from newspaper import Article

# Load spaCy and add pytextrank
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")

def fetch_article_text(url):
    # Download and parse the article
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def extract_key_points(url):
    try:
        # Fetch article content
        article_text = fetch_article_text(url)
        
        # Process the text using spaCy pipeline
        doc = nlp(article_text)
        
        # Extract key phrases using TextRank
        key_points = []
        for phrase in doc._.phrases:
            key_points.append(phrase.text)
        
        return key_points
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
url = input("Enter the URL of the article: ")
key_points = extract_key_points(url)

print("\nKey Points (Extracted Phrases):")
for point in key_points:
    print(f"- {point}")
