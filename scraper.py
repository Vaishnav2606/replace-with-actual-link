import asyncio
import re
from playwright.async_api import async_playwright

URLS = [
    "https://replace-with-actual-link-for-seed-63.com",
    "https://replace-with-actual-link-for-seed-64.com",
    "https://replace-with-actual-link-for-seed-65.com",
    "https://replace-with-actual-link-for-seed-66.com",
    "https://replace-with-actual-link-for-seed-67.com",
    "https://replace-with-actual-link-for-seed-68.com",
    "https://replace-with-actual-link-for-seed-69.com",
    "https://replace-with-actual-link-for-seed-70.com",
    "https://replace-with-actual-link-for-seed-71.com",
    "https://replace-with-actual-link-for-seed-72.com"
]

async def main():
    total_sum = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in URLS:
            if "replace-with-actual-link" in url:
                continue
            
            await page.goto(url)
            cells = await page.locator("table td, table th").all_inner_texts()
            
            for cell_text in cells:
                numbers = re.findall(r'-?\d+\.?\d*', cell_text)
                for num_str in numbers:
                    try:
                        total_sum += float(num_str)
                    except ValueError:
                        pass
        
        await browser.close()
    
    print("=========================================")
    print(f"FINAL TOTAL SUM: {total_sum}")
    print("=========================================")

if __name__ == "__main__":
    asyncio.run(main())
