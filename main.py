from manim import *
from code_style import DraculaCode, code_line, code_group


def transform(self, start, end, highlight, mat):
    """
    :param highlight: element to highlight
    :param self: self
    :param start: start elm
    :param end:  end elm
    :param mat: [[[start, end] | end]]
    :return:
    """
    instantiate_highlight = SurroundingRectangle(start[highlight], buff=.1)
    self.play(ShowCreation(instantiate_highlight))
    self.play(Uncreate(instantiate_highlight))
    start.animate.shift(np.array([0, 2, 0])),
    for entry in mat:
        self.play(*[TransformFromCopy(start[pair[0]], end[pair[1]])
                    if pair is list else Write(end[pair]) for pair in entry])


class SquareToCircle(Scene):
    def construct(self):
        background = BackgroundRectangle(FullScreenRectangle(), fill_color="#282828")
        self.add(background)

        simple_py = code_line("counter = [", "i", "for i in range(", "5", ") ]",
                              language="python")
        simple_kotlin = code_line("val counter = IntArray(", "5", ") {", "it", "}",
                                  language="kotlin")
        # name
        instantiate_highlight = SurroundingRectangle(simple_py[0], buff=.1)
        self.play(Write(simple_py))
        self.play(ShowCreation(instantiate_highlight))
        self.play(Uncreate(instantiate_highlight))
        self.play(simple_py.animate.shift(np.array([0, 2, 0])),
                  TransformFromCopy(simple_py[4], simple_kotlin[2]),
                  TransformFromCopy(simple_py[0], simple_kotlin[0]))
        # range
        range_highlight = SurroundingRectangle(simple_py[3], buff=.1)
        self.play(ShowCreation(range_highlight))
        self.play(Uncreate(range_highlight))
        self.play(TransformFromCopy(simple_py[3], simple_kotlin[1]),
                  Write(simple_kotlin[4]))
        # index
        index_highlight = SurroundingRectangle(simple_py[1], buff=.1)
        self.play(ShowCreation(index_highlight))
        self.play(Uncreate(index_highlight))
        self.play(TransformFromCopy(simple_py[1], simple_kotlin[3]))

        self.play(Uncreate(simple_py))

        simple_kotlin_decomp = code_group(
            ["byte var1 =", "5;"],
            ["int[] var2 = new int[var1];"],
            ["for(int var3 = 0; var3 < var1;", "var2[var3] = var3++", ") { }"],
            language="java")

        # range
        range_highlight = SurroundingRectangle(simple_kotlin[1], buff=.1)
        self.play(ShowCreation(range_highlight))
        self.play(Uncreate(range_highlight))
        self.play(simple_kotlin.animate.shift(np.array([0, 2, 0])),
                  Write(simple_kotlin_decomp[0][0]),
                  TransformFromCopy(simple_kotlin[1], simple_kotlin_decomp[0][1]))
        # name
        instantiate_highlight = SurroundingRectangle(simple_kotlin[0], buff=.1)
        self.play(ShowCreation(instantiate_highlight))
        self.play(Uncreate(instantiate_highlight))
        self.play(TransformFromCopy(simple_kotlin[0], simple_kotlin_decomp[1][0]))
        # index
        index_highlight = SurroundingRectangle(simple_kotlin[3], buff=.1)
        self.play(ShowCreation(index_highlight))
        self.play(Uncreate(index_highlight))
        self.play(TransformFromCopy(simple_kotlin[3], simple_kotlin_decomp[2][0]),
                  TransformFromCopy(simple_kotlin[4], simple_kotlin_decomp[2][2]),
                  TransformFromCopy(simple_kotlin[4], simple_kotlin_decomp[2][1]))

        self.play(Uncreate(simple_kotlin),
                  Uncreate(simple_kotlin_decomp))

        # ------------------
        simple_py = code_line("counter = [", "i", "for i in", "range( 5 )", "]",
                              language="python")
        map_kotlin = code_line("val counter =", "(0..5)", ".map", "{", "it", "}", language="kotlin")

        self.play(Write(simple_py))

        # name
        instantiate_highlight = SurroundingRectangle(simple_py[0], buff=.1)
        self.play(ShowCreation(instantiate_highlight))
        self.play(Uncreate(instantiate_highlight))
        self.play(simple_py.animate.shift(np.array([0, 2, 0])),
                  TransformFromCopy(simple_py[0], map_kotlin[0]))
        # range
        range_highlight = SurroundingRectangle(simple_py[3], buff=.1)
        self.play(ShowCreation(range_highlight))
        self.play(Uncreate(range_highlight))
        self.play(TransformFromCopy(simple_py[3], map_kotlin[1]))
        # map
        range_highlight = SurroundingRectangle(simple_py[2], buff=.1)
        self.play(ShowCreation(range_highlight))
        self.play(Uncreate(range_highlight))
        self.play(TransformFromCopy(simple_py[2], map_kotlin[2]))
        # index
        index_highlight = SurroundingRectangle(simple_py[1], buff=.1)
        self.play(ShowCreation(index_highlight))
        self.play(Uncreate(index_highlight))
        self.play(TransformFromCopy(simple_py[1], map_kotlin[4]),
                  TransformFromCopy(simple_py[-1], map_kotlin[-1]),
                  Write(map_kotlin[3]))

        map_kotlin_decomp = code_group("Iterable $this$map$iv = (Iterable)(new IntRange(var1, 5));",
                                       "Collection destination$iv$iv = (Collection)(new ArrayList(CollectionsKt.collectionSizeOrDefault($this$map$iv, 10)));\n" +
                                       "Iterator var6 = $this$map$iv.iterator();",
                                       "while(var6.hasNext()) {\n" +
                                       "    int item$iv$iv = ((IntIterator)var6).nextInt();\n" +
                                       "    Integer var11 = item$iv$iv;\n" +
                                       "    destination$iv$iv.add(var11);\n" +
                                       "}",
                                       "List list = (List)destination$iv$iv;",
                                       language="java")

        # range
        instantiate_highlight = SurroundingRectangle(map_kotlin[1], buff=.1)
        self.play(ShowCreation(instantiate_highlight))
        self.play(Uncreate(instantiate_highlight))
        self.play(map_kotlin.animate.shift(np.array([0, 2, 0])),
                  TransformFromCopy(map_kotlin[1], map_kotlin_decomp[0]))
        # name
        range_highlight = SurroundingRectangle(map_kotlin[0], buff=.1)
        self.play(ShowCreation(range_highlight))
        self.play(Uncreate(range_highlight))
        self.play(TransformFromCopy(map_kotlin[0], map_kotlin_decomp[1]),
                  TransformFromCopy(map_kotlin[0], map_kotlin_decomp[3]))
        # index
        index_highlight = SurroundingRectangle(map_kotlin[4], buff=.1)
        self.play(ShowCreation(index_highlight))
        self.play(Uncreate(index_highlight))
        self.play(TransformFromCopy(map_kotlin[1], map_kotlin_decomp[2]))
