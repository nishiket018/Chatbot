# utils/wikipedia_api.py
import wikipediaapi

def get_wikipedia_summary(query, language='english'):
    formatted_query = query.strip().replace(" ", "_").title()
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(formatted_query)
    if page.exists():
        return page.summary[:500]
    else:
        return f"Sorry, the topic '{query}' was not found on Wikipedia."
