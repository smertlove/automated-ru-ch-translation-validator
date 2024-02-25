from . import TagWrapper
from . import Comporator
from . import EnhancedRegexps
from . import UserRules



class TranslationChecker:

    rules = UserRules.RULES
    preprocessor = EnhancedRegexps.OrdinaryRegexBuilder(rules=rules)

    @classmethod
    def check_translation(cls, translation: str, regex: str):
        comparation_result = ''.join(Comporator.ChineseRegexpComporator.compare(translation, cls.preprocessor.get_ordinary_regexp(regex)))
        return TagWrapper.TagWrapper.mk_html_tags(comparation_result)








def main():

    _testcases = (
        ("您好，王老师。你们好。欢迎，请进。", "<s你>好，王老师。<s你>好。欢迎，请进。"),
        ("您好吗？我很好。", "<s你>好吗？我很?好。"),
        ("请进。你喝茶吗？", "请进。<s你>喝茶吗？"),
        ("这是中国茶。中国茶很好。", "这是中国茶。中国茶很?好喝?。"),
        ("请喝píjiǔ。您喝什么啤酒？我喝déguó píjiǔ。déguó píjiǔ很好喝。", "请喝<p啤酒>。<s你>喝什么<p啤酒>？我喝<p德国><p啤酒>。<p德国><p啤酒>很?好喝?。"),
        ("请吸烟。我不吸烟。", "请吸烟。我不吸烟。"),
        ("你喝kāfēi吗？谢谢。不客气。", "<s你>喝<p咖啡>吗？谢谢。不客气。"),
        ("您喝什么？我喝茶。谢谢。", "<s你>喝什么？我喝茶。谢谢。"),
        ("中国人喝茶，éluósī人也喝茶。éluósī人也喝kāfēi。", "中国人喝茶，<p俄罗斯>人也喝茶。<p俄罗斯>人也喝<p咖啡>。"),
        ( "他是中国人。中国人不喝niúnǎi。", "他是中国人。中国人不喝<p牛奶>。"),
        ( "欢迎您。您是谁？ 您是哪国人？", "欢迎<s你>。<s你>是谁? <s你>是哪国人？"),
        ( "王tàitai，请进。请不客气。", "王<p太太>，请进。请不客气。"),
        ( "这是马xiānsheng的书。他是汉语老师。", "这是马<p先生>的书。他是汉语老师。"),
        ( "大夫都很忙。我很不忙。","大夫都很?忙。我很?不忙。"),
        ( "这是谁的地图？这是我朋友的地图。", "这是谁的地图？这是我朋友的地图。"),
        ("你好，老师王。你好。欢迎，进请。", "<s你>好，王老师。<s你>好。欢迎，请进。"),
        ("你好？我很好。", "<s你>好吗？我很?好。"),
        ("请进。您喝茶？", "请进。<s你>喝茶吗？"),
        ("这中国的茶。中国的茶很好。","这是中国茶。中国茶很?好喝?。"),
        ("喝茶。你喝哪píjiǔ？我喝中国píjiǔ。déguó píjiǔ是很好。", "请喝<p啤酒>。<s你>喝什么<p啤酒>？我喝<p德国><p啤酒>。<p德国><p啤酒>很?好喝?。"),
        ("吸烟请。我不吸。", "请吸烟。我不吸烟。"),
        ("你喝kāfēi？谢谢。请。", "<s你>喝<p咖啡>吗？谢谢。不客气。"),
        ("你喝什么？我喝茶。谢谢。", "<s你>喝什么？我喝茶。谢谢。"),
        ("中国人喝茶。éluósī也喝茶。", "中国人喝茶，<p俄罗斯>人也喝茶。<p俄罗斯>人也喝<p咖啡>。"),
        ( "你是中国人。中国人不喝niúnǎi。", "他是中国人。中国人不喝<p牛奶>。"),
        ( "欢迎你。你是什么？你是什么国人？", "欢迎<s你>。<s你>是谁? <s你>是哪国人？"),
        ( "tàitai王，请进。请不客气。", "王<p太太>，请进。请不客气。"),
        ( "这是书xiānsheng马。他是中国老师。", "这是马<p先生>的书。他是汉语老师。"),
        ( "都大夫很忙。她不忙。","大夫都很?忙。我很?不忙。"),
        ( "这是谁的地图吗？这是我的朋友的。", "这是谁的地图？这是我朋友的地图。"),
    )


    for case in _testcases:
        print(TranslationChecker.check_translation(*case))

if __name__ == "__main__":
    main()