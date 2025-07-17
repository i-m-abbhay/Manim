from manim import *


class Pith(Scene):
    def construct(self):
        sq = Square(
            side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75
        )
        self.play(Create(sq), run_time=3)
        self.wait()


class Testing(Scene):
    def construct(self):
        name = Text("Abhay").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait()

        # now animating name etc existing shapes or elements
        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()


class Errors(Scene):
    def construct(self):
        c = Circle(radius=2)
        self.play(Write(c))
        # spelling or indentation error try reading the error messages correctly
        # note kwargs means keyword arguments


class Library(Scene):
    def construct(self):
        ax = Axes()
        self.play(Create(ax), run_time=2)
        self.wait()


class Getters(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)

        # arrow = Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip()
        arrow = always_redraw(
            lambda: Line(
                start=rect.get_bottom(), end=circ.get_top(), buff=0.2
            ).add_tip()
        )
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(
            rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4
        )  # our arrow will not follow this movement cause arrow is already placed at a static place for arrow to be moving along with rect we need to use always_redraw method
