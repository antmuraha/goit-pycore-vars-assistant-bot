import nltk
from rake_nltk import Rake

def run_nltk_downloader():
    nltk.download()

def check_and_download_resources():
    try:
        r = Rake()
        r.extract_keywords_from_text('')
        r.get_ranked_phrases()
    except:
        nltk.download('stopwords')
        nltk.download('punkt_tab')


def extract_keywords(text: str) -> list[tuple[float, str]]:
    try:
        check_and_download_resources()
        r = Rake()

        # # # Extraction given the text.
        r.extract_keywords_from_text(text)

        # To get keyword phrases ranked highest to lowest with scores.
        ranked = r.get_ranked_phrases_with_scores()
        return ranked
    except Exception as e:
        return []
