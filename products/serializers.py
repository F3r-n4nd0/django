from geopy.distance import great_circle
from rest_framework import serializers

from images.serializers import ImageSerializer
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    # distance = serializers.SerializerMethodField('get_distance')

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'seller', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'longitude', 'latitude', 'created_at', 'images')
    #
    # def get_distance(self):
    #     location_one = (self.latitude, self.longitude)
    #     location_two = (41.499498, -81.695391)
    #     return great_circle(location_one, location_two).meters

    # def get_json(self):
    #     return {
    #         'id': self.id,
    #         'race': self.race_id,
    #         'seller': self.seller_id,
    #         'gender': self.gender_id,
    #         'sterile': self.sterile,
    #         'description': self.description,
    #         'state': self.state,
    #         'price': self.price,
    #         'category': self.category,
    #         'active': self.active,
    #         'longitude': self.longitude,
    #         'latitude': self.latitude,
    #         'created_at': self.created_at
    #     }

#
# ,
#             'images': [
#                 {'id': image.id,
#                  'name': image.name,
#                  'photo_url': image.photo_url,
#                  'photo_thumbnail_url': image.photo_thumbnail_url
#                  }
#                 for image in self.image_set.all()]