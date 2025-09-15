from manim import *

class GeneratedSlide(Scene):
    def construct(self):
        title = Text("Derivative: Intuition")
        bullets = BulletedList("Rate of change", "Slope of tangent")
        self.play(Write(title))
        self.play(Write(bullets))
        self.wait(1)

