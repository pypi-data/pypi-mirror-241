import os
import logging
import hashlib
from fnmatch import fnmatch
from typing import Union, Optional, List, Tuple


def get_default_logger():
    """Get a logging object using the default log level set in cfg.
    https://docs.python.org/3/library/logging.html
    """
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        stderr_handler = logging.StreamHandler()
        logger.addHandler(stderr_handler)
    return logger


def check_env_variables():
    """
    Check if necessary env variables are set
    """
    if (
        "OIP_API_HOST" not in os.environ
        or "WORKSPACE_ID" not in os.environ
        or "DATASET_WORKSPACE_NAME" not in os.environ
        or "DATASET_AUTHENTICATION_TOKEN" not in os.environ
    ):
        raise RuntimeError("NOT CONNECTED, PLEASE CALL CONNECT BEFORE STARTING...")


def sha256sum(
    filename: str, skip_header: Optional[int] = 0, block_size: Optional[int] = 65536
) -> Union[Tuple[str, str], Tuple[None, None]]:
    """
    create sha2 of the file, notice we skip the header of the file (32 bytes)
        because sometimes that is the only change
    :param filename: str: file name
    :param skip_header: int: default to 0 if 1 we skip
    :param block_size: int: default to 65536
    :return: union[(str,str),(none,none)]:
    """
    h = hashlib.sha256()
    file_hash = hashlib.sha256()
    b = bytearray(block_size)
    mv = memoryview(b)
    try:
        with open(filename, "rb", buffering=0) as f:
            # skip header
            if skip_header:
                file_hash.update(f.read(skip_header))
            for n in iter(lambda: f.readinto(mv), 0):
                h.update(mv[:n])
                if skip_header:
                    file_hash.update(mv[:n])
    except (Exception,):
        return None, None

    return h.hexdigest(), file_hash.hexdigest() if skip_header else None


def matches_any_wildcard(
    path: str, wildcards: Union[str, List], recursive: Optional[bool] = True
) -> bool:
    """
    Checks if given pattern matches any supplied wildcard

    :param path:str: path to check
    :param wildcards:union[str,list] wildcards to check against
    :param recursive: bool: whether or not the check is recursive. Default: True
        E.g. for path='directory/file.ext' and wildcards='*.ext',
        recursive=False will return False, but recursive=True will
        return True

    :return: bool: True if the path matches any wildcard and False otherwise
    """
    if wildcards is None:
        wildcards = ["*"]
    if not isinstance(wildcards, list):
        wildcards = [wildcards]
    wildcards = [str(w) for w in wildcards]
    if not recursive:
        path_as_list: List[str] = path.split("/")
    for wildcard in wildcards:
        if not recursive:
            wildcard = wildcard.split("/")
            matched: bool = True
            if len(path_as_list) != len(wildcard):
                continue
            for path_segment, wildcard_segment in zip(path_as_list, wildcard):
                if not fnmatch(path_segment, wildcard_segment):
                    matched = False
                    break
            if matched:
                return True
        else:
            wildcard_file: str = wildcard.split("/")[-1]
            wildcard_dir: str = wildcard[: -len(wildcard_file)] + "*"
            if fnmatch(path, wildcard_dir) and fnmatch(
                "/" + path, "*/" + wildcard_file
            ):
                return True
    return False


def format_size(
    size_in_bytes: Union[int, float],
    binary: Optional[bool] = False,
    use_nonbinary_notation: Optional[bool] = False,
    use_b_instead_of_bytes: Optional[bool] = False,
) -> str:
    """
    Return the size in human readable format (string)
    Matching humanfriendly.format_size outputs

    :param size_in_bytes:union[float,int]: number of bytes
    :param binary: bool: If `True` 1 Kb equals 1024 bytes, if False (default) 1 KB = 1000 bytes
    :param use_nonbinary_notation: bool: Only applies if binary is `True`. If this is `True`,
        the binary scale (KiB, MiB etc.) will be replaced with the regular scale (KB, MB etc.)
    :param use_b_instead_of_bytes: bool: If `True`, return the formatted size with `B` as the
        scale instead of `byte(s)` (when applicable)
    :return: string representation of the number of bytes (b,Kb,Mb,Gb, Tb,)
        >>> format_size(0)
        '0 bytes'
        >>> format_size(1)
        '1 byte'
        >>> format_size(5)
        '5 bytes'
        > format_size(1000)
        '1 KB'
        > format_size(1024, binary=True)
        '1 KiB'
        >>> format_size(1000 ** 3 * 4)
        '4 GB'
    """
    size: float = float(size_in_bytes)
    # single byte is the exception here
    if size == 1 and not use_b_instead_of_bytes:
        return "{} byte".format(int(size))
    k: int = 1024 if binary else 1000
    scale: List[str] = (
        ["bytes", "KiB", "MiB", "GiB", "TiB", "PiB"]
        if (binary and not use_nonbinary_notation)
        else ["bytes", "KB", "MB", "GB", "TB", "PB"]
    )
    if use_b_instead_of_bytes:
        scale[0] = "B"
    for i, m in enumerate(scale):
        if size < k ** (i + 1) or i == len(scale) - 1:
            return (
                (
                    "{:.2f}".format(size / (k**i)).rstrip("0").rstrip(".")
                    if i > 0
                    else "{}".format(int(size))
                )
                + " "
                + m
            )
    # we should never get here
    return f"{int(size)} {scale[0]}"


def is_within_directory(directory: str, target: str) -> bool:
    """
    Check if the path represented by 'target' is within or equal to the 'directory'.
    :param directory: str: The directory path to check against.
    :param target: str: The path to be checked.
    :return: bool: True if 'target' is within or equal to 'directory', False otherwise.
    """
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)
    prefix = os.path.commonprefix([abs_directory, abs_target])
    return prefix == abs_directory
