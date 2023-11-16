import fameio.source.scenario as fameio


class Contract(fameio.Contract):
    """Extends fameio.Contract with the features required for the GUI"""

    @classmethod
    def from_dict(cls, definitions: dict) -> "Contract":
        return super().from_dict(definitions)

    FIELD_TYPE_INT = "int"
    FIELD_TYPE_STRING = "string"
    FIELD_TYPE_STRING_COMBO_SELECTION = "stringComboSelection"

    FIELD_TYPE_FLOAT = "float"
    FIELD_TYPE_DATE_TIME = "datetime"

    def get_field_types(self) -> list:
        """Returns a list of tuples with the field name and the field type to build a UI"""
        return [
            (super()._KEY_SENDER, self.FIELD_TYPE_INT),
            (super()._KEY_RECEIVER, self.FIELD_TYPE_INT),
            (super()._KEY_PRODUCT, self.FIELD_TYPE_STRING_COMBO_SELECTION),
            (super()._KEY_FIRST_DELIVERY, self.FIELD_TYPE_DATE_TIME),
            (super()._KEY_INTERVAL, self.FIELD_TYPE_INT),
            (super()._KEY_EXPIRE, self.FIELD_TYPE_DATE_TIME),
        ]

    def get_field_type(self, field_name):
        """Returns field type"""
        for field in self.get_field_types():
            if field[0] == field_name:
                return field[1]

        raise RuntimeError(f"Field type not found with the field_name: {field_name}")


    def get_fields_to_edit(self):
        return [
            super()._KEY_SENDER,
            super()._KEY_RECEIVER,
            super()._KEY_PRODUCT,
            super()._KEY_FIRST_DELIVERY,
            super()._KEY_INTERVAL,
            super()._KEY_EXPIRE,
        ]
