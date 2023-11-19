from typing import Set, Union, Iterable
import uuid

from django.db import models
from rest_framework import serializers


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class UserHistoryMixin(models.Model):
    created_by = models.UUIDField(editable=False, null=True)
    updated_by = models.UUIDField(editable=False, null=True)

    class Meta:
        abstract = True


class DateHistoryMixin(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    updated_datetime = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_dict(self, exclude_fields: Set[str] = None):
        return self.__instance_to_dict(self, exclude_fields)

    @classmethod
    def instances_to_dict(
        cls,
        instances: Iterable[models.Model],
        exclude_fields: Set[str] = None,
    ):
        return cls.__instances_to_dict(instances, exclude_fields)

    def __instance_to_dict(
        self,
        exclude_fields: Set[str] = None,
    ) -> Union[dict, list]:
        """
        Convert a model instance to dict.
        """
        if exclude_fields is None:
            exclude_fields = set()
        exclude_fields = {field for field in exclude_fields if hasattr(self, field)}

        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = type(self)
                depth = 1
                exclude = tuple(exclude_fields)

        serializer = Serializer(self)
        return serializer.data

    @classmethod
    def __instances_to_dict(
        cls,
        instances: Iterable[models.Model],
        exclude_fields: Set[str] = None,
    ):
        """
        Convert multiple model instances to dict.
        """
        if not all(isinstance(instance, cls) for instance in instances):
            raise ValueError("All instances must be of the same model.")

        if exclude_fields is None:
            exclude_fields = set()
        exclude_fields = {
            field for field in exclude_fields if hasattr(instances[0], field)
        }

        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                depth = 1
                exclude = tuple(exclude_fields)

        serializer = Serializer(instances, many=True)
        return serializer.data
