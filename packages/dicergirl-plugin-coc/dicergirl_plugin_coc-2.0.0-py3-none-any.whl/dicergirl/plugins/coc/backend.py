from dicergirl.utils.docimasy import judger
from dicergirl.utils.dicer import Dicer
from dicergirl.reply.manager import manager
from nonebot.adapters import Event
from multilogging import multilogger

from .cards import coc_cards, coc_attrs_dict
from .investigator import Investigator
from .madness import temporary_madness, madness_end, phobias, manias

import random


logger = multilogger(name="DicerGirl", payload="plugins.coc.handlers")
""" `coc.handlers`日志 """


def sc(arg: str, event: Event):
    """ COC 疯狂检定 """
    if not arg:
        return "使用`.help sc`查看使用帮助."

    reply = []
    try:
        args = arg.split(" ")
        args = list(filter(None, args))
        using_card = False
        s_and_f = args[0].split("/")
        success = Dicer(s_and_f[0]).roll().outcome
        failure = Dicer(s_and_f[1]).roll().outcome

        if len(args) > 1:
            card = {"san": int(args[1]), "name": "未指定调查员"}
            reply.append("用户指定了应当检定的 SAN 值, 这会使得本次检定不会被记录.")
            using_card = False
        else:
            card = coc_cards.get(event)
            using_card = True

        docimasy_number = Dicer().roll().calc()
        san_before = card["san"]

        if docimasy_number <= card["san"]:
            down = success
            docimasy_status = "成功"
        else:
            down = failure
            docimasy_status = "失败"
        if down >= card["san"]:
            docimasy_result = "陷入了永久性疯狂"
        elif down >= (card["san"] // 5):
            docimasy_result = "陷入了不定性疯狂"
        elif down >= 5:
            docimasy_result = "陷入了临时性疯狂"
        else:
            docimasy_result = "未受到严重影响"
        card["san"] -= down
        if card["san"] <= 0:
            card["san"] = 0
        sc_result = manager.process_generic_event(
            "plugins.coc.sancheck",
            event=event,
            CardName=card['name'],
            SANBefore=san_before,
            SAN=card['san'],
            DocimasyNumber=docimasy_number,
            DocimasyStatus=docimasy_status,
            DocimasyResult=docimasy_result,
            SANDown=down
        )
        reply.append(sc_result)

        if using_card:
            coc_cards.update(event, card)

        return reply
    except:
        return "产生了未知的错误, 你可以使用`.help sc`指令查看指令使用方法.\n如果你确信这是一个错误, 建议联系开发者获得更多帮助.\n如果你是具有管理员权限, 你可以使用`.debug on`获得更多信息."


def at(event: Event, args: str):
    """ COC 伤害检定 """
    got = coc_cards.get(event)
    if not got:
        db_num = "0"
    else:
        db_num = Investigator().load(got).db()

    method = "+"

    if args:
        d = Dicer(args).roll()
    else:
        d = Dicer("1d6").roll()

    db = Dicer(db_num).roll()
    dbtotal = db.outcome
    db = db.db

    return f"投掷 {d.db}{method}{db}=({d.outcome}+{dbtotal})\n造成了 {d.outcome+dbtotal}点 伤害."


def dam(event: Event, args: list):
    """ COC 承伤检定 """
    card = coc_cards.get(event)
    if not card:
        return "未找到缓存数据, 请先使用`.coc`指令进行车卡生成角色卡并`.set`进行保存."

    max_hp = card["con"] + card["siz"]

    try:
        arg = int(args[0])
        card["hp"] -= arg
        r = f"{card['name']} 失去了 {arg}点 生命"
    except:
        d = Dicer("1d6").roll()
        card["hp"] -= d.outcome
        r = "投掷 1D6={d}\n受到了 {d}点 伤害".format(d=d.outcome)

    if card["hp"] <= 0:
        card["hp"] = 0
        r += f", 调查员 {card['name']} 已死亡."
    elif (max_hp * 0.8) <= card["hp"] and (card["hp"] < max_hp):
        r += f", 调查员 {card['name']} 具有轻微伤."
    elif (max_hp * 0.6 <= card["hp"]) and (card["hp"] <= max_hp * 0.8):
        r += f", 调查员 {card['name']} 进入轻伤状态."
    elif (max_hp * 0.2 <= card["hp"]) and (card["hp"] <= max_hp * 0.6):
        r += f", 调查员 {card['name']} 身负重伤."
    elif max_hp * 0.2 >= card["hp"]:
        r += f", 调查员 {card['name']} 濒死."
    else:
        r += "."

    coc_cards.update(event, card)
    return r


def ra(event: Event, args: list, bp=None):
    """ COC 技能检定 """
    if len(args) == 0:
        return "错误: 检定技能需要给入技能名称.\n使用`.help ra`指令查看指令使用方法."

    if len(args) > 4:
        return "错误: 参数过多(最多4需要但%d给予)." % len(args)

    skill_name = args[0]

    card_data = coc_cards.get(event)
    if not card_data:
        if len(args) == 1:
            return str(judger(event, Dicer(), 0, name=skill_name))

        return str(judger(event, Dicer(), int(args[1]), name=skill_name))

    inv = Investigator().load(card_data)

    is_base = False
    exp = None
    for attr_name, alias in coc_attrs_dict.items():
        if args[0] in alias:
            exp = int(getattr(inv, alias[0]))
            is_base = True
            skill_name = attr_name
            break

    if not is_base:
        for skill in inv.skills:
            if args[0] == skill:
                exp = inv.skills[skill]
                break
            else:
                exp = False

    if not exp:
        if len(args) == 1:
            exp = 0
        elif not args[1].isdigit():
            return "技能值应当为整型数, 使用`.help ra`查看技能检定指令使用帮助."
        else:
            exp = int(args[1])

        return judger(event, Dicer(), exp, name=args[0]).detail
    elif exp and len(args) > 1:
        if not args[1].isdigit():
            return "技能值应当为整型数, 使用`.help ra`查看技能检定指令使用帮助."

        reply = [f"你已经设置了技能 {args[0]} 为 {exp}, 但你指定了检定值, 使用指定检定值作为替代."]
        reply.append(str(judger(event, Dicer(), int(args[1]), name=args[0])))
        return reply

    time = 1
    r = judger(event, Dicer(), exp, name=skill_name)

    for _ in range(time-1):
        r += judger(event, Dicer(), exp, name=args[0])

    return r.detail


def ti():
    """ COC 临时疯狂检定 """
    i = random.randint(1, 10)
    r = "临时疯狂判定1D10=%d\n" % i
    r += temporary_madness[i-1]

    if i == 9:
        j = random.randint(1, 100)
        r += "\n恐惧症状为: \n"
        r += phobias[j-1]
    elif i == 10:
        j = random.randint(1, 100)
        r += "\n狂躁症状为: \n"
        r += manias[j-1]

    r += "\n该症状将会持续1D10=%d" % random.randint(1, 10)
    return r


def li():
    """ COC 总结疯狂检定 """
    i = random.randint(1, 10)
    r = "总结疯狂判定1D10=%d\n" % i
    r += madness_end[i-1]

    if i in [2, 3, 6, 9, 10]:
        r += "\n调查员将在1D10=%d小时后醒来" % random.randint(1, 10)

    if i == 9:
        j = random.randint(1, 100)
        r += "\n恐惧症状为: \n"
        r += phobias[j-1]
    elif i == 10:
        j = random.randint(1, 100)
        r += "\n狂躁症状为: \n"
        r += manias[j-1]

    return r


def en(event: Event, args: list):
    """ COC 技能成长检定 """
    if not args:
        return "错误: 检定技能需要给入技能名称.\n使用`.help en`指令查看指令使用方法."

    exp = 0

    got = coc_cards.get(event)
    if not got:
        inv_dict = Investigator().__dict__
        coc_cards.update(event, inv_dict, save=True)
        got = inv_dict

    inv = Investigator().load(got)
    for skill in inv.skills.keys():
        if args[0] == skill:
            exp = inv.skills[skill]
            break

    dice = Dicer("1d100").roll()
    check = dice.outcome

    if check > exp or check > 95:
        plusdice = Dicer(f"{exp}+1d10").roll()
        plus = plusdice.outcome
        status = "成功"
    else:
        plusdice = Dicer(f"{exp}+0").roll()
        plus = plusdice.outcome
        status = "失败"

    inv.skills[args[0]] = plus
    coc_cards.update(event, inv.__dict__, save=True)
    return manager.process_generic_event(
        "plugins.coc.encourage",
        event=event,
        SkillName=args[0],
        Value=exp,
        DiceDescription=dice.description(),
        DocimasyStatus=status,
        EnDiceDesc=plusdice.description()
    )