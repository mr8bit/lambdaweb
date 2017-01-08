from django.db import models
from cms.models import CMSPlugin
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField
from unidecode import unidecode
from taggit.managers import TaggableManager

news_types = (
	('news', 'Новости'),
	('lec', 'Лекции'),

)

default_url_vk = "https://vk.com/lambdafrela"
default_url_github = "https://github.com/lambdafrela"

# Create your models here.

class Entry(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=3000)
	image = models.ImageField(null=True)
	slug = models.SlugField(max_length=300, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	url = models.URLField(max_length=100, default=default_url_vk)

	class Meta:
		ordering = ['-created_date']

	def get_absolute_url(self):
		return reverse('event', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name))
		super(Entry, self).save(*args, **kwargs)

	@property
	def get_type(self):
		return self.__class__.__name__

class Meetup(Entry):
	date = models.DateTimeField()
	address = models.CharField(max_length=300)
	speaker = models.CharField(max_length=100, blank=True)
	avatar = models.ImageField(null=True, blank=True)
	# calendar = models.URLField(blank=True)

	class Meta:
		ordering = ['-date']

	@property
	def is_future(self):
		tz_info = self.date.tzinfo
		if datetime.now(tz_info) < self.date:
			return True
		return False

class News(Entry):
	tags = TaggableManager()