from django.db import models
import os
import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)

	slug = slug.lower()
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug = slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(
				slug = slug,
				randstr=random_string_generator(size=4)
			)
		return unique_slug_generator(instance, new_slug=new_slug)

	return slug

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 3000000220)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
	return "{table_name}/{new_filename}/{final_filename}".format(
			table_name=instance.__class__.__name__,new_filename=new_filename, final_filename=final_filename
		)
def upload_file_path(instance, filename):
  return upload_image_path(instance, filename)

def upload_original_image_path(instance, filename):
	new_filename = random.randint(1, 3000000220)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=name,ext = ext)
	return "{table_name}/{new_filename}/{final_filename}".format(
			table_name=instance.__class__.__name__,new_filename=new_filename, final_filename=final_filename
		)

def upload_original_file_path(instance, filename):
  return upload_original_image_path(instance, filename)