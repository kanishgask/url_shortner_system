CREATE TABLE urls (
    short_key VARCHAR(20) PRIMARY KEY,
    original_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE url_clicks (
    short_key VARCHAR(20),
    click_count BIGINT DEFAULT 0,
    last_accessed TIMESTAMP
);
