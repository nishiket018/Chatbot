# utils/web_search.py
from dotenv import load_dotenv
import os
import requests
import re

# Load environment variables from the .env file
load_dotenv()

def search_web(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": os.getenv("GOOGLE_API_KEY"),
        "cx": os.getenv("SEARCH_ENGINE_ID"),
        "num": 5,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get('items', [])
        if not results:
            raise Exception("No relevant search results found. Try refining your search.")
        return results
    else:
        raise Exception(f"Error fetching search results: {response.status_code}, {response.text}")

def identify_query_type(query):
    # Regular expressions to identify query types
    if re.search(r'\b(compare|versus)\b', query, re.IGNORECASE):
        return "comparative_analysis"
    elif re.search(r'\b(how to|guide|tutorial)\b', query, re.IGNORECASE):
        return "guides_and_how_tos"
    elif re.search(r'\b(reviews|opinions|ratings)\b', query, re.IGNORECASE):
        return "reviews_and_opinions"
    elif re.search(r'\b(live|weather|score|stock)\b', query, re.IGNORECASE):
        return "real_time_data"
    elif re.search(r'\b(who is|biography|born|death|died)\b', query, re.IGNORECASE):
        return "person_query"
    else:
        return "general_info"

def format_results(results, query_type, query):
    formatted = ""

    if query_type == "person_query":
        main_info = next((item for item in results if 'wikipedia' in item.get('link', '').lower()), results[0])
        formatted += f"### Detailed Information about '{query}'\n\n"
        intro = main_info.get('snippet', 'Snippet unavailable')
        formatted += f"{intro}\n\n"
        formatted += "#### Additional Information:\n\n"
        for result in results[1:4]:  # Use up to 3 additional sources for expanded detail
            formatted += f"{result.get('snippet', '')} "
        formatted += f"\n\n[📘 Read more on Wikipedia or related sources]({main_info.get('link')})\n\n"

    elif query_type == "guides_and_how_tos":
        formatted += f"### Guides and Tutorials on '{query}'\n\n"
        for result in results[:5]:  
            formatted += f"- **{result.get('title')}**\n  {result.get('snippet')}\n  [📖 Read more]({result.get('link')})\n\n"

    elif query_type == "comparative_analysis":
        formatted += f"### Comparative Analysis for '{query}'\n\n"
        for idx, result in enumerate(results[:5]):  
            formatted += f"{idx + 1}. **{result.get('title')}**\n   {result.get('snippet')}\n   [🔗 Link]({result.get('link')})\n\n"

    elif query_type == "reviews_and_opinions":
        formatted += f"### Reviews and Opinions on '{query}'\n\n"
        for result in results[:5]:  
            formatted += f"- **{result.get('title')}**\n  {result.get('snippet')}\n  [Read more]({result.get('link')})\n\n"

    else:
        formatted += f"### General Information on '{query}'\n\n"
        for result in results[:5]:  
            formatted += f"- **{result.get('title')}**\n  {result.get('snippet')}\n  [Read more]({result.get('link')})\n\n"

    return formatted
