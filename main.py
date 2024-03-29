from manim import *
from code_style import DraculaCode, code_line, code_group


class ListComp(Scene):
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
                self.play(ShowCreationThenFadeOut(instantiate_highlight))
            self.play(*[TransformFromCopy(elms(start, pair[0]), elms(end, pair[1]))
                        if isinstance(pair, list) else Write(elms(end, pair)) for pair in entry])

    def draw_py_simple_decomp(self, simple_py_from=None, destruct=True):
        # Python list comprehension -> Simple Kotlin
        simple_py = code_line("counter = [", "i", "for i in", "range( 5 )", "]",
                              language="python")
        map_kotlin = code_line("val counter =", "(0..5)", ".map", "{", "it", "}", language="kotlin")
        if simple_py_from is None:
            self.play(Write(simple_py))
        else:
            self.play(ReplacementTransform(simple_py_from, simple_py))

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
        if destruct:
            self.play(Uncreate(map_kotlin),
                      Uncreate(map_kotlin_decomp))

    def draw_py_ktinit_decomp(self, destruct=True):
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
        if destruct:
            self.play(Uncreate(simple_kotlin),
                      Uncreate(simple_kotlin_decomp))

    def show_py_list_iteration(self):
        # Python list comprehension -> List
        simple_py = code_line("[", "i", "for", "i", "in", "range( 5 )", "]",
                              language="python")
        py_list = code_line("[", "0,", "1,", "2,", "3,", "4", "]", language="python")
        py_list.shift(DOWN)
        py_breakpoint = SurroundingRectangle(simple_py[3], buff=.1)

        self.play(Write(simple_py))
        self.play(TransformFromCopy(simple_py[0], py_list[0]),
                  TransformFromCopy(simple_py[-1], py_list[-1]))
        self.play(ShowCreation(py_breakpoint))
        for i in range(5):
            self.play(py_breakpoint.animate.move_to(simple_py[1]))
            self.play(TransformFromCopy(simple_py[1], py_list[1 + i]))
            self.play(py_breakpoint.animate.move_to(simple_py[3]))
        self.play(Uncreate(py_breakpoint))
        self.play(Uncreate(py_list))
        return simple_py

    def show_test_results(self):
        c_logo = SVGMobject(file_name="C-Logo.svg", stroke_width=5, stroke_opacity=.6, fill_opacity=.2, height=1)
        c_text = Text("4300ms")
        c_text_o = Text("1000ms")
        java_logo = SVGMobject(file_name="Java-Logo2.svg", stroke_width=0, fill_opacity=.4, height=1)
        java_text = Text("800ms")
        kotlin_logo = SVGMobject(file_name="Kotlin-logo.svg", stroke_width=5, stroke_opacity=.6, fill_opacity=.2, height=1)
        kotlin_text = Text("3500ms")

        c_code = DraculaCode(file_name="code/c_code.c", language="c")
        c_code_o = DraculaCode(file_name="code/c_code_o.c", language="c")
        simple_kotlin = code_line("val counter = IntArray(", "5", ") {", "it", "}",
                                  language="kotlin")
        simple_kotlin.shift(UP*2)
        map_kotlin = code_line("val counter =", "(0..5)", ".map", "{", "it", "}", language="kotlin")

        c_logo.set_y(0).set_x(-6)
        java_logo.set_y(1.5).set_x(-6)
        kotlin_logo.set_y(3).set_x(-6)

        # Kotlin
        self.play(ShowCreation(kotlin_logo))
        self.play(Write(map_kotlin))
        self.play(map_kotlin.animate.shift(2*UP),
                  Write(kotlin_text))
        self.play(Transform(map_kotlin, simple_kotlin),
                  Transform(kotlin_text, java_text))
        self.play(map_kotlin.animate.scale(0.3).move_to(kotlin_logo, aligned_edge=LEFT).shift(1.5*RIGHT).shift(.4*DOWN),
                  kotlin_text.animate.move_to(kotlin_logo, aligned_edge=LEFT).shift(1.5*RIGHT).shift(.2*UP))

        # Java
        self.play(ShowCreation(java_logo))
        java_text.move_to(java_logo, aligned_edge=LEFT).shift(1.3*RIGHT)
        self.play(TransformFromCopy(kotlin_text, java_text))

        # C
        self.play(ShowCreation(c_logo))
        c_code.shift(2*DOWN)
        c_code_o.shift(2*DOWN)
        self.play(Write(c_code))
        self.play(Write(c_text))
        self.play(Transform(c_code, c_code_o),
                  Transform(c_text, c_text_o))
        self.play(c_code.animate.scale(0.2).move_to(c_logo, aligned_edge=LEFT).shift(1.4*RIGHT).shift(.4*DOWN),
                  c_text.animate.move_to(c_logo, aligned_edge=LEFT).shift(1.4*RIGHT).shift(.2*UP))

        self.play(Uncreate(kotlin_logo), Uncreate(kotlin_text), Uncreate(map_kotlin),
                  Uncreate(java_logo), Uncreate(java_text),
                  Uncreate(c_logo), Uncreate(c_text), Uncreate(c_code))

    def construct(self):
        simple_py = self.show_py_list_iteration()
        self.draw_py_simple_decomp(simple_py)
        self.draw_py_ktinit_decomp()
        self.show_test_results()
