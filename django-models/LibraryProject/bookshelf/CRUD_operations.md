# CRUD Operations in Django Shell

## **Create**
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Expected Output: 1984 by George Orwell (1949)
```

## **Retrieve**
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```
**Expected Output:**
```
1984 George Orwell 1949
```

## **Update**
```python
book = Book.objects.get(author="George Orwell")
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(author="George Orwell"))
```
**Expected Output:**
```
Nineteen Eighty-Four by George Orwell (1949)
```

## **Delete**
```python
book = Book.objects.get(Id=1)
book.delete()
print(Book.objects.all())  # Expected Output: <QuerySet []>
```

