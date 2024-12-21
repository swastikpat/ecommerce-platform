
# Solution Documentation

## Part 1: Optimizing the Product Search API

### Improvements:
- **Filtering**: Added filters for category and price range in the API query.
- **Sorting**: Enabled sorting by price in ascending or descending order.
- **Pagination**: Implemented `LIMIT` and `OFFSET` to handle large datasets efficiently.

### Code:
See `search_api_optimization.py` for implementation.

## Part 2: Database Optimization for Order History Queries

### Schema Changes:
- Added indexes on `user_id`, `order_date`, and `status` columns for faster lookups.
- Optimized the schema for better performance during peak loads.

### Query Optimization:
```sql
SELECT * FROM orders
WHERE user_id = ? AND order_date BETWEEN ? AND ? AND status = ?
ORDER BY order_date DESC;
```

## Part 3: Scalable Architecture Design

### High-Level Architecture:
- **Caching**: Used Redis to cache frequently accessed data like product listings.
- **Load Balancing**: Integrated a load balancer (e.g., NGINX) to distribute traffic across servers.
- **Database Scaling**: Implemented master-slave replication and sharding for scalability.
- **Fault Tolerance**: Used Kubernetes for automatic failover and recovery.

### Diagram:
Refer to `architecture_diagram.png`.

---

## Files:
- `search_api_optimization.py`: Optimized API code.
- `schema.sql`: Database schema with optimizations.
- `architecture_diagram.png`: High-level architecture diagram.
