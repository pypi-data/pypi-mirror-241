from dicergirl.utils.docimasy import Docimasy
import random


def scp_doc(result, difficulty, encourage=None, agent=None, great=False) -> Docimasy:
    """类 SCP 模式技能检定结果"""
    if not agent:
        agent = "该特工"

    r = Docimasy(f"事件难度: {difficulty}")

    if difficulty > 25 and result <= difficulty:
        r += f"检定数据: {result}"
        r += f"检定结果: 致命失败."
        r += f"检定结论: {agent} 在试图挑战数学、挑战科学、挑战真理, 尝试达成一个不可能事件, {agent} 毫无疑问获得了 致命失败."
        r.set_judge("fatal fail")
        return r

    if encourage:
        r += f"肾上腺素: {encourage}"
        r += f"检定数据: {result}+{encourage}"
        result += encourage
    else:
        r += f"检定数据: {result}"

    if great:
        r += "检定结果: 关键成功."
        if result <= difficulty:
            r += "检定结论: 有时候, 一次普通的成功或许会大幅度的牵扯到整个未来, 但这并不是一件太过于值得高兴的事情, 因为它不见得是一个好的开始."
        else:
            r += "检定结论: 被 Administrator 所眷顾的人, 毫无疑问这是一次完美的成功, 但是你或许会面对更加绝望的未来."
        r.set_judge("critical success")
    elif result >= (difficulty * 2):
        r += "检定结果: 关键成功."
        r += "检定结论: 绝境之中的人常常能够爆发出无尽的潜力, 疯狂是人类最强大的武器, 用疯狂去嗤笑命运吧."
        r.set_judge("critical success")
    elif result > difficulty:
        r += "检定结果: 成功."
        r += "检定结论: 命运常常给予人们无声的嗤笑, 一次成功当然是好事, 但也要警惕这是否是步入深渊的开始."
        r.set_judge("success")
    elif result < (difficulty / 2):
        r += "检定结果: 致命失败."
        r += "检定结论: 努力或许的确有用处, 但是努力只是提高运气的一种手段. 在低劣的运气面前, 任何努力都是没有用的."
        r.set_judge("fatal fail")
    elif result < difficulty:
        r += "检定结果: 失败."
        r += "检定结论: 人类从来都生活在饱含恐惧与绝望的危险之中, 失败是一件稀松平常的事情, 小心, 错误的决定或许会让你步入深渊."
        r.set_judge("fail")
    else:
        result = random.randint(0, 1)
        if result:
            r += "检定结果: 成功."
            r += "检定结论: 小心, 你的成功完全是一次偶然, 不要试图去将这样的偶然当做希望."
            r.set_judge("success")
        else:
            r += "检定结果: 失败."
            r += "检定结论: 成功与失败宛如山顶与深渊, 无论是哪一种都是可能的, 相反, 在这个世界落入深渊是一件更加合理的事情."
            r.set_judge("fail")
    return r
