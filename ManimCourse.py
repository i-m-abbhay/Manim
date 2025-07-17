from manim import *

class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)
        self.play(Create(sq), run_time = 3)
        self.wait()


class Testing(Scene):
    def construct(self):
        name = Text("Abhay").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)
        
        self.play (Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play (Create(tri))
        self.wait()
        
        #now animating name etc existing shapes or elements
        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()