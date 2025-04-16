import requests
from pprint import pprint

import requests

import requests

def get_synonyms(word):
    """
    Fetches a list of synonyms for the specified word from the Free Dictionary API.

    Parameters:
        word (str): The word to look up.

    Returns:
        list: A list of synonyms if found, otherwise an empty list.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        synonyms = []
        for entry in data:
            for meaning in entry.get('meanings', []):
                # Check for synonyms in the 'synonyms' field of each meaning
                synonyms.extend(meaning.get('synonyms', []))
            # Also check for synonyms at the top level of the entry
            synonyms.extend(entry.get('synonyms', []))
        return synonyms
    else:
        print(f"Error: Unable to fetch synonyms for '{word}'. Status Code: {response.status_code}")
        return []



def get_flesch_reading_ease(text_to_analyze):
    API_KEY = 'XML8YHNY280YY27NSTTBVO4Y971TR9L0'

    # API endpoint
    url = "https://api.sapling.ai/api/v1/statistics"

    # Request payload
    payload = {
        "key": API_KEY,
        "text": text_to_analyze,
        "lang": "en"  # Optional: specify language code (e.g., 'en' for English)
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the response JSON
        data = response.json()
        return(data.get('readability_scores', {}).get('flesch_reading_ease'))
    else:
        print("Error, flesh reading api error")
        return(0)


def trim_connectors(text_to_trim):
    connectors = {
        "it", "and", "am", "for",  "will", "that", "as", "a", "an", "of", "which", "for", "the", "is", 
        "what", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
        "do", "does", "did", "would", "shall", "should", "can", "could", 
        "may", "might", "must", "at", "by", "from", "to", "with", "in", 
        "on", "over", "under", "through", "because", "while", "if", "then", 
        "so", "though", "although", "just", "really", "very", "kind", 
        "like", "maybe", "perhaps", "even", "only", "still", "actually", 
        "basically"
    }
    words = text_to_trim.split()
    trimmed_words = [word for word in words if word.lower().strip(".,!?\"'") not in connectors]
    return ' '.join(trimmed_words)


def get_best_synonym(word):
    synonyms = get_synonyms(word)

    best_synonym = None
    highest_score = -float('inf') 

    for synonym in synonyms:
        score = get_flesch_reading_ease(synonym)
        if score is not None and score > highest_score:
            highest_score = score
            best_synonym = synonym

    return best_synonym

def replace_words_with_best_synonyms(text):
    """
    Replaces each word in the input text with its best synonym based on the Flesch Reading Ease score.
    """
    words = text.split()
    updated_words = []

    for word in words:
        if word.lower() == "i":
            updated_words.append("Me")
        elif word.lower() == "not":
            updated_words.append("not")
        else:
            best_synonym = get_best_synonym(word)
            if best_synonym:
                updated_words.append(best_synonym)
            else:
                updated_words.append(word)

    updated_text = ' '.join(updated_words)
    return updated_text

def remove_after_apostrophe(text):
    """
    For every word in the text, removes the apostrophe and any characters following it.

    Parameters:
        text (str): The input text.

    Returns:
        str: The modified text with parts of words after an apostrophe removed.
    """
    words = text.split()
    new_words = []
    
    for word in words:
        if "'" in word:
            # Find the index of the first apostrophe and take only the substring before it.
            idx = word.find("'")
            trimmed = word[:idx]
            # If trimming leaves an empty string, you can choose to exclude it.
            if trimmed:
                new_words.append(trimmed)
        else:
            new_words.append(word)
    
    return ' '.join(new_words)

examples = [
    "Allen has mistaken me for his friend Marcus Halberstam. It seems logical because Marcus also works at P&P and in fact does the same exact thing I do and he also has a penchant for Valentino suits and Oliver Peoples glasses. Marcus and I even go to the same barber, although I have a slightly better haircut.",
    "As you all know, first prize is a Cadillac Eldorado. Anybody wanna see second prize? Second prize's a set of steak knives. Third prize is you're fired.",
    "The good news is Vinnie, you're not going to care cause you're gonna make so much money. That's what I get out of it. Wanna know what you get out of it? You get the ice cream, the hot fudge, the banana and the nuts. Right now I get the sprinkles, and you- if this goes through, I get the cherry. But you get the sundae, Vinny. You get the sundae.",
    "And I'll bet what you hated the most was that they identified me as a co-founder of Facebook, which I am. You better lawyer up asshole, because I'm not coming back for 30%, I'm coming back for everything.",
    "Because the man who makes an appearance in the business world, the man who creates personal interest, is the man who gets ahead. Be liked and you will never want. I never have to wait in line to see a buyer."
]

for example in examples:
    updated_text = trim_connectors(example)
    print("After trim_connectors:", updated_text)

    updated_text = remove_after_apostrophe(updated_text)
    print("After remove apostrophe:", updated_text)
    # Then, replace words with their best synonyms
    updated_text = replace_words_with_best_synonyms(updated_text)
    print("After replace_with_best_synonyms:", updated_text)