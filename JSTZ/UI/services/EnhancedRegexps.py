import re
import pyparsing as pp



class EnhancedRegexpPreprocessor:
    open_non_ascii_tag = "/d"
    close_non_ascii_tag = "d/"
    encoded_elements_pattern = re.compile(open_non_ascii_tag + "[0-9]+?" + close_non_ascii_tag)


    @classmethod
    def preprocess_string(cls, string: str):
        """Pyparsing не умеет нормально работать с юникодовыми символами.
        Для этого все символы не из таблицы ASCII нужно перевести в, собственно, ASCII.
        Этот метод заменяет все неподходящие символы на их ord-ы и оборачивает в теги, чотбы потом их можно было найти при помощи регулярок, например."""
        return ''.join([c if c.isascii() else cls.open_non_ascii_tag + str(ord(c)) + cls.close_non_ascii_tag for c in string ])


    @classmethod
    def decode_preprocessed_string(cls, string: str):
        """Эта функция возвращает на место иероглифы, преобразованные в ord-ы методом preprocess_string."""

        encoded_elements = cls.encoded_elements_pattern.findall(string)

        result = string
        for element in encoded_elements:
            decoded = chr(int(element.strip(cls.open_non_ascii_tag).strip(cls.close_non_ascii_tag)))

            result = result.replace(element, decoded)

        return result




class OrdinaryRegexBuilder:

    #  Грамматика для переменных
    valid_var_content_characters = pp.printables.replace(";", "")

    var_grammar = (
        pp.Suppress(pp.Literal("$")) +
        pp.Word(pp.alphanums) +
        pp.Suppress(pp.Literal("=")) +
        pp.Word(valid_var_content_characters) +
        pp.Suppress(pp.Literal(";"))
        )

    vars_grammar = (
        pp.Suppress(pp.Literal("<<")) +
        pp.Suppress(pp.Keyword("vars")) +
        pp.ZeroOrMore(var_grammar) +
        pp.Suppress(pp.Literal(">>"))
        )

    expr_body_grammar = pp.Word(pp.printables)

    expr_grammar = pp.Optional(vars_grammar) + expr_body_grammar

    def __init__(self, rules: dict):
        self.rules = rules

    def strip_rule_expr(self, expr: str, rule: str):
        return expr.strip(f"<{rule}").strip(">")

    def apply_rules(self, enhanced_regexp: str):
        """Применяет пользовательский дополнительный синтаксис к регулярному выражению."""
        result = enhanced_regexp
        for rule in self.rules:
            matches = re.findall(f"<{rule}.+?>", enhanced_regexp)
            for match in matches:
                rulefunc = self.rules[rule]
                result = result.replace(match, rulefunc(self.strip_rule_expr(  match, rule)))
        return result


    def get_ordinary_regexp(self, enhanced_regexp: str):
        """Преобразует регулярное выражение с дополнительным синтаксисом в обычное регулярное выражение."""
        preprocessed_result = EnhancedRegexpPreprocessor.preprocess_string(enhanced_regexp)

        parsed = self.expr_grammar.parseString(preprocessed_result)
        _vars, expr = parsed[:-1], parsed[-1]

        vars = {}
        for var, value in zip(_vars[::2], _vars[1::2]):
                vars["$" + var] = EnhancedRegexpPreprocessor.decode_preprocessed_string(value)

        expr = EnhancedRegexpPreprocessor.decode_preprocessed_string(expr)

        for var in vars:
            expr = expr.replace(var, vars[var])
        return self.apply_rules(expr)

