'''## 🟡 1. Normalize a sentence

👉 Remove extra spaces + make all lowercase

```python
"  HeLLo   WoRLD  " → "hello world"
```

✔ Methods: `.strip()`, `.lower()`, `.split()`, `.join()`'''

text = "HeLLo    WoRLD"

result = " ".join(text.strip().lower().split())

print(result)

