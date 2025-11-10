from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    birth_year = models.IntegerField()

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    year_written = models.IntegerField()

    def __str__(self):
        return self.title


class Publication(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_date = models.DateField()
    copies = models.IntegerField()  # тираж

    def __str__(self):
        return f"{self.book.title} ({self.publisher.name}, {self.publish_date})"


class Sales(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_sold = models.IntegerField()

    @property
    def total_sales(self):
        return self.price * self.qty_sold

    def __str__(self):
        return f"{self.publication.book.title}, {self.year}: {self.qty_sold} sold"
