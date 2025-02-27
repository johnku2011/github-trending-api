import requests
from bs4 import BeautifulSoup

def get_trending_repositories(time_frame="daily"):
    """
    Fetches trending repositories from GitHub based on the specified time frame.

    Args:
        time_frame (str): The time frame for trending repositories. Must be 'daily', 'weekly', or 'monthly'.

    Returns:
        list: A list of dictionaries containing repository information (owner, repo_name, language, stars).

    Raises:
        ValueError: If the time_frame is not 'daily', 'weekly', or 'monthly'.
        Exception: If the HTTP request to fetch the page fails.
    """
    # Validate the time_frame input
    if time_frame not in ["daily", "weekly", "monthly"]:
        raise ValueError("Invalid time_frame. Must be 'daily', 'weekly', or 'monthly'.")

    # Construct the URL based on the time frame
    url = f"https://github.com/trending?since={time_frame}"
    
    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all repository articles
    repo_articles = soup.find_all("article", class_="Box-row")

    # List to store repository information
    repositories = []

    # Process each repository article
    for article in repo_articles:
        # Extract owner and repository name
        h2 = article.find("h2", class_="h3 lh-condensed")
        owner = None
        repo_name = None
        if h2:
            owner_span = h2.find("span", class_="text-normal")
            if owner_span:
                owner = owner_span.get_text(strip=True).strip("/")
                # Get the text after the span for repo name
                repo_name = h2.contents[-1].strip()

        # Extract programming language (type of project)
        language_span = article.find("span", itemprop="programmingLanguage")
        language = language_span.get_text(strip=True) if language_span else None

        # Extract star count
        stars_a = article.find("a", class_="Link--muted d-inline-block mr-3")
        stars = None
        if stars_a:
            stars_text = stars_a.get_text(strip=True).replace(",", "")
            if "k" in stars_text:
                stars = int(float(stars_text.replace("k", "")) * 1000)
            else:
                stars = int(stars_text)

        # Store the extracted information in a dictionary
        repositories.append({
            "owner": owner,
            "repo_name": repo_name,
            "language": language,
            "stars": stars
        })

    return repositories

# Example usage
if __name__ == "__main__":
    # Fetch trending repositories for different time frames
    for period in ["daily", "weekly", "monthly"]:
        print(f"\nTrending repositories ({period}):")
        trending_repos = get_trending_repositories(period)
        for repo in trending_repos[:5]:  # Display first 5 for brevity
            print(f"Owner: {repo['owner']}, Repo: {repo['repo_name']}, "
                  f"Language: {repo['language']}, Stars: {repo['stars']}")