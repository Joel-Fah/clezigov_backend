from django.db import models
from slugify import slugify


# Create your models here.
class Availability(models.Model):
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE, related_name='availabilities', blank=True)
    date = models.DateField(blank=False, null=False, help_text='Date of availability')
    from_time = models.TimeField(blank=False, null=False, help_text='Available from')
    to_time = models.TimeField(blank=False, null=False, help_text='Available to')
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'Available on: {self.date} from {self.from_time} to {self.to_time}'


class Category(models.Model):
    class Filters(models.TextChoices):
        JUSTICE = 'JUSTICE', 'Justice'
        HEALTH = 'HEALTH', 'Health'
        EDUCATION = 'EDUCATION', 'Education'
        ENVIRONMENT = 'ENVIRONMENT', 'Environment'
        ECONOMY = 'ECONOMY', 'Economy'
        INTERNATIONAL = 'INTERNATIONAL', 'International'
        SPORT = 'SPORT', 'Sport'
        CIVIL = 'CIVIL', 'Civil'
        SCIENCE = 'SCIENCE', 'Science'

    name = models.CharField(max_length=255, choices=Filters.choices, blank=False, null=False, help_text='Select a '
                                                                                                        'category')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE, related_name='contacts', blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True, help_text='Email address')
    address = models.CharField(max_length=255, blank=True, null=True, help_text='Physical address')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.id


class Document(models.Model):
    class Filters(models.TextChoices):
        pass

    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE, related_name='documents', blank=True)
    name = models.CharField(max_length=255, blank=False, null=False, help_text='Name of the document')
    description = models.TextField(blank=True, null=True, help_text='Description of the document')
    file = models.ImageField(upload_to='documents/', blank=False, null=False,
                             help_text='Upload a document: <strong>.PNG, .JPG</strong> file')
    type = models.CharField(max_length=255, choices=Filters.choices, blank=False, null=False,
                            help_text='Select a document type')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE, related_name='images', blank=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False,
                              help_text='Upload an image: <strong>.PNG, .JPG</strong> file')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.image.name


class Phone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers', blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=False, null=False, help_text='Phone number')
    is_whatsapp = models.BooleanField(default=False, help_text='Is this a WhatsApp number?')
    is_calling = models.BooleanField(default=False, help_text='Is this a calling number?')
    is_messaging = models.BooleanField(default=False, help_text='Is this a messaging number?')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.phone_number


class Tag(models.Model):
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE, related_name='tags', blank=True)
    name = models.CharField(max_length=255, blank=False, null=False,
                            help_text='Select a category')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    class Filters(models.TextChoices):
        pass

    title = models.CharField(max_length=255, blank=False, null=False, help_text='Title of the procedure')
    slug = models.SlugField(max_length=200, default="", editable=False)
    description = models.TextField(blank=False, null=False, help_text='Description of the procedure')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='procedures', blank=True, null=True)
    estimated_time_to_complete = models.DurationField(blank=False, null=False, help_text='Estimated time to complete')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False,
                                help_text='Price of the procedure')
    status = models.CharField(max_length=255, choices=Filters.choices, blank=False, null=False,
                              help_text='Select a status')
    is_visible = models.BooleanField(default=True, help_text='Is this procedure visible?')

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Populate slug field from project name field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
