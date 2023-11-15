import dataclasses
import functools
from typing import Any, Callable, List, Type, TypeVar, cast

from chalk.features.feature_field import Feature
from chalk.features.feature_set import FeatureSetBase
from chalk.features.feature_wrapper import FeatureWrapper
from chalk.features.underscore import Underscore
from chalk.serialization.parsed_annotation import ParsedAnnotation
from chalk.utils.notebook import is_notebook

T = TypeVar("T")
V = TypeVar("V")


@dataclasses.dataclass(frozen=True)
class classproperty:
    fget: Callable[[Any], Any]
    bind_to_instances: bool = True
    cached: bool = False


def _cached_getter(
    instance: T,
    *,
    getter: Callable[[T], V],
    cache: List[V],
) -> V:
    if len(cache) == 1:
        return cache[0]
    val = getter(instance)
    cache.append(val)
    return val


def classproperty_support(cls: Type[T]) -> Type[T]:
    """
    Class decorator to add metaclass to our class.
    Metaclass uses to add descriptors to class attributes, see:
    http://stackoverflow.com/a/26634248/1113207
    """

    # From https://stackoverflow.com/questions/3203286/how-to-create-a-read-only-class-property-in-python
    class Meta(type(cls)):
        __chalk_feature_set__ = True

        # This overload important for feature explosion correctness
        def __str__(self):
            return self.namespace

        def __iter__(self):
            for feature in self.features:
                if feature.is_scalar:
                    yield feature

        def __setattr__(self, key, value):
            # Handle inline feature definitions in notebooks
            if isinstance(value, Underscore) and is_notebook():
                from chalk.df.ast_parser import parse_inline_setattr_annotation
                from chalk.features.feature_set_decorator import _process_field

                fqn = f"{self.namespace}.{key}"
                existing_feature = next((f for f in self.features if f.fqn == fqn), None)

                typ = parse_inline_setattr_annotation(key)
                if typ is None and existing_feature is None:
                    raise TypeError(f"Please define a type annotation for feature '{fqn}'")
                elif typ is None:
                    prev_typ = self.features[self.features.index(fqn)].typ
                    typ = prev_typ
                parsed_annotation = (
                    typ if typ is None or isinstance(typ, ParsedAnnotation) else ParsedAnnotation(underlying=typ)
                )

                if existing_feature is not None:
                    f = existing_feature
                    f.typ = parsed_annotation
                    f.underscore_expression = value
                else:
                    f = Feature(
                        namespace=self.namespace,
                        name=key,
                        attribute_name=key,
                        features_cls=self,
                        typ=parsed_annotation,
                        underscore_expression=value,
                    )
                    self.features.append(f)

                    wrapped_feature = FeatureWrapper(f)
                    super().__setattr__(key, wrapped_feature)

                # Process feature field
                _process_field(
                    f=f,
                    comments={},
                    class_owner=cls.__chalk_owner__,
                    class_tags=tuple(cls.__chalk_tags__),
                    class_etl_offline_to_online=cls.__chalk_etl_offline_to_online__,
                    class_max_staleness=cls.__chalk_max_staleness__,
                )

                # Update graph in notebook for inline feature definition
                if FeatureSetBase.hook:
                    FeatureSetBase.hook(self)

            else:
                super().__setattr__(key, value)

    cls_vars = dict(vars(cls))
    class_prop_names: List[str] = []

    for name, obj in cls_vars.items():
        if isinstance(obj, classproperty):
            # Removing this pseudoproperty that we really want on the metaclass
            if obj.bind_to_instances:
                class_prop_names.append(name)
            delattr(cls, name)
            if obj.cached:
                setattr(
                    Meta,
                    name,
                    property(
                        functools.partial(
                            _cached_getter,
                            getter=obj.fget,
                            cache=[],
                        )
                    ),
                )
            else:
                setattr(Meta, name, property(obj.fget))

    class Wrapper(cast(Type[object], cls), metaclass=Meta):
        def __getattribute__(self, name: str):
            # Bind all cached properties to the metaclass @property
            if name in class_prop_names:
                return getattr(type(self), name)
            return super().__getattribute__(name)

    Wrapper.__name__ = cls.__name__
    Wrapper.__qualname__ = cls.__qualname__
    Wrapper.__module__ = cls.__module__
    Wrapper.__doc__ = cls.__doc__
    Wrapper.__annotations__ = cls.__annotations__

    return cast(Type[T], Wrapper)
