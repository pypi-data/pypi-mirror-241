# Downloading Yi Tay's favorite language papers of 2022
Let's say you were browsing Twitter and you saw a tweet from Yi Tay, a researcher at Google Brain, about his [favorite NLP papers from 2022](https://www.yitay.net/blog/2022-best-nlp-papers). You want to download them all, but you don't want to click on each link and download them one by one.

With a few lines of Python and a call to `rsrch`, you can download all of the papers in a single command.

```python
import requests
import re
from rsrch import RsrchClient

# Get the HTML of the page
html = requests.get("https://www.yitay.net/blog/2022-best-nlp-papers").text

# Regex match all arXiv abstracts
matches = re.findall(r"https:\/\/arxiv\.org\/abs\/[\w\-]+\.[\w\-]+", html)

# Concatenate all the matches into a single string, remove quotes, and make a list
urls = " ".join(matches).replace('"', '').split()

# Upload the links to Notion and download the paper PDFs
rsrch = RsrchClient(token="your_notion_token", database="your_notion_database")
rsrch.upload(urls)
rsrch.download()
```
