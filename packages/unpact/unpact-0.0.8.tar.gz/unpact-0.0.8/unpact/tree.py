from functools import reduce
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from .types import ColumnSpec, IndexFormatter
import inspect

__all__ = ["Tree"]


class Tree:
    def __init__(self, parent: Optional["Tree"], path: str) -> None:
        self.parent: Union[Tree, None] = parent
        self.depth: int = 0
        if parent and parent.depth is not None:
            self.depth = parent.depth + 1

        self.path: str = path
        self.children: List[Tree] = []
        self.tree_spec: ColumnSpec = {}
        self.accepts_index_arg = False

    @property
    def name(self) -> Any:
        if self.tree_spec.get("name"):
            return self.tree_spec.get("name")
        return self.path

    def get_value(self, value: Any, idx: Union[int, None] = None) -> Any:
        formatter = self.tree_spec.get("formatter")
        if formatter:
            if isinstance(formatter, IndexFormatter) and idx is not None and self.accepts_index_arg:
                return formatter(value, index=idx)
            return formatter(value)

        return {self.name: value}

    def add_child(self, child_tree: "Tree") -> None:
        self.children.append(child_tree)

    def get_child(self, path: str) -> "Tree":
        paths = path.split(".")

        def _select_child(tree: "Tree", path: str) -> "Tree":
            return next(filter(lambda p: p.path == path, tree.children))

        child = reduce(lambda tree, path: _select_child(tree, path), paths, self)
        return child

    def __repr__(self) -> str:
        base = f"{self.path}\n"

        for child in self.children:
            sep = "\t" * self.depth
            base += f"{sep}{repr(child)}\n"

        return base


def load_tree(data: dict, path: str, parent: Union[Tree, None] = None, root_name: str = "root") -> Tree:
    if parent is None:
        tree = Tree(parent, root_name)
    else:
        tree = Tree(parent=parent, path=path)

    if isinstance(data, dict):
        for k, v in data.items():
            child = load_tree(v, k, tree)
            tree.add_child(child)

    return tree


def set(obj: dict, path: str, value: Any) -> None:
    *split_path, last = path.split(".")
    for bit in split_path:
        obj = obj.setdefault(bit, {})
    obj[last] = value


def load_tree_rep(paths: Sequence[Union[str, Tuple[str, ColumnSpec]]]) -> Tree:
    tree_dict: Dict[str, Any] = {}
    for path in paths:
        if isinstance(path, tuple):
            path = path[0]
        set(tree_dict, path, None)
    tree = load_tree(tree_dict, "None", parent=None)

    specs: List[Tuple[str, ColumnSpec]] = [path for path in paths if isinstance(path, tuple)]

    for path, spec in specs:
        child = tree.get_child(path)
        child.tree_spec = spec
        formatter = spec.get("formatter")
        if formatter:
            argspec = inspect.getfullargspec(formatter)
            child.accepts_index_arg = "index" in argspec.args

    return tree
