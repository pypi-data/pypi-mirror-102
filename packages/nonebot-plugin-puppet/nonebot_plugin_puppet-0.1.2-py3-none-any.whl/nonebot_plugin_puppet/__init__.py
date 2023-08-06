from nonebot.permission import SUPERUSER
from nonebot.plugin import on_message, on_shell_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, PrivateMessageEvent

from .data import get_conv_mapping
from .parser import puppet_parser

puppet = on_shell_command(
    "puppet", parser=puppet_parser, priority=1, permission=SUPERUSER
)
puppet_ = on_message(priority=10, block=False)


@puppet.handle()
async def _(bot: Bot, event: PrivateMessageEvent, state: T_State):
    args = state["args"]
    args.origin = event.user_id
    args.user_id = None
    args.group_id = None
    if hasattr(args, "handle"):
        args = args.handle(args)
        if args.message:
            await bot.send_msg(
                user_id=args.user_id, group_id=args.group_id, message=args.message
            )


@puppet_.handle()
async def _(bot: Bot, event: Event):
    conv_mapping = get_conv_mapping()
    reverse_conv_mapping = get_conv_mapping(reverse=True)

    if isinstance(event, PrivateMessageEvent):
        conv_id = event.user_id
    elif isinstance(event, GroupMessageEvent):
        conv_id = event.group_id

    user_id, group_id = None, None

    if conv_id in reverse_conv_mapping:
        user_id = reverse_conv_mapping[conv_id]
    elif conv_id in conv_mapping:
        if conv_mapping[conv_id]["type"] == "user":
            user_id = conv_mapping[conv_id]["conv_id"]
        else:
            group_id = conv_mapping[conv_id]["conv_id"]

    await bot.send_msg(user_id=user_id, group_id=group_id, message=event.get_message())
