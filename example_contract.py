
```python
# Example Intelligent Contract using API layer (conceptual)

price = gl.api.fetch("price", token="ETH")

if price > 3000:
    print("Execute trade logic")
