from nonebot.plugin import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, MessageEvent
from nonebot import MatcherGroup, CommandGroup, export, logger
from src.plugins.hoke.selectMysql import QueryWeiboAll, QueryQQ, QueryMobole, QueryWeibo
from src.urils.tool import is_number, validPhone, fomatMessage

'''聊天模式'''
pBot_mes_group = MatcherGroup(type='message', priority=20, block=True)
pbot_cmd = pBot_mes_group.on_command('q')


@pbot_cmd.handle()
async def queryPhoneInfo(bot: Bot, event: MessageEvent):
    mes = str(event.message).strip()
    if mes == '637442240':
        return 0
    bool = validPhone(mes)
    bList = ""
    mobiles = []
    weibo = []
    if is_number(mes):
        if bool:
            mobiles = QueryMobole(mes)
            weibo = QueryWeibo(mes)
        else:
            mobiles = QueryQQ(mes)
            weibo = QueryWeiboAll(mobiles)
        bList = fomatMessage(mobiles, weibo)
    else:
        bList = "你说啥？"

    await pbot_cmd.send(bList)
