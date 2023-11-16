from __future__ import annotations

from collections.abc import Mapping, Sequence
import configparser
import datetime
import functools
import importlib

from importlib import metadata
import io
import itertools
import json
import logging
import operator
import os
import pathlib
import platform
import pprint
import sys
import tomllib
from typing import Any, Literal

from jinjarope import envtests, utils


logger = logging.getLogger(__name__)


version_info = dict(
    python_version=sys.version.split("(")[0].strip(),
    jinja_version=metadata.version("jinja2"),
    jinjarope_version=metadata.version("jinjarope"),
    system=platform.system(),
    architecture=platform.architecture(),
    python_implementation=platform.python_implementation(),
)


def wrap_in_elem(
    text: str | None,
    tag: str,
    add_linebreaks: bool = False,
    **kwargs,
) -> str:
    """Wrap given text in an HTML/XML tag (with attributes).

    If text is empty, just return an empty string.

    Arguments:
        text: Text to wrap
        tag: Tag to wrap text in
        add_linebreaks: Adds a linebreak before and after the text
        kwargs: additional key-value pairs to be inserted as attributes for tag.
                Key strings will have "_" stripped from the end to allow using keywords.
    """
    if not text:
        return ""
    attrs = [f'{k.rstrip("_")}="{v}"' for k, v in kwargs.items()]
    attr_str = (" " + " ".join(attrs)) if attrs else ""
    nl = "\n" if add_linebreaks else ""
    return f"<{tag}{attr_str}>{nl}{text}{nl}</{tag}>"


def html_link(text: str | None = None, link: str | None = None, **kwargs) -> str:
    """Create a html link.

    If link is empty string or None, just the text will get returned.

    Arguments:
        text: Text to show for the link
        link: Target url
        kwargs: additional key-value pairs to be inserted as attributes.
                Key strings will have "_" stripped from the end to allow using keywords.
    """
    if not link:
        return text or ""
    attrs = [f'{k.rstrip("_")}="{v}"' for k, v in kwargs.items()]
    attr_str = (" " + " ".join(attrs)) if attrs else ""
    return f"<a href={link!r}{attr_str}>{text or link}</a>"


def md_link(
    text: str | None = None,
    link: str | None = None,
    tooltip: str | None = None,
) -> str:
    """Create a markdown link.

    If link is empty string or None, just the text will get returned.

    Arguments:
        text: Text to show for the link
        link: Target url
        tooltip: Optional tooltip
    """
    if not link:
        return text or ""
    tt = f" '{tooltip}'" if tooltip else ""
    return f"[{text or link}]({link}{tt})"


def serialize(data: Any, mode: Literal["yaml", "json", "ini", "toml"] | None) -> str:  # type: ignore[return]
    """Serialize given json-like object to given format.

    Arguments:
        data: The data to serialize
        mode: The serialization mode
    """
    match mode:
        case None | "yaml":
            import yaml

            return yaml.dump(data)
        case "json":
            return json.dumps(data, indent=4)
        case "ini":
            config = configparser.ConfigParser()
            config.read_dict(data)
            file = io.StringIO()
            with file as fp:
                config.write(fp)
                return file.getvalue()
        case "toml" if isinstance(data, dict):
            import tomli_w

            return tomli_w.dumps(data)
        case _:
            raise TypeError(mode)


@functools.cache
def load_file_cached(path: str | os.PathLike) -> str:
    """Return the str-content of file at given path.

    Arguments:
        path: The path to get str content from
    """
    if "://" in str(path):
        return utils.fsspec_get(str(path))
    return pathlib.Path(path).read_text(encoding="utf-8")


def get_output_from_call(
    call: str | Sequence[str],
    cwd: str | os.PathLike | None,
) -> str | None:
    """Execute a system call and return its output as a string.

    Arguments:
        call: The system call to make
        cwd: The working directory for the call
    """
    import subprocess

    if not isinstance(call, str):
        call = " ".join(call)
    try:
        return subprocess.run(
            call,
            stdout=subprocess.PIPE,
            text=True,
            shell=True,
            cwd=cwd,
        ).stdout
    except subprocess.CalledProcessError:
        logger.warning("Executing %s failed", call)
        return None


def format_js_map(mapping: dict | str, indent: int = 4) -> str:
    """Return JS map str for given dictionary.

    Arguments:
        mapping: Dictionary to dump
        indent: The amount of indentation for the key-value pairs
    """
    dct = json.loads(mapping) if isinstance(mapping, str) else mapping
    rows = []
    indent_str = " " * indent
    for k, v in dct.items():
        match v:
            case bool():
                rows.append(f"{indent_str}{k}: {str(v).lower()},")
            case dict():
                rows.append(f"{indent_str}{k}: {format_js_map(v)},")
            case None:
                rows.append(f"{indent_str}{k}: null,")
            case _:
                rows.append(f"{indent_str}{k}: {v!r},")
    row_str = "\n" + "\n".join(rows) + "\n"
    return f"{{{row_str}}}"


def svg_to_data_uri(svg: str) -> str:
    """Wrap svg as data URL.

    Arguments:
        svg: The svg to wrap into a data URL
    """
    return f"url('data:image/svg+xml;charset=utf-8,{ svg }')"


def format_css_rule(dct: Mapping) -> str:
    """Format a nested dictionary as CSS rule.

    Mapping must be of shape {".a": {"b": "c"}}

    Arguments:
        dct: The mapping to convert to CSS text
    """
    data: dict[str, list] = {}

    def _parse(obj, selector: str = ""):
        for key, value in obj.items():
            if hasattr(value, "items"):
                rule = selector + " " + key
                data[rule] = []
                _parse(value, rule)

            else:
                prop = data[selector]
                prop.append(f"\t{key}: {value};\n")

    _parse(dct)
    string = ""
    for key, value in sorted(data.items()):
        if data[key]:
            string += key[1:] + " {\n" + "".join(value) + "}\n\n"
    return string


def add(text, prefix: str = "", suffix: str = ""):
    if not text:
        return ""
    return f"{prefix}{text}{suffix}"


def regex_replace(
    value: str = "",
    pattern: str = "",
    replacement: str = "",
    ignorecase: bool = False,
    multiline: bool = False,
    count: int = 0,
):
    """Perform a `re.sub` returning a string.

    Arguments:
        value: The value to search-replace.
        pattern: The regex pattern to use
        replacement: The replacement pattern to use
        ignorecase: Whether to ignore casing
        multiline: Whether to do a multiline regex search
        count: Amount of maximum substitutes.
    """
    import re

    flags = 0
    if ignorecase:
        flags |= re.I
    if multiline:
        flags |= re.M
    pat = re.compile(pattern, flags=flags)
    output, _subs = pat.subn(replacement, value, count=count)
    return output


def ternary(value: Any, true_val: Any, false_val: Any, none_val: Any = None):
    """Value ? true_val : false_val.

    Arguments:
        value: The value to check.
        true_val: The value to return if given value is true-ish
        false_val: The value to return if given value is false-ish
        none_val: Optional value to return if given value is None
    """
    if value is None and none_val is not None:
        return none_val
    if bool(value):
        return true_val
    return false_val


def do_any(seq: Sequence, attribute: str | None = None) -> bool:
    """Check if at least one of the item in the sequence evaluates to true.

    The `any` builtin as a filter for Jinja templates.

    Arguments:
        seq: An iterable object.
        attribute: The attribute name to use on each object of the iterable.

    Returns:
        A boolean telling if any object of the iterable evaluated to True.
    """
    if attribute is None:
        return any(seq)
    return any(_[attribute] for _ in seq)


def resolve(name: str, module: str | None = None):
    """Resolve ``name`` to a Python object via imports / attribute lookups.

    If ``module`` is None, ``name`` must be "absolute" (no leading dots).

    If ``module`` is not None, and ``name`` is "relative" (has leading dots),
    the object will be found by navigating relative to ``module``.

    Returns the object, if found.  If not, propagates the error.
    """
    names = name.split(".")
    if not names[0]:
        if module is None:
            msg = "relative name without base module"
            raise ValueError(msg)
        modules = module.split(".")
        names.pop(0)
        while not name[0]:
            modules.pop()
            names.pop(0)
        names = modules + names

    used = names.pop(0)
    found = importlib.import_module(used)
    for n in names:
        used += "." + n
        try:
            found = getattr(found, n)
        except AttributeError:
            importlib.import_module(used)
            found = getattr(found, n)

    return found


def is_instance(obj: object, typ: str | type) -> bool:
    kls = resolve(typ) if isinstance(typ, str) else typ
    if not isinstance(kls, type):
        raise TypeError(kls)
    return isinstance(obj, kls)


def is_subclass(obj: type, typ: str | type) -> bool:
    kls = resolve(typ) if isinstance(typ, str) else typ
    if not isinstance(kls, type):
        raise TypeError(kls)
    return issubclass(obj, kls)


ENV_GLOBALS = {
    "zip": zip,
    "now": datetime.datetime.now,
    "utcnow": datetime.datetime.utcnow,
    "importlib": importlib,
    "environment": version_info,
}
ENV_FILTERS = {
    "pformat": pprint.pformat,
    "format_code": utils.format_code,
    "html_link": html_link,
    "md_link": md_link,
    "wrap_in_elem": wrap_in_elem,
    "repr": repr,
    "zip": zip,
    "any": do_any,
    "rstrip": str.rstrip,
    "lstrip": str.lstrip,
    "removesuffix": str.removesuffix,
    "removeprefix": str.removeprefix,
    "contains": operator.contains,
    "regex_replace": regex_replace,
    "add": add,
    "pairwise": itertools.pairwise,
    "ternary": ternary,
    "issubclass": is_subclass,
    "isinstance": is_instance,
    "import_module": importlib.import_module,
    "hasattr": hasattr,
    "partial": functools.partial,
    "dump_json": json.dumps,
    "load_json": json.loads,
    "load_toml": tomllib.loads,
    "serialize": serialize,
    "load_file": load_file_cached,
    "path_join": os.path.join,
    "format_js_map": format_js_map,
    "format_css_rule": format_css_rule,
    "svg_to_data_uri": svg_to_data_uri,
    "check_output": get_output_from_call,
    "getenv": os.getenv,
}


ENV_TESTS = {
    "is_number": envtests.is_number,
    "list": envtests._is_list,
    "set": envtests._is_set,
    "tuple": envtests._is_tuple,
    "dict": envtests._is_dict,
    "datetime": envtests._is_datetime,
    "string_like": envtests._is_string_like,
    "subclass": is_subclass,
    "instance": is_instance,
    # "match": envtests.regex_match,
    # "search": envtests.regex_search,
    "contains": operator.contains,
}
