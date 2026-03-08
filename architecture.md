# 🏗️ URL Shortener Architecture

Client
 ↓
API Gateway
 ↓
URL Shortener Service
 ↓
Cache (Redis)
 ↓
Database

---

# Write Flow

1. User submits long URL
2. Generate unique ID
3. Convert ID to Base62
4. Store mapping
5. Return short URL

---

# Read Flow

1. User clicks short URL
2. Check cache
3. If miss → query database
4. Redirect to original URL

---

# Scaling Strategy

- Cache popular links
- Partition database by hash
- Use CDN for global redirects

---

# Handling Massive Scale

If system stores billions of links:

• Use distributed ID generator  
• Shard databases  
• Cache hot URLs  
• Use load balancers
