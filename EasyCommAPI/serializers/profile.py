from rest_framework import serializers
from oscar.core.compat import (get_user_model)

__all__ = ('profile',) 

User = get_user_model()

class profile(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ("password","groups","user_permissions","is_staff",) 