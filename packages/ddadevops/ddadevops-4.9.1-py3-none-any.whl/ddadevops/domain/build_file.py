import json
import re
from enum import Enum
from typing import Optional
from pathlib import Path
from .common import Validateable
from .version import Version


class BuildFileType(Enum):
    JS = ".json"
    JAVA_GRADLE = ".gradle"
    JAVA_CLOJURE = ".clj"
    PYTHON = ".py"


class BuildFile(Validateable):
    def __init__(self, file_path: Path, content: str):
        self.file_path = file_path
        self.content = content

    def validate(self):
        result = []
        result += self.__validate_is_not_empty__("file_path")
        result += self.__validate_is_not_empty__("content")
        if not self.build_file_type():
            result += [f"Suffix {self.file_path} is unknown."]
        return result

    def build_file_type(self) -> Optional[BuildFileType]:
        result: Optional[BuildFileType] = None
        if not self.file_path:
            return result
        config_file_type = self.file_path.suffix
        match config_file_type:
            case ".json":
                result = BuildFileType.JS
            case ".gradle":
                result = BuildFileType.JAVA_GRADLE
            case ".clj":
                result = BuildFileType.JAVA_CLOJURE
            case ".py":
                result = BuildFileType.PYTHON
            case _:
                result = None
        return result

    def get_version(self) -> Version:
        try:
            match self.build_file_type():
                case BuildFileType.JS:
                    version_str = json.loads(self.content)["version"]
                case BuildFileType.JAVA_GRADLE:
                    # TODO: '\nversion = ' will not parse all ?!
                    version_line = re.search("\nversion = .*", self.content)
                    version_line_group = version_line.group()
                    version_string = re.search(
                        "[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?", version_line_group
                    )
                    version_str = version_string.group()
                case BuildFileType.PYTHON:
                    # TODO: '\nversion = ' will not parse all ?!
                    version_line = re.search("\nversion = .*\n", self.content)
                    version_line_group = version_line.group()
                    version_string = re.search(
                        "[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?(-dev)?[0-9]*",
                        version_line_group,
                    )
                    version_str = version_string.group()
                case BuildFileType.JAVA_CLOJURE:
                    # TODO: unsure about the trailing '\n' !
                    version_line = re.search("\\(defproject .*\n", self.content)
                    version_line_group = version_line.group()
                    version_string = re.search(
                        "[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?", version_line_group
                    )
                    version_str = version_string.group()
        except:
            raise RuntimeError(f"Version not found in file {self.file_path}")

        result = Version.from_str(version_str, self.get_default_suffix())
        result.throw_if_invalid()

        return result

    def set_version(self, new_version: Version):
        # TODO: How can we create regex-pattern constants to use them at both places?

        if new_version.is_snapshot():
            new_version.snapshot_suffix = self.get_default_suffix()

        try:
            match self.build_file_type():
                case BuildFileType.JS:
                    json_data = json.loads(self.content)
                    json_data["version"] = new_version.to_string()
                    self.content = json.dumps(json_data, indent=4)
                case BuildFileType.JAVA_GRADLE:
                    substitute = re.sub(
                        '\nversion = "[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?"',
                        f'\nversion = "{new_version.to_string()}"',
                        self.content,
                    )
                    self.content = substitute
                case BuildFileType.PYTHON:
                    substitute = re.sub(
                        '\nversion = "[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?(-dev)?[0-9]*"',
                        f'\nversion = "{new_version.to_string()}"',
                        self.content,
                    )
                    self.content = substitute
                case BuildFileType.JAVA_CLOJURE:
                    # TODO: we should stick here on defproject instead of first line!
                    substitute = re.sub(
                        '"[0-9]*\\.[0-9]*\\.[0-9]*(-SNAPSHOT)?"',
                        f'"{new_version.to_string()}"',
                        self.content,
                        1,
                    )
                    self.content = substitute
        except:
            raise RuntimeError(f"Version not found in file {self.file_path}")

    def get_default_suffix(self) -> str:
        result = "SNAPSHOT"
        match self.build_file_type():
            case BuildFileType.PYTHON:
                result = "dev"
        return result

    def __eq__(self, other):
        return other and self.file_path == other.file_path

    def __hash__(self) -> int:
        return self.file_path.__hash__()
