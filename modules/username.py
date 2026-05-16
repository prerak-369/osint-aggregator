import httpx

platforms = {
    "github": "https://github.com/{}",
    #"linkedin": "https://www.linkedin.com/in/{}",
    #"twitter": "https://twitter.com/{}",
    #"instagram": "https://www.instagram.com/{}",
    #"facebook": "https://www.facebook.com/{}",
    #"youtube": "https://www.youtube.com/{}",
    "reddit": "https://www.reddit.com/user/{}",
    #"discord": "https://discord.com/users/{}",
    "telegram": "https://t.me/{}",
    "medium": "https://medium.com/@{}"
}

def check_username(username):
    results = []
    for platform, url in platforms.items():
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"}
            response = httpx.get(url.format(username), timeout=10, headers=headers)
            if response.status_code == 200:
                results.append((platform, True, url.format(username)))  
            else:
                results.append((platform, False, None))
            
        except httpx.RequestError:
            print(f"[!] Error connecting to {platform}")

    return results
