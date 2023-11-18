from dicergirl.common.messages import regist
from dicergirl.reply.manager import manager


def message_regist():
    """消息事件注册"""
    manager.register_event(
        "plugins.coc.sancheck",
        "[{SenderCard}]调查员: {CardName}\n检定精神状态: {SANBefore}\n理智检定值: {DocimasyNumber}, 检定{DocimasyStatus}.\n{CardName} 理智降低了 {SANDown} 点, {DocimasyResult}.\n当前 {CardName} 的 SAN 值为: {SAN}.",
    )
    manager.register_event(
        "plugins.coc.encourage",
        "[{SenderCard}]进行技能[{SkillName}:{Value}]成长检定: {DiceDescription}\n检定{DocimasyStatus}, 技能增长{EnDiceDesc}.",
    )


def init():
    message_regist()
    regist(
        "克苏鲁",
        """用法：.coc [天命次数] [指令] [选项]
描述：
    完成 COC 人物作成。
指令：
    [ROLL]   天命次数
    cache    给出所有天命池中的人物卡
    set <ID>   使用天命池中序列为ID的人物卡
    age <AGE>    预设置调查员年龄
    name <名称>   调查员姓名
    sex <ID>   调查员性别
    age <ID>   调查员年龄
示例：
    .coc 7   进行7次COC天命
    .coc 5 name 欧若可 sex 女 age 20   预设定5次天命的人物卡为20岁女性人物欧若可
注意：
    - 以上指令均可缺省.
    - 调查员的外貌、教育值等值与年龄相关.""",
        alias=["coc", "克苏鲁"],
    )
    regist(
        "理智检定",
        """用法：.sc <成功表达式>/<失败表达式> [SAN]
描述：
    COC 角色理智检定。
示例：
    .sc 1d5/1d10
注意：
- 表达式支持掷骰表达式语法, 例如1d10.
- 指定检定的 SAN 值不会修改人物卡数据.
- 缺省SAN则会自动使用该用户已保存的人物卡数据, 检定结束后人物卡SAN会被修改.""",
        alias=["sc", "sancheck", "理智检定"],
    )
    regist(
        "临时疯狂检定",
        """用法：.ti
描述：
    对调查员进行临时疯狂检定""",
        alias=["ti", "临时疯狂", "临时疯狂检定"],
    )
    regist(
        "总结疯狂检定",
        """用法：.li
描述：
    对调查员进行总结疯狂检定""",
        alias=["li", "总结疯狂", "总结疯狂检定"],
    )
