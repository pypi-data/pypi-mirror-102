import argparse
import json
import os
import typing

__all__ = ["Configuration", "ConfigurationOptions", "from_file", "from_args"]

class ConfigurationOptions:
    @classmethod
    def default(cls) -> "ConfigurationOptions":
        default_name = "_default"

        val = getattr(cls, default_name, None)
        if not val:
            val = cls()
            setattr(cls, default_name, val)

        return val
    
    def __init__(self, relative_root_name: str or None = "root", config_arg: str or None = "config", index_file_name="index.json", extends_field_name: str or None ="extends") -> None:
        self.relative_root_name = relative_root_name
        self.config_arg = config_arg
        self.index_file_name = index_file_name
        self.extends_field_name = extends_field_name

GetValueType = typing.TypeVar("GetValueType")

class Configuration:
    def __init__(self, vals: dict, root_dir: str, base_config: "Configuration" = None, options: ConfigurationOptions = None):
        self.__args = vals
        self.__dir = root_dir
        self.__base_config = base_config
        self.__options = options
        
    def __getitem__(self, key) -> str:
        return self.get_value(key, required = True)

    def get_raw_value(self, name: str, required = False) -> typing.Any:
        val = self.__args.get(name)

        if val:
            return val
        elif self.__base_config:
            return self.__base_config.get_raw_value(name, required=required)
        elif required:
            raise ValueError(f"Value for configuration property '{name}' was not found!")
        else:
            return None  

    def get_dict_value(self, name: str, required = False) -> dict:
        raw = self.get_raw_value(name, required=required)

        if isinstance(raw, dict):
            return raw

        path = self._file_name_to_path(raw)

        with open(path, "r") as fp:
            return json.load(fp)

    def get_value(self, name: str, dtype: typing.Type[GetValueType] = str, required = False) -> GetValueType:
        val = self.get_raw_value(name, required=required)

        if val:
            return dtype(val)
        else:
            return None

    def _file_name_to_path(self, file_name: str, dir_name_name: str = None) -> os.PathLike:
        root_dir = self.__dir

        dir_name = dir_name_name and self.__args.get(dir_name_name)

        if dir_name:
            root_dir = os.path.join(root_dir, dir_name)

        return os.path.join(root_dir, file_name)

    def get_fully_qualified_path(self, file_name_name: str, dir_name_name: str = None, required = False) -> os.PathLike or None:

        file_name = self.__args.get(file_name_name)

        if file_name:
            return self._file_name_to_path(file_name, dir_name_name)
        elif self.__base_config:
            return self.__base_config.get_fully_qualified_path(file_name_name, dir_name_name, required=required)
        elif required:
            raise ValueError(f"Value for configuration property '{file_name_name}' was not found!")
        else:
            return None

    def _get_sub_config_from_value(self, val: dict or str, is_nested = False) -> "Configuration":
        base_config = self if is_nested else None

        if isinstance(val, str):
            path = self._file_name_to_path(val)

            return from_file(path, base_config, options=self.__options)
        elif isinstance(val, dict):
            return Configuration(val, self.__dir, self.__base_config)
        else:
            raise ValueError()

    def get_multi_sub_config(self, name: str, is_nested = False, required = False) -> typing.Generator["Configuration", None, None]:
        val = self.__args.get(name)

        if val:
            for v in val:
                yield self._get_sub_config_from_value(v, is_nested)
        elif self.__base_config:
            return self.__base_config.get_multi_sub_config(name, is_nested=is_nested, required=required)
        elif required:
            raise ValueError(f"Sub-config '{name}' was not found!")
        else:
            return

    def get_sub_config(self, name: str, is_nested = False, required = False) -> typing.Union["Configuration", None]:
        val = self.__args.get(name)

        if val:
            return self._get_sub_config_from_value(val, is_nested)
        elif self.__base_config:
            return self.__base_config.get_sub_config(name, is_nested=is_nested, required=required)
        elif required:
            raise ValueError(f"Sub-config '{name}' was not found!")
        else:
            return None

def from_file(path: str, base_config: Configuration = None, options: ConfigurationOptions = None) -> Configuration:
    if not options:
        options = ConfigurationOptions.default()
    
    if os.path.isdir(path):
        dir_name = path
        path = os.path.join(path, options.index_file_name)
    else:
        dir_name = os.path.dirname(path)
    
    try:    
        with open(path, "r") as fp:
            config_dict: dict = json.load(fp)

        if options.extends_field_name:
            extends_path = config_dict.get(options.extends_field_name)
            if extends_path:
                extends_path = os.path.join(dir_name, extends_path)
                base_config = from_file(extends_path, base_config=base_config, options=options)
            
    except FileNotFoundError:
        raise ValueError(f"Error while reading configuration index file. Path does not exist: '{path}'")

    if options.relative_root_name:
        relative_root = config_dict.get(options.relative_root_name)

        if relative_root:
            dir_name = os.path.join(dir_name, relative_root)

    return Configuration(config_dict, dir_name, base_config, options)

def from_args(args: argparse.Namespace, options: ConfigurationOptions = None) -> Configuration:
    if not options:
        options = ConfigurationOptions.default()
    
    base_config = None

    if options.config_arg:
        config_path = getattr(args, options.config_arg, None)

        if config_path:
            base_config = from_file(config_path, options=options)

    config = Configuration(vars(args), ".", base_config, options)

    return config
