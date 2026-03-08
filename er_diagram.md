# 📊 ER Diagram – URL Shortener

URLS
- short_key (PK)
- original_url
- created_at

URL_CLICKS
- short_key
- click_count
- last_accessed

Relationship:

Short URL 1 → 1 Click Counter
