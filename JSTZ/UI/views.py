from django.shortcuts import render
from .services import Comporator
from .services import EnhancedRegexps as ER
from .services.UserRules import RULES
# from .models import Lesson, ChineseRegexp
from .services.parse_file import StudentTranslationParser
from .services.TranslationChecker import TranslationChecker
from pprint import pprint
import pathlib


class RegexpsDatabase:
    
    regexp_dir_path = pathlib.Path(__file__).parent.resolve() / "regexps"
    lesson_paths = {c.name: c for c in regexp_dir_path.iterdir()}
    
    
    @classmethod
    def read(cls, lesson_name) -> str:
        with open(cls.lesson_paths[lesson_name], "r", encoding="utf-8") as file:
            return file.read()
        


def index(request):
    lessons = RegexpsDatabase.lesson_paths
    lesson_names = [l for l in lessons]
    return render(request, 'UI/index.html', { "data": { "lessons": lesson_names , "verdicts":["Тут будут результаты проверки."]}})



def get_file(request):
    lessons = RegexpsDatabase.lesson_paths
    lesson_names = [l for l in lessons]
    
    
    lesson = request.POST["lesson"]
    data = request.FILES["file-to-check"].read().decode("utf-8")
    data = StudentTranslationParser.parse(data)
    
    true_regexps = StudentTranslationParser.parse(RegexpsDatabase.read(lesson))
    verdicts = []

    template = "{}) {}"

    for number in data:
        verdicts.append(
            template.format(number,
                            TranslationChecker.check_translation(
                                data[number],
                                true_regexps[number])
                            )
            )
    pprint(verdicts)


    return render(request, "UI/index.html", {"data": {"lessons":lesson_names, "verdicts":verdicts}})



def constructor(request):
    return render(request, 'UI/constructor.html', {"data":{"regex": ["Тут появится результат Ваших стараний!"], "variants":[]}})



def get_regex(request):

    vars = request.POST["vars"].replace("\n", ' ').replace("\r", '')
    regex = request.POST["regexp"].replace("\n", ' ').replace("\r", '')

    enhanced_regex = f"<<vars {vars} >>{regex}"

    regex = ER.OrdinaryRegexBuilder(RULES).get_ordinary_regexp(enhanced_regex)

    variants = Comporator.ChineseRegexpComporator.get_all_variants(regex)
    variants = [f"{i}) {c}" for i, c in enumerate(variants, start=1)]

    return render(request, 'UI/constructor.html', {"data":{"ordinary_regex": [regex], "enhanced_regex":[enhanced_regex], "variants":variants}})
