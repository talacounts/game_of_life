from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union, _GenericAlias
from inspect import signature, Parameter


PRIMITIVE_TYPES = {'str': str, 'int': int}


class Serializable:
    # TODO: Tal, Understand code
    def __init__(self, **kwargs):
        self._constructor_kwargs = kwargs

    def serialize(self, include_type: bool = True):
        def serialize_value(value, typ) -> Union[str, Dict[str, Any]]:
            if typ.__name__ in PRIMITIVE_TYPES:
                return {'__type__': typ.__name__, 'value': repr(value)}
            if typ == list:
                inner_typ = type(value[0])
                return {'__type__': f'List[{inner_typ.__name__}]', 'value': [serialize_value(_value, inner_typ) for _value in value]}
            elif issubclass(typ, Serializable):
                return {'__type__': typ.__name__, 'value': value.serialize(include_type=False)}
            else:
                raise Exception(f"Cannot serialize value of type {typ.__name__}")

        serialized = {}
        if include_type:
            serialized['__type__'] = type(self).__name__
        serialized = {**serialized, **{kwarg: serialize_value(value, type(value)) for kwarg, value in self._constructor_kwargs.items()}}
        return serialized

    @classmethod
    def deserialize(cls, serialized: Dict[str, Any]) -> 'Serializable':
        def deserialize_value(typ, _serialized: Dict[str, Any]):
            if getattr(typ, '__name__', "") in PRIMITIVE_TYPES:
                return PRIMITIVE_TYPES[typ.__name__](_serialized['value'])
            elif isinstance(typ, _GenericAlias) and typ._name == 'List':
                inner_typ = typ.__args__[0]
                lst = _serialized['value']
                return [deserialize_value(inner_typ, value) for value in lst]
            elif issubclass(typ, Serializable):
                return typ.deserialize(_serialized['value'])
            else:
                raise Exception(f"Invalid type hint for parameter {name} of type {typ.__name__}")

        parameters = signature(cls.__init__).parameters.values()
        if any(parameter.kind == Parameter.POSITIONAL_ONLY for parameter in parameters):
            raise Exception("Cannot deserialize class with positional only parameters")

        kwargs = {}
        for parameter in parameters:
            name = parameter.name
            typ = parameter.annotation

            if name == 'self':
                continue

            if name not in serialized:
                if parameter.default == Parameter.empty:
                    raise Exception(f"No value given for constructor parameter {name}")
                else:
                    kwargs[name] = parameter.default
                    continue

            kwargs[name] = deserialize_value(typ, serialized[name])

        return cls(**kwargs)


def serialize_to_file(obj, path):
    # TODO: Tal, check code
    with open(path, 'wb') as f:
        f.write(json.dump(obj.serialize()))

def deserialize_from_file(path, typ):
    # TODO: Tal, check code
    with open(path, 'rb') as f:
        return typ.deserialize(json.load(f.read()))


# serialize_to_file(DrawableImage(???), 'image.obj')
# deserialize_from_file('image.obj', DrawableImage)
