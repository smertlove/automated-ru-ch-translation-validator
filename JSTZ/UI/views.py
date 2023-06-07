from django.shortcuts import render
from .src import Comporator
from .src import EnhancedRegexps as ER
from .src.UserRules import RULES
from .models import Lesson, ChineseRegexp
from .src.parse_file import parse_file
from .src.TranslationChecker import TranslationChecker
from pprint import pprint


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'UI/index.html', {"data": {"lessons":lessons, "verdicts":["Тут будут результаты проверки."]}})



def get_file(request):
    lessons = Lesson.objects.all()
    data = request.FILES["file-to-check"].read().decode("utf-8")
    data = parse_file(data.strip())

    lesson = int(request.POST["lesson"].split(")")[0])
    regexps = ChineseRegexp.objects.filter(lesson=lesson-7)

    verdicts = []

    template = "{}) {}"

    for number in data:
        regexp = regexps.get(number=number).regexp
        verdicts.append(template.format(number, TranslationChecker.check_translation(data[number], regexp)))
    pprint(verdicts)


    return render(request, "UI/index.html", {"data": {"lessons":lessons, "verdicts":verdicts}})



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
