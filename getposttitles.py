import re

def extract_urls_from_text(file_path):
    urls = []
    with open(file_path, 'r') as file:
        for line in file:
            if "https://www.mortgagechoice.com.au/guides/" in line:
                # Extract the URL from the line
                url = re.search(r"https://www\.mortgagechoice\.com\.au/guides/[\w/-]+", line)
                if url:
                    urls.append(url.group(0))
    return urls

def extract_titles(urls):
    titles = []
    for url in urls:
        # Extract the slug part of the URL
        slug = url.split('/guides/')[1]
        # Replace hyphens with spaces and capitalize words
        title = ' '.join(word.capitalize() for word in slug.split('-'))
        # Replace the last forward slash with a question mark if present
        title = title.replace('/', ' ')
        titles.append(title)
    return titles

def write_titles_to_file(titles, file_path):
    with open(file_path, 'w') as file:
        for title in titles:
            file.write(title + '\n')

# Hardcoded sitemap file path and output file path
sitemap_path = 'mcsitemap.xml'
output_file_path = 'extracted_titles.txt'

urls = extract_urls_from_text(sitemap_path)
titles = extract_titles(urls)
write_titles_to_file(titles, output_file_path)
print(f"Titles extracted and written to {output_file_path}")

