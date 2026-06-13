import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# List of URLs to scrape (Books to Scrape sandbox website - safe, fast, and does not block)
urls = [f"http://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 6)]

# Shared list (array) to store the scraped book titles
scraped_books = []

def scrape_page(url):
    """
    Function to scrape book titles from a single web page.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all products on the page
            articles = soup.find_all("article", class_="product_pod")
            page_books = []
            
            for article in articles:
                # Extract the full title from the anchor tag
                title = article.h3.a["title"]
                page_books.append(title)
                
            # Safely add the titles to our global list
            scraped_books.extend(page_books)
            print(f"[SUCCESS] Scraped {len(page_books)} books from: {url}")
        else:
            print(f"[ERROR] Failed to fetch {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Error occurred while scraping {url}: {e}")

def run_sequential():
    print("\n--- 1. Starting Sequential Scraping (One by One) ---")
    scraped_books.clear()
    start_time = time.time()
    
    for url in urls:
        scrape_page(url)
        
    end_time = time.time()
    duration = end_time - start_time
    print(f"Sequential Execution Time: {duration:.2f} seconds")
    return duration

def run_multithreaded():
    print("\n--- 2. Starting Multithreaded Scraping (Simultaneously) ---")
    scraped_books.clear()
    start_time = time.time()
    
    # Using ThreadPoolExecutor to run tasks concurrently
    # max_workers=5 means we will run 5 requests at the exact same time
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scrape_page, urls)
        
    end_time = time.time()
    duration = end_time - start_time
    print(f"Multithreaded Execution Time: {duration:.2f} seconds")
    return duration

if __name__ == "__main__":
    # Step 1: Run sequentially and track the time
    seq_time = run_sequential()
    
    print("\n" + "="*50)
    
    # Step 2: Run using multi-threading and track the time
    mt_time = run_multithreaded()
    
    # Step 3: Display Comparison & Scraped Data
    print("\n" + "="*15 + " TIMING COMPARISON " + "="*15)
    print(f"Sequential Time   : {seq_time:.2f} seconds")
    print(f"Multi-threaded Time: {mt_time:.2f} seconds")
    speedup = seq_time / mt_time if mt_time > 0 else 0
    print(f"Speedup Factor    : {speedup:.2f}x faster!")
    print("="*49)
    
    print(f"\nTotal unique books scraped and stored in array: {len(scraped_books)}")
    print("\nFirst 10 books in the array:")
    for idx, title in enumerate(scraped_books[:10], 1):
        # Safe print for Windows terminal to avoid UnicodeEncodeError
        safe_title = title.encode('ascii', 'ignore').decode('ascii')
        print(f"  {idx}. {safe_title}")