from django.db import models
from uuslug import uuslug

class ContentMixin(models.Model):
	page = models.ForeignKey('drf_cms.Page', null=False, on_delete=models.CASCADE)
	key = models.CharField(null=False, max_length=64)

	class Meta:
		unique_together = ('page', 'key')
		abstract = True

	def __str__(self):
		return self.key


class MetadataMixin(models.Model):
	description = models.CharField(blank=True, max_length=512)
	uploaded_at =  models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.description


class SlugModelMixin(models.Model):
    slugged_field = ""

    slug = (
        models.SlugField()
    )

    class Meta:
        abstract = True
        unique_together = ('slug', )

    def prepare_slug(self):
        if not self.slug:
            _slugged_field = getattr(self, self.slugged_field)
            self.slug = uuslug(_slugged_field, instance=self)
        else:
            self.slug = uuslug(self.slug, instance=self)

    def save(self, *args, **kwargs):
        self.prepare_slug()
        super(SlugModelMixin, self).save(*args, **kwargs)