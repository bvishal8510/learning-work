from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
import uuid
import os
from django.contrib import messages
from django.core.urlresolvers import reverse
from PIL import Image
from PIL import ImageFilter, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

def get_profile_name(instance, filename):    # to give unique id to profile pic uploaded by using uuid
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile_pic', filename)


class Profile(models.Model):                # all details comming as user's profile info form get saved in this table
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100, blank=True)
    Last_Name = models.CharField(max_length=100, blank=True)
    City = models.CharField(max_length=30, blank=True)
    DOB = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to=get_profile_name, default='profile_pic/default_profile.jpg')
    bio = models.TextField(max_length=500, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):                    # shows every object with username name
        return self.user.username


def get_file_name(instance, filename):               # to give unique id to images uploaded
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('documents', filename)

choice1 = (("PRIVATE", "Private"), ("PUBLIC", "Public"),)
choice2 = ((1, "Large"), (2, "Medium"),(3, "Small"))
choice3 = (('horizon', "Flip Horizontally"), ('vertical', "Flip Vertically"),('NONE', "None"))
choice4 = (('clock', "Clockwise"), ('anti', "Anticlockwise"), ('NONE', "None"))
choice5 = (('y', 'Yes'), ('n', 'No'))
choice6 = ((1, "None"), (2, "Aqua"), (3, "Seaform"), (4, "Grayscale"),
           (5, "Retro"), (6, "Edges"), (7, "Negative"), (8, 'Sepia'))


class Document(models.Model, object):                  # all details comming about a particular picture uploaded                                                      #  get saved in this table
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=choice1, default="PUBLIC")
    width = models.IntegerField(blank=True, default=500, help_text="Enter positive value ")
    height = models.IntegerField(blank=True, default=500, help_text="Enter positive value ")
    flip = models.CharField(max_length=17, choices=choice3, default="NONE")
    rotate = models.CharField(max_length=15, choices=choice4, default='NONE')
    blur = models.CharField(max_length=5, choices=choice5, default='n')
    effect = models.IntegerField(choices=choice6, default=1)
    document = models.ImageField(upload_to=get_file_name)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    like_or_not = models.IntegerField(default=0)
    like_user = models.ManyToManyField(User, related_name='hello', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):                  # gives a common name to objects
        return self.document

    def get_absolute_url(self):
        return reverse('model_form_upload', kwargs={'pk': self.pk})

    def save(self):
        im = Image.open(self.document)    #opens a particular image

        output = BytesIO()                #file is written into memory
        im = im.resize((self.width, self.height))
        if self.flip == 'horizon':
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif self.flip == 'vertical':
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        elif self.flip == 'NONE':
            pass

        if self.rotate == 'clock':
            im = im.rotate(270)
        elif self.rotate == 'anti':
            im = im.rotate(90)
        elif self.rotate == 'NONE':
            pass

        if self.blur == 'y':
            im = im.filter(ImageFilter.BLUR)
        elif self.blur == 'n':
            pass

        if self.effect == 1:
            im = im.convert('RGB')
            r, g, b = im.split()
            im = Image.merge('RGB', (r, g, b))
        elif self.effect == 2:
            im = im.convert('RGB')
            r, g, b = im.split()
            im = Image.merge('RGB', (b, g, r))
        elif self.effect == 3:
            im = im.convert('RGB')
            r, g, b = im.split()
            im = Image.merge('RGB', (g, r, b))
        elif self.effect == 4:
            width, height = im.size
            for i in range(width):
                for j in range(height):
                    r, g, b = im.getpixel((i,j))
                    c = int(round((r+g+b)/3))
                    im.putpixel((i,j),(c,c,c))
        elif self.effect == 5:
            im = im.convert('RGB')
            r, g, b = im.split()
            im = Image.merge('RGB', (r, b, g))
        elif self.effect == 6:
            im = im.filter(ImageFilter.FIND_EDGES)
        elif self.effect == 7:
            im = ImageOps.invert(im)
        elif self.effect == 8:
            width, height = im.size
            for i in range(width):
                for j in range(height):
                    r, g, b = im.getpixel((i,j))
                    c = int((round(r+g+b)/3))
                    R, G, B = c+100, c+100, c
                    im.putpixel((i, j), (R, G, B))
        im.save(output, format='JPEG', quality=100)   # saving the image into the file in memory
        output.seek(0)

        self.document = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.document.name.split('.')[0],
                                             'image/jpeg', sys.getsizeof(output), None)

        try:
            this = Document.objects.get(id=self.id)
            if this.document == self.document:
                self.document = this.document
            else:
                this.document.delete(save=False)
        except:
            pass  # when new image
        super(Document, self).save()


# @receiver(post_delete, sender=Document)
# def document_post_delete_handler(sender, **kwargs):
#     instance = kwargs['instance']
#     storage, path = instance.document.storage, instance.document.path
#     if (path != '.') and (path != '/') and (path != 'photo/') and (path != 'document/.'):
#         storage.delete(path)

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    comment = models.TextField(max_length=225)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

@receiver(post_save,sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    # here created is a boolean that tells new instance
    #  was created or an older instance was updated.
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
