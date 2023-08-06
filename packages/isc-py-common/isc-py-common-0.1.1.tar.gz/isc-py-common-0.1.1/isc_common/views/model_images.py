import logging
import os

from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet

logger = logging.getLogger(__name__)


class Model_imagesQuerySet(AuditQuerySet):
    pass


class Model_imagesManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
        }
        return res

    def get_queryset(self):
        return Model_imagesQuerySet(self.model, using=self._db)


class ImageNotFound(Exception):
    pass


class Model_images(AuditModel):
    @classmethod
    def update_or_create_image(cls, file_name, main_model, code, path, self_image_field=False, name=None, exception=True, full_name_image=None, image_field_name=None, pk_name='id', defaults=None):
        from lfl_admin.common.models.site_lfl_images import Site_lfl_images
        from isc_common.models.image_types import Image_types
        from isc_common.models.images import Images

        if name is None:
            name = code

        if file_name is not None and file_name.strip() == '':
            file_name = None

        if full_name_image is None:
            full_name_image = Site_lfl_images.get_image(file_name=file_name, path=path)

        if full_name_image is not None:

            image_type, created = Image_types.objects.get_or_create(code=code, defaults=dict(name=name))
            image, created = Images.objects.update_or_create(image_type=image_type, real_name=full_name_image)
            if os.path.exists(full_name_image):
                image1, created = Images.create_update(id=image.id, image_type=image_type, real_file_name=full_name_image)
            if self_image_field is False:
                return cls.objects.update_or_create(image=image, main_model=main_model, defaults=defaults)
            else:
                eval(f'main_model._meta.concrete_model.objects.filter({pk_name}=main_model.{pk_name}).update({image_field_name}=image)', dict(), dict(image=image, main_model=main_model))

            logger.debug(f'{file_name} : found')

        elif file_name is not None:
            if exception is True:
                raise ImageNotFound(f'{file_name} : not found')
            else:
                logger.debug(f'{file_name} : not found !!!')
        return None, None

    objects = Model_imagesManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Базовый класс'
        abstract = True
