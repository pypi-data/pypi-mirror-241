import auror
import numpy


class Protego(auror.Validator):
    numpy_ndarray_type = auror.TypeDefinition('ndarray', (numpy.ndarray,), ())
    str_type = auror.TypeDefinition('str', (str,), ())
    types_mapping = auror.Validator.types_mapping.copy()
    types_mapping['ndarray'] = numpy_ndarray_type
    types_mapping['str'] = str_type

    @staticmethod
    def custom_allowed_function(*args, **kwargs):
        return None

    def _validate_check_allowed_with(self, constraint, field, value):
        custom_constraint = self.custom_allowed_function(constraint)
        if custom_constraint is None:
            self._error(field, "Custom constraint checking function not valid")
            return

        for entry in value:
            if entry not in custom_constraint:
                self._error(field,
                            "Allowed values not satisfied: {value} != {c}".format(value=value, c=custom_constraint))

    def _validate_sequence(self, constraint, field, value):
        if not value == constraint:
            self._error(field, "Correct sequence not satisfied: {value}!={constraint}".format(value=value,
                                                                                              constraint=constraint))

    def _validate_struct_type(self, constraint, field, value):
        """ Test the structure type.

        constraint: True | False
        field: amount
        value: number
        """
        if isinstance(value, list):
            for entry in value:
                if not type(entry).__name__ in constraint:
                    self._error(field, "Must be of type:{constraint}".format(constraint=constraint))

    def register_data_type(self, data_type):
        new_data_type = auror.TypeDefinition(data_type.__name__, (data_type,), ())
        self.types_mapping[data_type.__name__] = new_data_type
