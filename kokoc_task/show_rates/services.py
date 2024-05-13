class DatabaseService:
    """ Класс для выполнения общих операций с базой данных. """

    @staticmethod
    def create_object(model, **kwargs):
        model.objects.create(**kwargs)

    @staticmethod
    def get_object(model, **kwargs):
        return model.objects.get(**kwargs)

    @staticmethod
    def get_object_by_attr(model, **kwargs):
        return model.objects.filter(**kwargs)

    @staticmethod
    def if_exists(model, **kwargs):
        return model.objects.filter(**kwargs).exists()
