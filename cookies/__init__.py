import aiohttp
import os

async def fetch_cookies():
    pastebin_url = os.getenv("COOKIES")
    if pastebin_url is None:
        return None
    id = pastebin_url.split("/")[-1]
    url = f"https://batbin.me/raw/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                raw_content = await response.text()
                with open("cookies/cookies.txt", "w") as file:
                    file.write(raw_content)
                
                print(f"Content successfully written to {output_file}")
            else:
                print(f"Failed to fetch the URL. Status code: {response.status}")
