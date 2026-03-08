# 🔗 URL Shortener System

> Day 13 – Scalable Backend System Design

---

## 📌 Problem Statement

Design a URL shortener service similar to Bitly.

The system should:

- Convert long URLs into short links
- Redirect users to the original URL
- Track basic analytics
- Support billions of links

---

# 🎯 Functional Requirements

- Create short URL
- Redirect to original URL
- Track click count
- Custom short links (optional)

---

# ⚙️ Non Functional Requirements

- Extremely fast redirection
- Highly scalable
- Highly available
- Handle billions of URLs

---

# 🧠 Core Concepts

✔ Base62 encoding  
✔ Unique ID generation  
✔ Caching hot URLs  
✔ Read-heavy optimization  
✔ Distributed databases  

---

# 📊 High Level Architecture

User
 ↓
API Gateway
 ↓
Shortener Service
 ↓
Cache (Redis)
 ↓
Database
