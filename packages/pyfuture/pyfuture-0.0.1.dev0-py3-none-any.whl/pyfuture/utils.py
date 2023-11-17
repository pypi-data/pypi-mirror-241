from libcst.codemod import Codemod, transform_module, TransformFailure, TransformExit, TransformSkip
from loguru import logger


def exec_transform(
    transform: Codemod,
    code: str,
    *,
    python_version: str|None = None,
) -> str | None:
    result = transform_module(transform, code, python_version=python_version)
    if isinstance(result, (TransformFailure, TransformExit, TransformSkip)):
        return None
    return result.code
