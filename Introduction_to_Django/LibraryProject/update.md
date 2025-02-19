### Update Book Title

```python
book = Book.objects.get(author="Goerge Orwell")
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(author="George Orwell"))
```

#### Expected Output:
```
Nineteen Eighty-Four by George Orwell (1949)
```
