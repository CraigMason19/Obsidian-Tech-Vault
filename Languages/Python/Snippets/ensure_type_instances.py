import inspect
from functools import wraps

# what wont it do
def ensure_type_instances(func):
    """
    @enforce_types wraps the function
    When called, it:
    Maps supplied args → parameter names
    Reads type hints
    Does an isinstance() check for each
    Throws a helpful TypeError if mismatched
    Otherwise it just runs your function normally
    guards against accidental enum/class misuse
    """
    signature = inspect.signature(func)
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        """
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






@ensure_type_instances
def foo(x: list[str]):
    print(x)

foo(3)

