from .serializers import ConditionSerializer
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.viewsets import ViewSetMixin


class ConditionGenericAPIView(GenericAPIView):
    conditions = {}

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )
        assert ConditionSerializer in self.serializer_class.__bases__, (
            "Incorrect `serializer_class` attribute in '%s'."
            "`conditions` feature can be used only with ConditionSerializer."
            % self.__class__.__name__
        )

        self.serializer_class.conditions = self.conditions
        return self.serializer_class


class ConditionGenericViewSet(ViewSetMixin, ConditionGenericAPIView):
    pass


class ConditionModelViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            ConditionGenericViewSet):
    pass
