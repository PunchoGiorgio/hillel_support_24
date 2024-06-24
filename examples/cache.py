# from rest_framework import serializers
# from dataclasses import dataclass
# from shared.cache import CacheService
# from users.models import User


# @dataclass
# class ActivatorUserMeta:
#     id: int


# class ActivatorUserMetaSerializer(serializers.Serializer):
#     id = serializers.IntegerField()

# record: dict = CacheService().get(
#     namespace="activation", key="3b412c94-6347-3b90-bff4-a4ee8b52fee6"
# )

# serializer = ActivatorUserMetaSerializer(data=record)
# serializer.is_valid(raise_exception=True)

# serializer.validated_data["id"]

# user = User.objects.get(id=instance.id)
