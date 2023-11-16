from django.db import models
from uuslug import uuslug


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