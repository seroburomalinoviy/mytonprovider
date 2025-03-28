from .utils import generate_login, generate_password, get_package_path

from random import randint
from mypylib import add2systemd, Dict, MyPyClass
from mypylib import GetConfig, SetConfig
import subprocess


def install(util: str = None, storage_path: str = None, user: str ="root", **kwargs):
    name = util.lower()
    host = "localhost"
    port = randint(1024, 49151)
    login = generate_login()
    password = generate_password()
    path = storage_path
    bin_path = "/usr/bin/"

    subprocess.run(["bash", get_package_path() + "scripts/ton_storage_install.sh", path])

    cmd = f"{bin_path} --api {host}:{port} --api-login {login} --api-password {password}"

    add2systemd(
        name=name,
        start=cmd,
        workdir=storage_path,
    )

    local = MyPyClass("./mypyclass.py")
    start_service(local, name)
    stop_service(local, name)

    mconfig_path = f"/home/{user}/.local/share/mytonprovider/mytonprovider.db"
    mconfig = GetConfig(path=mconfig_path)
    ton_storage = Dict()
    ton_storage.api.port = port
    ton_storage.api.host = host
    ton_storage.api.login = login
    ton_storage.api.password = password
    ton_storage.api.path = path
    mconfig.ton_storage = ton_storage
    SetConfig(path=mconfig_path, data=mconfig)





