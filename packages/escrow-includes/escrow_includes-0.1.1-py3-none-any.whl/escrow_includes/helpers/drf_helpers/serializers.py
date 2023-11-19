from django.contrib.auth import get_user_model
from rest_framework import serializers


USER_MODEL = get_user_model()


class UserHistorySerializer(serializers.Serializer):
    def _get_user(self) -> USER_MODEL:
        return self.context["request"].user

    def save(self, **kwargs):
        if self.instance is None:
            self.validated_data["created_by"] = self._get_user().id
        else:
            self.validated_data["updated_by"] = self._get_user().id
        return super().save(**kwargs)
