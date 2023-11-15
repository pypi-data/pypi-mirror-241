from typing import Any, NamedTuple, Set

class _ProtoModule(NamedTuple):
    package: Any
    marshal: Any
    manifest: Any

def define_module(
    package: str, *, marshal: str = ..., manifest: Set[str] = ...
) -> _ProtoModule: ...
