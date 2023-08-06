from rest_framework import serializers
from django.utils.functional import cached_property
from rest_framework.utils.serializer_helpers import BindingDict


class ConditionSerializer(serializers.Serializer):
    conditions = {}

    def _check_condition(self, key):
        condition = self.conditions.get(key)
        condition_value = True
        if condition is not None:
            if isinstance(condition, bool):
                condition_value = condition
            elif callable(condition):
                condition_value = condition()
                assert isinstance(condition_value, bool), (
                    "Invalid output type in condition function in '%s'.conditions."
                    "All condition functions must return boolean values."
                    % self.__class__.__name__
                )
            else:
                raise AssertionError(
                    "Invalid condition value. All conditions must be boolean or function, "
                    "returning boolean"
                )
        return condition_value

    @cached_property
    def fields(self):
        fields = BindingDict(self)
        if self.conditions:
            for key, value in self.get_fields().items():
                if self._check_condition(key):
                    fields[key] = value
        return fields
