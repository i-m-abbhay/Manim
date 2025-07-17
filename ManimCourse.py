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


class Updaters(Scene):
    def construct(self):
        num = Text("ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=2
            )
        )
        name = always_redraw(lambda: Text("Abhay").next_to(box, DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 3), run_time=2)
        self.wait()


class ValueTrackers(Scene):
    def construct(self):
        # mobjects are the objects that are being animated
        # value trackers are the objects that are used to track the value of the mobjects
        k = ValueTracker(0)
        num = always_redraw(
            lambda: DecimalNumber().set_value(k.get_value()).to_edge(UP)
        )
        self.play(FadeIn(num))
        self.wait()
        self.play(
            k.animate.set_value(2), run_time=2, rate_func=linear
        )  # other possible params are linear, smooth, smooth, etc


class Graphing(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-4, 4, 1], x_length=7, y_range=[0, 16, 4], y_length=5)
            .to_edge(DOWN)
            .add_coordinates()
        )
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = plane.plot(lambda x: x**2, color=GREEN)
        func_label = (
            MathTex("f(x) = x^2")
            .scale(0.6)
            .next_to(parab, UR, buff=0.5)
            .set_color(GREEN)
        )

        area = plane.get_riemann_rectangles(
            parab,
            x_range=[-2, 2],
            dx=0.05,
            stroke_width=0.1,
            stroke_color=RED,
            fill_opacity=0.5,
        )
        area_label = (
            MathTex("\\sum_{i=1}^{n} f(x_i) \\Delta x")
            .scale(0.6)
            .next_to(area, UP, buff=0.5)
        )

        self.play(DrawBorderThenFill(plane))
        self.play(Create(parab), Create(labels))
        self.play(Write(func_label))
        self.play(Create(area), Write(area_label))
        self.wait()


class Graphing2(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-4, 4, 1], x_length=7, y_range=[0, 16, 4], y_length=5)
            .to_edge(DOWN)
            .add_coordinates()
        )
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = plane.plot(lambda x: x**2, color=GREEN)
