from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggeditemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_tags_for_model(obj_type)
        
        return TaggedItem.objects.select_related('tag') \
            .filter(
                    content_type=content_type, 
                    object=obj_id
                )
    

class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self):
        return self.label
    
    
class TaggedItem(models.Model):
    #customer manager
    objects = TaggeditemManager()
    # what  tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article ..)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Id of that object, here we specify the positiveintergerfield by assuming all the tabsle with primary key as integer.
    object_id = models.PositiveIntegerField()
    # to get the actual object/product this tag is applied to while querying.
    content_object = GenericForeignKey()    