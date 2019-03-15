import re
import wikipedia

def search(input_text):
    try:
        wiki_data = wikipedia.summary(input_text, sentences=5)
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)
            wiki_data = wiki_data.replace("'", "")
        return wiki_data
    except wikipedia.exceptions.DisambiguationError:
        return 'Can you please be more specific? I could not find what you asked for.'