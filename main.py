import requests
from bs4 import BeautifulSoup

def get_trending_repositories(time_frame="daily"):
    """
    Fetches trending repositories from GitHub based on the specified time frame.

    Args:
        time_frame (str): The time frame for trending repositories. Must be 'daily', 'weekly', or 'monthly'.

    Returns:
        list: A list of dictionaries containing repository information (repo_name, link, language, stars, forks, description, stars_in_period).

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
        # Extract repository name and link
        h2 = article.find("h2", class_="h3 lh-condensed")
        repo_name = None
        link = None
        if h2:
            a_tag = h2.find("a")
            if a_tag and 'href' in a_tag.attrs:
                href = a_tag['href']
                link = "https://github.com" + href
                repo_name = href.split("/")[-1]

        # Extract programming language
        language_span = article.find("span", itemprop="programmingLanguage")
        language = language_span.get_text(strip=True) if language_span else "Unknown"

        # Extract total star count
        stars_a = article.find("a", href=lambda x: x and "stargazers" in x)
        stars = 0
        if stars_a:
            stars_text = stars_a.get_text(strip=True).replace(",", "")
            if "k" in stars_text:
                stars = int(float(stars_text.replace("k", "")) * 1000)
            else:
                stars = int(stars_text)

        # Extract fork count
        forks_a = article.find("a", href=lambda x: x and "forks" in x)
        forks = 0
        if forks_a:
            forks_text = forks_a.get_text(strip=True).replace(",", "")
            if "k" in forks_text:
                forks = int(float(forks_text.replace("k", "")) * 1000)
            else:
                forks = int(forks_text)

        # Extract description
        description_p = article.find("p", class_="col-9 color-fg-muted my-1 pr-4")
        description = description_p.get_text(strip=True) if description_p else ""

        # Extract stars gained in the specified time period
        stars_period_span = article.find("span", class_="d-inline-block float-sm-right")
        stars_in_period = 0
        if stars_period_span:
            stars_period_text = stars_period_span.get_text(strip=True)
            try:
                stars_in_period = int(stars_period_text.split()[0].replace(",", ""))
            except (IndexError, ValueError):
                stars_in_period = 0

        # Store the extracted information in a dictionary
        repositories.append({
            "repo_name": repo_name,
            "link": link,
            "language": language,
            "stars": stars,
            "forks": forks,
            "description": description,
            "stars_in_period": stars_in_period
        })

    return repositories

# Example usage
if __name__ == "__main__":
    for period in ["daily", "weekly", "monthly"]:
        print(f"\nTrending repositories ({period}):")
        trending_repos = get_trending_repositories(period)
        print(f"Fetched {len(trending_repos)} repositories.")
        for repo in trending_repos[:5]:  # Show first 5, but all are fetched
            print(f"Repo: {repo['repo_name']}, Link: {repo['link']}, "
                  f"Language: {repo['language']}, Stars: {repo['stars']}, "
                  f"Forks: {repo['forks']}, Stars in period: {repo['stars_in_period']}, "
                  f"Description: {repo['description']}")
        if len(trending_repos) > 5:
            print("... (additional repositories fetched but not displayed)")
