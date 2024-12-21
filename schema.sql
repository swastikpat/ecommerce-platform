
-- File: schema.sql
-- Optimized Database Schema for Order History

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_date DATETIME NOT NULL,
    status TEXT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);

CREATE INDEX idx_user_id ON orders(user_id);
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_status ON orders(status);
