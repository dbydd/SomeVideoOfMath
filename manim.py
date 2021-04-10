from math import sin
from manimlib import *


class scene1(Scene):
    def construct(self):
        axe = Axes(
            x_range=(-10, 10),
            y_range=(-5, 5),
        )

        axe.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )

        self.play(Write(axe, lag_ratio=0.01, run_time=1))

        sin_graph = axe.get_graph(
            lambda x: sin(x),
            color=BLUE
        )

        text = Tex("\\sin (x)")

        self.play(
            ShowCreation(sin_graph),
            FadeIn(text),
        )
        text.move_to(axe.c2p(8, 5))

        for i in range(2, 10):
            tempGraph = axe.get_graph(
                lambda x: sin(i * x),
                color=BLUE
            )
            tempText = Tex("\\sin (" + str(i) + "x)")
            tempText.shift(axe.c2p(8, 5))
            self.wait(2)
            self.play(
                ReplacementTransform(sin_graph, tempGraph),
                ReplacementTransform(text, tempText)
            )
            sin_graph = tempGraph
            text = tempText

        self.wait(2)

        self.clear()

        self.play(Write(axe, lag_ratio=0.01, run_time=1))

        sin_graph = axe.get_graph(
            lambda x: sin(x),
            color=BLUE
        )

        self.play(
            ShowCreation(sin_graph),
            FadeIn(text),
        )
        text.move_to(axe.c2p(8, 5))

        for i in range(2, 5):
            tempGraph = axe.get_graph(
                lambda x: i * sin(x),
                color=BLUE
            )
            tempText = Tex(str(i) + "\\sin (x)")
            tempText.shift(axe.c2p(8, 5))
            self.wait(2)
            self.play(
                ReplacementTransform(sin_graph, tempGraph),
                ReplacementTransform(text, tempText)
            )
            sin_graph = tempGraph
            text = tempText

        self.wait(2)
