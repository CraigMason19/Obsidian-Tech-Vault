import inspect
from functools import wraps

def ensure_type_instances(func):
    """
    Decorator that performs lightweight runtime type checks based on a
    function's type annotations.

    This is intended as a sanity check to catch accidental misuse of
    custom classes or enums. It only validates simple, concrete types
    (i.e., annotations that are actual classes). Generic type hints such
    as list[str] or dict[str, int] are ignored.

    Behavior:
        • Maps supplied arguments to parameter names.
        • Looks up each parameter's type annotation.
        • If the annotation is a concrete class, checks the argument using
          isinstance(arg, annotated_class).

    Important Notes:
        • Subclasses of the annotated type are accepted (normal
          isinstance() behavior).
        • Generic type hints (e.g., list[str]) are ignored.
        • No deep or structural type checking is performed.
        • Only annotations that are actual classes trigger a check.

    Raises:
        TypeError:
            If an argument does not match the annotated class (or its subclasses).
    """
    signature = inspect.signature(func)
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected = annotations.get(name)

            if isinstance(expected, type) and not isinstance(value, expected):
                msg = f"Argument '{name}' must be of type {expected.__name__}, not {type(value).__name__}"
                
                raise TypeError(msg)

        return func(*args, **kwargs)

    return wrapper




class Note:
    pass

class ScaleType:
    pass

class DiatonicScale(ScaleType):
    pass

class KeyType:
    pass


@ensure_type_instances
def make_scale(root: Note, scale_type: ScaleType):
        # if not isinstance(root, Note):
        #     raise TypeError(f"root must be Note, not {type(root).__name__}")

        # if not isinstance(scale_type, ScaleType):
        #     raise TypeError(f"scale_type must be ScaleType, not {type(scale_type).__name__}")

    print("Scale created!")


make_scale(Note(), ScaleType())
make_scale(Note(), DiatonicScale())






@ensure_type_instances
def foo(x: list[str]):
    print(x)

foo(3)


@ensure_type_instances
def foobar(note: Note, x: list[str]):
    print(x)

foobar(Note(), 5)

