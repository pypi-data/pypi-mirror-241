import inspect
import functools
from typing import Annotated

__all__ = (
    "Unsigned",
    "Negative",
    "UnsignedEven",
    "validate",
    "ValidationError",
)

Unsigned = Annotated[
    int,
    (lambda V: V >= 0, "{} must be greater than or equal to 0 but it is {{}}"),
]

Negative = Annotated[
    int,
    (lambda V: V < 0, "{} must be negative(i.e: < 0) but it is equal to {{}}"),
]

UnsignedEven = Annotated[
    int,
    (lambda V: V % 2 == 0, "{} must be even but it is {{}}"),
    (lambda V: V >= 0, "{} must be positive but it is {{}}"),
]


class ValidationError(Exception):
    ...


def validate(strict=True, cache=False):
    def wrapper(func):
        sig = inspect.signature(func)
        parameters = sig.parameters

        @functools.wraps(func)
        def inner(*args, **kwargs):
            for idx, (key, param) in enumerate(parameters.items()):
                if idx < len(args):
                    arg_val = args[idx]
                elif kwargs.get(key, None):
                    arg_val = kwargs[key]
                elif param.default != param.empty:
                    arg_val = param.default
                else:
                    arg_val = None
                anno = param.annotation

                _validate_annotation(anno, strict, arg_val, key, param)

            result = func(*args, **kwargs)
            if sig.return_annotation != sig.empty:
                _validate_annotation(
                    sig.return_annotation, strict, result, "return value", "return"
                )
            return result

        if cache:
            return functools.cache(inner)

        return inner

    return wrapper


def _validate_annotation(anno, strict, arg_val, key, param):
    if isinstance(anno, type):
        return

    if not hasattr(anno, "__metadata__"):
        return

    try:
        for predicate, message in anno.__metadata__:
            if strict and not isinstance(arg_val, anno.__origin__):
                raise ValidationError(
                    f"{key} is of type {type(key)} but it should be of type {anno.__origin__}\n"
                    f"and follow these predicate(s): {anno}"
                )
            if predicate(arg_val) == False:
                raise ValidationError(
                    message.replace("{{}}", f"{arg_val}").replace("{}", key)
                )
    except (ValueError, TypeError, AttributeError) as err:
        raise ValidationError(
            f'{err}\nThe type for "{param}" is configured incorrectly for runtime validation.\n'
            "Annotated type should look like: Annotated[<base_type>, (<predicate>, <message>), <...>]"
        )


if __name__ == "__main__":

    @validate()
    def add_two(a: int = 5, b: Unsigned = -2) -> Unsigned:
        return a + b

    add_two()
