import os
import datetime
from PIL import Image as PImage
from django.conf import settings
from os.path import join as pjoin, basename
from tempfile import NamedTemporaryFile

from django.db.models import *
from django.core.files import File

from shared.utils import *

from taggit.managers import TaggableManager

link   = "<a href='%s'>%s</a>"
imgtag = "<img border='0' alt='' src='%s' />"


class Category(BaseModel):
    title       = CharField(max_length=60)
    description = TextField(blank=True, null=True)
    link        = URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self, show="thumbnails"):
        return reverse2("category", dpk=self.pk, show=show)

    def image_links(self):
        lst = [img.image.name for img in self.images.all()]
        lst = [link % ( settings.MEDIA_URL+img, basename(img) ) for img in lst]
        return ", ".join(lst)
    image_links.allow_tags = True
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["title"]

DEFAULT_UNCATEGORIZED_ID = 4

class Image(BaseModel):
    title       = CharField(max_length=60, blank=True, null=True)
    slug        = SlugField(max_length=255, blank=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    description = TextField(blank=True, null=True)
    image       = ImageField(upload_to="images/")
    thumbnail1  = ImageField(upload_to="images/", blank=True, null=True)
    thumbnail2  = ImageField(upload_to="images/", blank=True, null=True)
    width       = IntegerField(blank=True, null=True)
    height      = IntegerField(blank=True, null=True)
    category    = ForeignKey(Category, default=DEFAULT_UNCATEGORIZED_ID, related_name="images", blank=True, null=True)
    tags = TaggableManager()
    created     = DateTimeField(auto_now_add=True)
    modified    = DateTimeField(default=datetime.datetime.now, editable=False)

    class Meta:
        ordering = ["created"]

    def __unicode__(self):
        return self.image.name

    def get_absolute_url(self):
        return reverse2("image", mfpk=self.pk)

    def __str(self):
        return self.name

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        img = PImage.open(pjoin(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = img.size
        self.save_thumbnail(img, 1, (128,128))
        self.save_thumbnail(img, 2, (64,64))

        if self.title and not self.slug:
            self.slug = slugify(self.title)

        if not self.sku:
            self.sku = self.slug
        self.modified = datetime.datetime.now()
        if self.category is None and self.category == "":
            self.category = DEFAULT_UNCATEGORIZED_ID
        super(Image, self).save(*args, **kwargs)

    # @property
    # def uncategorized(self):
    #     return self.category is None and self.category == ""

    def save_thumbnail(self, img, num, size):
        fn, ext = os.path.splitext(self.image.name)
        img.thumbnail(size, PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + str(num) + ext
        tf = NamedTemporaryFile()
        img.convert("RGB").save(tf.name, "JPEG")
        thumbnail = getattr(self, "thumbnail%s" % num)
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

    def size(self):
        return "%s x %s" % (self.width, self.height)

    def thumbnail1_url(self):
        return settings.MEDIA_URL + self.thumbnail1.name

    def thumbnail2_url(self):
        return settings.MEDIA_URL + self.thumbnail2.name

    def image_url(self):
        return settings.MEDIA_URL + self.image.name
