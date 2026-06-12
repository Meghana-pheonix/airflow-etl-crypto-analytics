CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    coin_name VARCHAR(50),
    price_usd NUMERIC,
    market_cap NUMERIC,
    captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
