from rest_framework import serializers
from movie.models import StreamPlatform, WatchList

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = "__all__"

# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    
    # https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield
    # watch-detail = urls.py path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="watch-detail")
    # len_title = serializers.SerializerMethodField()

    class Meta:
        model = StreamPlatform
        fields = "__all__"
    
    # def get_len_title(self, object):
    #   return len(object.title)
    
    def validate(self, data):
      if data['title'] == data['description']:
          raise serializers.ValidationError("Title and Description should be different!")
      else:
          return data

    def validate_title(self, value):
      if len(value) < 2:
          raise serializers.ValidationError("Name is too short!")
      else:
          return value






# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class StreamPlatformSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     image = serializers.CharField()
#     show_date = serializers.DateField()
#     time_show_date = serializers.TimeField()
#     close_date = serializers.DateField()
#     time_close_date = serializers.TimeField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#       return StreamPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.show_date = validated_data.get('show_date', instance.show_date)
#         instance.time_show_date = validated_data.get('time_show_date', instance.time_show_date)
#         instance.close_date = validated_data.get('close_date', instance.close_date)
#         instance.time_close_date = validated_data.get('time_close_date', instance.time_close_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data