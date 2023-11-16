import json
import os
import sys
from glob import glob
from pathlib import Path
from typing import Any
from uuid import uuid4

import yaml
from airfold_common.config import merge_dicts
from airfold_common.format import Format
from airfold_common.utils import dict_from_env, model_hierarchy

from airfold_cli.models import (
    Config,
    LocalFile,
    ProjectFile,
    UserPermissions,
    UserProfile,
)

CONFIG_PATH = Path().cwd() / ".airfold" / "config.yaml"
CONFIG_DIR = os.path.dirname(CONFIG_PATH)
PROJECT_DIR = "airfold"

PREFIX = "AIRFOLD"


def uuid() -> str:
    return "af" + uuid4().hex


def save_config(config: Config) -> str:
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config.dict(), f)
    return str(CONFIG_PATH)


def load_config() -> Config:
    data = yaml.safe_load(open(CONFIG_PATH))

    env_data: dict = dict_from_env(model_hierarchy(Config), PREFIX)
    merge_dicts(data, env_data)

    return Config(**data)


def normalize_path_args(path: list[str] | str | None) -> list[str]:
    res: list[str]
    if not path:
        path = [os.path.join(os.getcwd(), PROJECT_DIR)]
    if isinstance(path, str):
        res = [path]
    else:
        res = path
    return res


def find_project_files(path: list[str], file_ext: list[str] = [".yaml", ".yml"]) -> list[Path]:
    res: list[Path] = []
    for ipath in path:
        resolved = [os.path.abspath(p) for p in glob(ipath)]
        for p in resolved:
            if os.path.isdir(p):
                for root, dirs, files in os.walk(p):
                    for f in files:
                        file_path = Path(os.path.join(root, f))
                        if file_path.suffix.lower() in file_ext:
                            res.append(file_path)
            elif os.path.exists(p):
                file_path = Path(p)
                if file_path.suffix.lower() in file_ext:
                    res.append(file_path)
    return res


def load_from_stream(stream: Any) -> list[ProjectFile]:
    res: list[ProjectFile] = []
    for doc in yaml.safe_load_all(stream):
        name = doc.get("name")
        if not name:
            raise ValueError(f"No name in document: {doc}")
        res.append(ProjectFile(name=name, data=doc))
    return res


def load_files(paths: list[Path]) -> list[ProjectFile]:
    res: list[ProjectFile] = []
    for path in paths:
        if path == Path("-"):
            res.extend(load_from_stream(sys.stdin))
        else:
            res.append(LocalFile(path=str(path), name=path.stem, data=yaml.safe_load(open(path))))
    return res


def str_presenter(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.representer.SafeRepresenter.add_representer(str, str_presenter)


class Dumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


def sort_keys(key: str) -> str:
    if key == "version":
        return "0"
    if key == "type":
        return "1"
    if key == "name":
        return "2"
    return key


def dump_yaml(data: list[dict] | dict, remove_names=False) -> str:
    if not isinstance(data, list):
        data = [data]
    out = []
    for d in data:
        keys = sorted(d.keys(), key=sort_keys)
        for k in keys:
            if remove_names and k == "name":
                d.pop(k)
                continue
            d[k] = d.pop(k)
        out.append(d)
    return yaml.dump_all(out, Dumper=Dumper, sort_keys=False)


def dump_json(data: dict) -> str:
    return json.dumps(data, indent=2)


def get_org_permissions(user: UserProfile, _org_id: str | None = None) -> UserPermissions | None:
    org_id: str = _org_id or user.organizations[0].id
    for perm in user.permissions:
        if perm.org_id == org_id:
            return perm
    return None


def display_roles(user: UserProfile, org_id: str, proj_id: str) -> str:
    if bool([org for org in user.organizations if org.id == org_id]):
        return "Owner"
    for perm in user.permissions:
        if perm.org_id == org_id:
            roles = perm.roles
            for r in roles:
                if f"projects/{proj_id}" in r:
                    return r
            return ",".join(roles)
    return ""


def set_current_project(proj_id):
    config = load_config()
    conf = Config(**config.dict(exclude={"proj_id"}), proj_id=proj_id)
    save_config(conf)


def get_local_files(formatter: Format, files: list[ProjectFile]) -> list[LocalFile]:
    res: list[LocalFile] = []
    for file in files:
        if formatter.is_pipe(file.data):
            prefix = "pipes"
        else:
            prefix = "sources"
        file_path = os.path.join(prefix, f"{file.name}.yaml")
        res.append(LocalFile(**file.dict(), path=file_path))
    return res


def dump_project_files(files: list[LocalFile], dst_path: str) -> None:
    for file in files:
        file_path = os.path.join(dst_path, file.path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, "w").write(dump_yaml(file.data, remove_names=True))
