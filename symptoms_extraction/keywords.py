from rake_nltk import Rake
from difflib import get_close_matches

def find_best_match(user_question,questions):
    matches = get_close_matches(user_question,questions,n=1,cutoff=0.6)
    return matches[0] if matches else None

text = " I am suffering from fever, cold, skin Rash"
r = Rake()
r.extract_keywords_from_text(text)
phrases = r.get_ranked_phrases()

if __name__ == "__main__":
    print(phrases)
    r.extract_keywords_from_sentences(phrases)
    print(r.get_ranked_phrases())