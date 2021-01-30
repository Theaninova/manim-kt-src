from abc import ABC

from manim import Code, WHITE, VGroup, RIGHT, DOWN, DR, DL, LEFT
from pygments.style import Style
from pygments.token import Keyword, Text, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Punctuation, Literal, Other, Token, Escape


class DraculaStyle(Style):
    """
    The IntelliJ Dracula Style
    """

    background_color = "#313335"
    default_style = ""

    styles = {
        Token:                         "#A9B7C6",
        Text:                          "#A9B7C6",
        Whitespace:                    "#A9B7C6",

        Comment:                       "#808080",
        Number:                        "#6897BB",
        Operator:                      "#A9B7C6",
        Operator.Word:                 "#CC7832",
        Generic:                       "#009999",
        Punctuation:                   "#A9B7C6",

        Escape:                        "#CC7832",
        Error:                         "#FF0000",

        Other:                         "#A9B7C6",
        Keyword:                       "#CC7832",
        Keyword.Constant:              "#CC7832",

        Keyword.Declaration:           "#CC7832",
        Keyword.Namespace:             "#CC7832",

        Keyword.Pseudo:                "#CC7832",
        Keyword.Reserved:              "#CC7832",

        Keyword.Type:                  "#CC7832",
        Name:                          "#A9B7C6",
        Name.Attribute:                "#A9B7C6",
        Name.Builtin:                  "#A9B7C6",
        Name.Builtin.Pseudo:           "bold #A9B7C6",
        Name.Class:                    "#A9B7C6",
        Name.Constant:                 "#A9B7C6",
        Name.Decorator:                "#A9B7C6",
        Name.Entity:                   "#A9B7C6",
        Name.Exception:                "#FF0000",
        Name.Function:                 "#FFC66D",
        Name.Function.Magic:           "#FFC66D",

        Name.Property:                 "#9876AA",
        Name.Label:                    "italic",
        Name.Namespace:                "#A9B7C6",
        Name.Other:                    "#A9B7C6",
        Name.Tag:                      "#A9B7C6",
        Name.Variable:                 "#A9B7C6",
        Name.Variable.Class:           "#9876AA",
        Name.Variable.Global:          "bold italic #9876AA",

        Name.Variable.Instance:        "#A9B7C6",
        Name.Variable.Magic:           "#A9B7C6",
        Literal:                       "#A9B7C6",
        Literal.Date:                  "#A9B7C6",
        String:                        "#6A8759",
        String.Affix:                  "#6A8759",
        String.Backtick:               "#6A8759",
        String.Char:                   "#6A8759",
        String.Delimiter:              "#6A8759",
        String.Doc:                    "#6A8759",

        String.Double:                 "border:#FF0000"
    }


def code_group(*args, language=None):
    out = VGroup(*[code_line(*text, language=language) for text in args])
    out.arrange(direction=DOWN, center=False)
    for elm in out:
        elm.align_to(out.get_left(), direction=LEFT)
    return out


def code_line(*args, language=None):
    out = VGroup(*[DraculaCode(text=text, language=language) for text in args])
    out.arrange(direction=RIGHT)
    return out


class DraculaCode(Code):
    def __init__(
            self,
            text=None,
            file_name=None,
            tab_width=4,
            line_spacing=2,
            scale_factor=0.5,
            font="Fira Code",
            stroke_width=0,
            margin=0.3,
            indentation_chars="    ",
            background=None,  # or window, None for no background
            background_stroke_width=1,
            background_stroke_color=WHITE,
            corner_radius=0.2,
            insert_line_no=False,
            line_no_from=1,
            line_no_buff=0.6,
            style=DraculaStyle,
            language=None,
            generate_html_file=False,
            **kwargs,):
        super().__init__(text,
                         file_name,
                         tab_width,
                         line_spacing,
                         scale_factor,
                         font,
                         stroke_width,
                         margin,
                         indentation_chars,
                         background,
                         background_stroke_width,
                         background_stroke_color,
                         corner_radius,
                         insert_line_no,
                         line_no_from,
                         line_no_buff,
                         style,
                         language,
                         generate_html_file,
                         **kwargs)
