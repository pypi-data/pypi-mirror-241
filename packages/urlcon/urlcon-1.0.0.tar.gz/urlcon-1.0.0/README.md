# urlcon
Simple url constructor library.
```python
import urlcon

c = urlcon.Constructor("api.example.org")

print(c)

c = c / "api" / ["v2", "get_smth"]

print(c)
```
