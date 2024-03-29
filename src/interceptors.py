# Initialized `interceptors.py` generated by ipm.
# Regists your pre-interceptors and interceptors here.
# Documents at https://ipm.hydroroll.team/

from infini.register import Register
from infini.router import Router
from infini.typing import Literal
from infini.input import Input

from diceutils.status import StatusPool
from diceutils.logging import Logger
from diceutils.utils import get_group_id, get_user_id
from diceutils.cards import CardsPool


class AllCommand(Router):
    type: Literal["all"] = "all"
    prefix: tuple = (".", "/", "。")

    def match(self, _: str) -> bool:
        return True


register = Register()
logger = Logger()


@register.pre_interceptor(AllCommand("*"), priority=0)
def logging_pre_interceptor(input: Input):
    session_id = get_group_id(input)
    user_id = get_user_id(input)

    status = StatusPool.get("dicergirl")
    cards = CardsPool.get(status.get(session_id, "mode")) or {}
    card_name = (cards.get(user_id) or {}).get("name") or input.variables.get(
        "nickname", "User"
    )

    kp = status.get(session_id, "kp") or []
    pl = status.get(session_id, "pl") or []

    if user_id in kp:
        role = "KP"
    elif user_id in pl:
        role = "PL"
    else:
        role = "OB"

    active_loggers: set = status.get(session_id, "active_loggers") or set()
    for active_logger in active_loggers:
        logger.add(
            session_id,
            active_logger,
            user_id=user_id,
            user_role=role,
            card_name=card_name,
            data=input.variables.get("message"),
            message_sequence="xxx",
        )

    return input


@register.interceptor(AllCommand("*"), priority=0)
def dicer_logging_interceptor(input: Input, plain_text: str):
    status = StatusPool.get("dicergirl")

    session_id = get_group_id(input)

    active_loggers: set = status.get(session_id, "active_loggers") or set()
    for active_logger in active_loggers:
        logger.add(
            session_id,
            active_logger,
            user_id=input.variables.get("self_id", "bot"),
            user_role="DICER",
            card_name=status.get("bot", "name") or "Dicer",
            data=[{"type": "text", "data": {"text": plain_text}}],
            message_sequence="xxx",
        )

    return input
