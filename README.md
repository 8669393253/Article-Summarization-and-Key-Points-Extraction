# Article Summarization and Key Points Extraction

This project provides two Python scripts for processing articles from URLs. The first script extracts key points (key phrases) from an article using the `spaCy` and `pytextrank` libraries, and the second script summarizes the article using the `transformers` library with a pre-trained model. Both scripts rely on the `newspaper3k` library to fetch the article content.

## Prerequisites

Before running the scripts, you need to install the following Python libraries:

- `spaCy` (for NLP tasks)
- `pytextrank` (for key phrase extraction)
- `newspaper3k` (for article fetching and parsing)
- `transformers` (for summarization with pre-trained models)
- `torch` (required for running models from the `transformers` library)

### Installation

1. Install the necessary Python libraries:

   pip install spacy pytextrank newspaper3k transformers torch


2. Download the `spaCy` model:

   python -m spacy download en_core_web_sm


### Usage

There are two separate scripts in this project. Below are instructions on how to use each.

## 1. Key Points Extraction using spaCy and pytextrank

### Description:
This script extracts the key points (key phrases) from an article using the `spaCy` NLP library and the `pytextrank` package for TextRank-based key phrase extraction.

# Example usage
url = input("Enter the URL of the article: ")
key_points = extract_key_points(url)

print("\nKey Points (Extracted Phrases):")
for point in key_points:
    print(f"- {point}")

### How to Run:

1. Run the script:

   python extract_key_points.py


2. Enter the URL of the article when prompted.
3. The script will output key phrases extracted from the article.


## 2. Article Summarization using Hugging Face Transformers

### Description:
This script summarizes an article using the `transformers` library and a pre-trained `DistilBART` model. The model is used to generate a concise summary of the input article. If the article exceeds the token limit for the model, it will be split into chunks and summarized separately.

# Example usage
url = input("Enter the URL of the article: ")
summary = extract_summary_with_transformers(url)

print("\nArticle Summary:")
print(summary)

### How to Run:

1. Run the script:

   python summarize_article.py


2. Enter the URL of the article when prompted.
3. The script will output a summary of the article.

## Additional Notes

- **Error Handling**: Both scripts have basic error handling in place to manage common issues such as connectivity problems or invalid URLs.
- **Article Length**: The summarization script splits long articles into smaller chunks for processing, as the DistilBART model has a token limit of 1024 tokens. If the article exceeds this length, it will be processed in chunks to generate a coherent summary.
  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
