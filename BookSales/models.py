from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
class Publisher(models.Model):
    brand = models.CharField(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.brand
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.title
    

    

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.IntegerField(null=True, blank=True)
    sale_date = models.DateField()
    def save(self, *args, **kwargs):
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.book.title}"