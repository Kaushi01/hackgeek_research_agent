import requests
from bs4 import BeautifulSoup

def fetch_source_content(url: str, timeout: int = 10) -> dict:
    """
    Fetches and cleans text content from a URL.
    Returns: { url, title, full_text, success }
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and styles
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        title = soup.title.string.strip() if soup.title else "No Title"
        full_text = soup.get_text(separator="\n", strip=True)

        return {
            "url": url,
            "title": title,
            "full_text": full_text[:8000],  # limit to avoid token overload
            "success": True
        }

    except Exception as e:
        print(f"[fetch_sources] Failed to fetch {url}: {e}")
        return {
            "url": url,
            "title": "",
            "full_text": "",
            "success": False
        }