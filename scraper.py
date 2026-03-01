import asyncio
import re
from playwright.async_api import async_playwright

URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=63",
    "https://sanand0.github.io/tdsdata/js_table/?seed=64",
    "https://sanand0.github.io/tdsdata/js_table/?seed=65",
    "https://sanand0.github.io/tdsdata/js_table/?seed=66",
    "https://sanand0.github.io/tdsdata/js_table/?seed=67",
    "https://sanand0.github.io/tdsdata/js_table/?seed=68",
    "https://sanand0.github.io/tdsdata/js_table/?seed=69",
    "https://sanand0.github.io/tdsdata/js_table/?seed=70",
    "https://sanand0.github.io/tdsdata/js_table/?seed=71",
    "https://sanand0.github.io/tdsdata/js_table/?seed=72"
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
