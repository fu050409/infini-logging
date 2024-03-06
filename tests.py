from infini.loader import Loader
from infini.input import Input
from diceutils.cards import CardsPool
from ipm import api
from ipm.models.ipk import InfiniProject
from pathlib import Path

ipk = InfiniProject(Path(__file__).resolve().parent)
api.build(Path(__file__).resolve().parent, echo=True)
api.install(
    str(Path(__file__).resolve().parent.joinpath("dist", f"{ipk.default_name}")),
    force=True,
    upgrade=True,
    echo=True,
)

with Loader() as loader:
    print(f"Loading {ipk.name}...")
    loader.load(ipk.name)
core = loader.into_core()


commands = [
    ".log clear",
    ".log new",
    ".kp",
    ".log new",
    ".kp",
    ".log",
    ".pl",
    ".log",
    "测试",
    ".log stop 0",
    ".log start 0",
    ".pl",
    ".log export 0 name 测试",
]


def test():
    CardsPool.register("coc")
    for command in commands:
        print("测试指令:", command)
        print("=============== start ===============")
        for output in core.input(
            Input(
                command,
                variables={
                    "nickname": "苏向夜",
                    "message": [{"type": "text", "data": {"text": command}}],
                },
            )
        ):
            print(output)
        print("================ end ================")
        print()


test()
