from manim import *
from code_style import DraculaCode, code_line, code_group


class SquareToCircle(Scene):
    def transform_code(self, start, end, mat, highlight=True):
        """
        Transforms a code block into another one to show the connections

        :param highlight: whether to perform highlighting
        :param self: self
        :param start: start elm
        :param end:  end elm
        :param mat: [[[start, end] | end]]
        :return:
        """
        def elms(item, coord):
            return item[coord[0]][coord[1]] if isinstance(coord, tuple) else item[coord]
        for entry in mat:
            if highlight:
                instantiate_highlight = SurroundingRectangle(elms(start, entry[0][0]), buff=.1)
                self.play(ShowCreation(instantiate_highlight))
                self.play(Uncreate(instantiate_highlight))
            self.play(*[TransformFromCopy(elms(start, pair[0]), elms(end, pair[1]))
                        if isinstance(pair, list) else Write(elms(end, pair)) for pair in entry])

    def draw_py_simple_decomp(self):
        # Python list comprehension -> Simple Kotlin
        simple_py = code_line("counter = [", "i", "for i in", "range( 5 )", "]",
                              language="python")
        map_kotlin = code_line("val counter =", "(0..5)", ".map", "{", "it", "}", language="kotlin")
        self.play(Write(simple_py))
        self.play(simple_py.animate.shift(np.array([0, 2, 0])))
        self.transform_code(simple_py, map_kotlin, [[[0, 0]],
                                                    [[3, 1]],
                                                    [[2, 2]],
                                                    [[1, 4], [-1, -1], 3]])

        map_kotlin_decomp = code_group(["Iterable $this$map$iv = (Iterable)(new IntRange(var1, 5));"],
                                       ["Collection destination$iv$iv = (Collection)...;\n" +
                                        "Iterator var6 = $this$map$iv.iterator();"],
                                       ["while(var6.hasNext()) {\n" +
                                        "    int item$iv$iv = ((IntIterator)var6).nextInt();\n" +
                                        "    Integer var11 = item$iv$iv;\n" +
                                        "    destination$iv$iv.add(var11);\n" +
                                        "}"],
                                       ["List list = (List)destination$iv$iv;"],
                                       language="java")
        # Simple Kotlin -> Decompiled
        self.play(Uncreate(simple_py))
        self.play(map_kotlin.animate.shift(np.array([0, 2, 0])))
        self.transform_code(map_kotlin, map_kotlin_decomp, [[[1, (0, 0)]],
                                                            [[0, (1, 0)], [0, (3, 0)]],
                                                            [[4, (2, 0)]]])
        self.play(Uncreate(map_kotlin),
                  Uncreate(map_kotlin_decomp))

    def draw_py_ktinit_decomp(self):
        # Python list comprehension -> Kotlin list initializer
        simple_py = code_line("counter = [", "i", "for i in range(", "5", ") ]",
                              language="python")
        simple_kotlin = code_line("val counter = IntArray(", "5", ") {", "it", "}",
                                  language="kotlin")
        self.play(Write(simple_py))
        self.play(simple_py.animate.shift(np.array([0, 2, 0])))
        self.transform_code(simple_py, simple_kotlin, [[[0, 0], [4, 2]],
                                                       [[3, 1], 4],
                                                       [[1, 3]]])
        self.play(Uncreate(simple_py))

        # Kotlin list initializer -> Decompiled
        simple_kotlin_decomp = code_group(
            ["byte var1 =", "5;"],
            ["int[] var2 = new int[var1];"],
            ["for(int var3 = 0; var3 < var1;", "var2[var3] = var3++", ") { }"],
            language="java")
        self.play(simple_kotlin.animate.shift(np.array([0, 2, 0])))
        self.transform_code(simple_kotlin, simple_kotlin_decomp, [[[1, (0, 1)], (0, 0)],
                                                                  [[0, (1, 0)]],
                                                                  [[3, (2, 0)], [4, (2, 2)], [4, (2, 1)]]])
        self.play(Uncreate(simple_kotlin),
                  Uncreate(simple_kotlin_decomp))

    def construct(self):
        background = BackgroundRectangle(FullScreenRectangle(), fill_color="#282828")
        self.add(background)

        self.draw_py_simple_decomp()
        self.draw_py_ktinit_decomp()
