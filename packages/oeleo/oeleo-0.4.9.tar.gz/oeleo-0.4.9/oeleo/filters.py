import logging
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Any, Generator, Iterable

log = logging.getLogger("oeleo")


def filter_on_not_before(path: Path, value: datetime):
    st = path.stat()
    sdt = datetime.fromtimestamp(st.st_mtime)
    if sdt >= value:
        return True
    else:
        return False


def filter_on_not_after(path: Path, value: datetime):
    st = path.stat()
    sdt = datetime.fromtimestamp(st.st_mtime)
    if sdt <= value:
        return True
    else:
        return False


FILTERS = {
    "not_before": filter_on_not_before,
    "not_after": filter_on_not_after,
}

FilterFunction = Any
FilterTuple = Any  # tuple[str, FilterFunction] for py3.10


def base_filter(
    path: Path,
    extension: str = None,
    additional_filters: Iterable[FilterTuple] = None,
    base_filter_func: Any = None,
) -> Generator[Path, None, None]:

    """Simple directory content filter - cannot be used for ssh"""

    if base_filter_func is None:
        base_filter_func = path.glob

    file_list = base_filter_func(f"*{extension}")

    if additional_filters is not None:
        file_list = additional_filtering(file_list, additional_filters)

    return file_list


def additional_filtering(
    file_list: Iterable, additional_filters: Iterable[FilterTuple] = None
) -> Iterable:
    for filter_name, filter_val in additional_filters:
        filter_func = FILTERS[filter_name]
        file_list = filter(partial(filter_func, value=filter_val), file_list)
    return file_list


def main():
    directory = Path("../check/from").resolve()
    not_before = datetime(year=2022, month=7, day=1, hour=1, minute=0, second=0)
    not_after = datetime(year=2022, month=8, day=4, hour=1, minute=0, second=0)
    print(f"not_before: {not_before}")
    print(f"not_after: {not_after}")
    for f in directory.glob("*"):
        print(f"file: {f}: {datetime.fromtimestamp(f.stat().st_mtime)}")
    extension = ".xyz"

    print("Starting...")

    my_filters = [
        ("not_before", not_before),
        ("not_after", not_after),
    ]

    g = base_filter(directory, extension, additional_filters=my_filters)
    print("This is what I got after filtering:")
    for n, f in enumerate(g):
        st_mtime = datetime.fromtimestamp(f.stat().st_mtime)
        print(f"{n+1}: {f} {st_mtime} not-before: {st_mtime >= not_before} not-after: {st_mtime <= not_after}")


if __name__ == "__main__":
    main()
