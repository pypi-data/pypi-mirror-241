"""Define package contents."""
import importlib.resources
import json

import pydantic


class PackageMetadata(pydantic.BaseModel):
    """Define keys and types of corresponding values for package metadata."""

    Name: str
    Version: str
    Description: str
    Keywords: list[str]
    License: str
    Maintainers: list[str]
    Authors: list[str]
    Links: dict[str, pydantic.HttpUrl]


METADATA_CONTENTS: str = (
    importlib.resources.files("package_name_to_import_with").joinpath("metadata.json").read_text()
)
METADATA = PackageMetadata(**json.loads(METADATA_CONTENTS))
