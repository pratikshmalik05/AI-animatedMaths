from manim import *
import numpy as np

# Configuration for 1080p 60fps 16:9 Landscape
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class SpanBasisDimensionFull(Scene):

    
    def play_narrated_section(self, scene_function, audio_file, duration):
        start_time = self.time

    # Start narration at the beginning of this section
        self.add_sound(f"audio/{audio_file}")

    # Run the existing animation
        scene_function()

    # Calculate how much animation time has passed
        elapsed = self.time - start_time
        remaining = duration - elapsed

        if remaining > 0:
            self.wait(remaining)
        else:
            print(
                f"WARNING: {audio_file} exceeds its allocated "
                f"duration by {-remaining:.2f} seconds"
            )


    
    def construct(self):
        self.play_narrated_section(
            self.opening_frame, "opening.mp3", 18.984
        )

        self.play_narrated_section(
            self.scene_1_hook, "scene1.mp3", 31.632
        )

        self.play_narrated_section(
            self.scene_2_definitions, "scene2.mp3", 50.352
        )

        self.play_narrated_section(
            self.scene_3_visual_intuition, "scene3.mp3", 58.824
        )

        self.play_narrated_section(
            self.scene_4_worked_example, "scene4.mp3", 68.496
        )

        self.play_narrated_section(
            self.scene_5_r3_and_standard_basis, "scene5.mp3", 76.344
        )

        self.play_narrated_section(
            self.scene_6_summary_and_credits,
            "conclusion.mp3",
            35.064
        )
    # ~30 sec
        # Total Runtime: ~4 minutes 50 seconds

    def clear_screen(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)

    # ---------------------------------------------------------
    # SCENE 0: MANDATORY OPENING FRAME (~12 sec)
    # ---------------------------------------------------------
    def opening_frame(self):
        title = Text("Span, Basis, and Dimension", font_size=56, weight=BOLD, color=BLUE_B)
        subtitle = Text("A Geometric & Algebraic Guide in Linear Algebra", font_size=30, color=GRAY_A)
        student_info = Text(
            "Student Name: Pratiksh malik   |   Student ID: E25B070592 \nCourse: Engineering Mathematics III (M3)",
            font_size=24,
            color=YELLOW_B,
            line_spacing=1.4
        )
        group = VGroup(title, subtitle, student_info).arrange(DOWN, buff=0.6)
        border = SurroundingRectangle(group, color=BLUE_D, buff=0.5, corner_radius=0.15)

        self.play(FadeIn(border), Write(title), run_time=2.0)
        self.play(FadeIn(subtitle, shift=UP * 0.2), FadeIn(student_info, shift=UP * 0.2), run_time=1.8)
        self.wait(7.0)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 1: HOOK & CONTEXT (~40 sec)
    # ---------------------------------------------------------
    def scene_1_hook(self):
        header = Text("1. The Rover Navigation Problem", font_size=36, color=BLUE_B).to_edge(UP, buff=0.4)
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 8, 1],
            x_length=10,
            y_length=6.5,
            background_line_style={"stroke_color": TEAL_E, "stroke_width": 1, "stroke_opacity": 0.4}
        ).shift(DOWN * 0.3)

        self.play(Write(header), Create(plane), run_time=2.0)
        self.wait(3.0)

        origin = plane.c2p(0, 0)
        v1_end = plane.c2p(2, 1)
        v2_end = plane.c2p(-1, 2)
        target_pt = plane.c2p(4, 7)

        v1_arrow = Arrow(origin, v1_end, buff=0, color=BLUE, stroke_width=5)
        v2_arrow = Arrow(origin, v2_end, buff=0, color=GREEN, stroke_width=5)

        v1_label = MathTex(r"\vec{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", color=BLUE, font_size=30).next_to(v1_arrow.get_end(), RIGHT, buff=0.15)
        v2_label = MathTex(r"\vec{v}_2 = \begin{bmatrix} -1 \\ 2 \end{bmatrix}", color=GREEN, font_size=30).next_to(v2_arrow.get_end(), LEFT, buff=0.15)

        rover = Dot(origin, color=WHITE, radius=0.1)
        target_dot = Dot(target_pt, color=RED, radius=0.12)
        target_ring = Circle(radius=0.25, color=RED).move_to(target_pt)
        target_label = MathTex(r"\text{Target } \vec{b} = \begin{bmatrix} 4 \\ 7 \end{bmatrix}", color=RED, font_size=30).next_to(target_ring, RIGHT, buff=0.2)

        self.play(FadeIn(rover), GrowArrow(v1_arrow), Write(v1_label), run_time=1.8)
        self.wait(2.5)
        self.play(GrowArrow(v2_arrow), Write(v2_label), run_time=1.8)
        self.wait(2.5)
        self.play(FadeIn(target_dot), Create(target_ring), Write(target_label), run_time=1.8)
        self.wait(3.5)

        # Show scaling & tip-to-tail movement
        step1 = Arrow(origin, plane.c2p(6, 3), buff=0, color=BLUE_C, stroke_width=4)
        step1_lbl = MathTex(r"3\vec{v}_1", color=BLUE_C, font_size=26).next_to(step1.get_center(), DOWN, buff=0.15)
        step2 = Arrow(plane.c2p(6, 3), target_pt, buff=0, color=GREEN_C, stroke_width=4)
        step2_lbl = MathTex(r"2\vec{v}_2", color=GREEN_C, font_size=26).next_to(step2.get_center(), RIGHT, buff=0.15)

        question_box = Text(
            "Which points can we reach, and what is the minimum set of thrusters needed?",
            font_size=26, color=YELLOW
        ).to_edge(DOWN, buff=0.35).add_background_rectangle(color=BLACK, opacity=0.85, buff=0.15)

        self.play(GrowArrow(step1), Write(step1_lbl), run_time=1.5)
        self.wait(1.5)
        self.play(GrowArrow(step2), Write(step2_lbl), run_time=1.5)
        self.wait(2.5)
        self.play(FadeIn(question_box), run_time=1.5)
        self.wait(3.432)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 2: CONCEPT INTRODUCTION & FORMAL DEFINITIONS (~45 sec)
    # ---------------------------------------------------------
    def scene_2_definitions(self):
        header = Text("2. Core Definitions & Notation", font_size=38, color=BLUE_B).to_edge(UP, buff=0.5)
        self.play(Write(header), run_time=1.5)
        self.wait(2.0)

        items = VGroup(
            VGroup(
                Text("1. Linear Combination:", font_size=28, weight=BOLD, color=YELLOW),
                MathTex(r"\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \dots + c_k\vec{v}_k \quad (c_i \in \mathbb{R})", font_size=32)
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("2. Span:", font_size=28, weight=BOLD, color=BLUE_C),
                MathTex(r"\text{Span}\{\vec{v}_1, \dots, \vec{v}_k\} = \text{Set of ALL possible linear combinations}", font_size=30)
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("3. Linear Independence:", font_size=28, weight=BOLD, color=ORANGE),
                MathTex(r"c_1\vec{v}_1 + \dots + c_k\vec{v}_k = \vec{0} \iff c_1 = \dots = c_k = 0", font_size=30)
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("4. Basis:", font_size=28, weight=BOLD, color=GREEN_C),
                Text("A linearly independent set that spans the entire space", font_size=26)
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                Text("5. Dimension:", font_size=28, weight=BOLD, color=RED_C),
                MathTex(r"\dim(V) = \text{Exact number of vectors in any basis for } V", font_size=30)
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(DOWN * 0.25)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=1.5)
            self.wait(6.0)

        self.wait(3.0)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 3: VISUAL INTUITION (~55 sec)
    # ---------------------------------------------------------
    def scene_3_visual_intuition(self):
        header = Text("3. Geometric Intuition: Independent vs. Dependent", font_size=34, color=BLUE_B).to_edge(UP, buff=0.4)
        self.play(Write(header), run_time=1.5)

        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            x_length=8.8,
            y_length=6.0,
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.3}
        ).shift(LEFT * 2.1 + DOWN * 0.2)

        span_area = Rectangle(width=8.8, height=6.0, fill_color=BLUE, fill_opacity=0.22, stroke_width=0).move_to(plane.get_center())

        origin = plane.c2p(0, 0)
        v1 = Arrow(origin, plane.c2p(2, 1), buff=0, color=BLUE, stroke_width=5)
        v2 = Arrow(origin, plane.c2p(-1, 2), buff=0, color=GREEN, stroke_width=5)

        # Sample reachable points appearing across the plane
        sample_coords = [(1, 3), (-3, 1), (4, -1), (-2, -3), (3, 3), (-4, 2), (2, -2)]
        sample_dots = VGroup(*[Dot(plane.c2p(x, y), color=YELLOW, radius=0.07) for x, y in sample_coords])

        status_panel = VGroup(
            Text("Case A: Independent", font_size=28, weight=BOLD, color=GREEN),
            MathTex(r"\vec{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} -1 \\ 2 \end{bmatrix}", font_size=28),
            Text("Non-parallel directions", font_size=23, color=GRAY_A),
            Text("Span = Entire 2D Plane", font_size=24, color=BLUE_B),
            MathTex(r"\dim(\text{Span}) = 2", font_size=30, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).to_edge(RIGHT, buff=0.5)

        self.play(Create(plane), GrowArrow(v1), GrowArrow(v2), run_time=2.0)
        self.wait(2.5)
        self.play(LaggedStartMap(FadeIn, sample_dots, lag_ratio=0.2), run_time=2.5)
        self.play(FadeIn(span_area), FadeIn(status_panel), run_time=1.8)
        self.wait(9.0)

        # Case B: Rotate v2 onto the line of v1 -> v2 becomes [3, 1.5]
        v2_collinear = Arrow(origin, plane.c2p(3, 1.5), buff=0, color=ORANGE, stroke_width=5)
        collapsed_line = Line(plane.c2p(-6, -3), plane.c2p(6, 3), color=ORANGE, stroke_width=6)

        status_panel_b = VGroup(
            Text("Case B: Dependent", font_size=28, weight=BOLD, color=ORANGE),
            MathTex(r"\vec{v}_2 = 1.5\,\vec{v}_1", font_size=30, color=ORANGE),
            Text("v2 adds no new direction", font_size=23, color=GRAY_A),
            Text("Span collapses to a 1D Line!", font_size=24, color=RED_B),
            MathTex(r"\dim(\text{Span}) = 1", font_size=30, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).to_edge(RIGHT, buff=0.5)

        self.play(FadeOut(sample_dots), run_time=1.0)
        self.play(
            Transform(v2, v2_collinear),
            ReplacementTransform(span_area, collapsed_line),
            ReplacementTransform(status_panel, status_panel_b),
            run_time=3.5
        )
        self.wait(11.0)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 4: WORKED EXAMPLE (~60 sec)
    # ---------------------------------------------------------
    def scene_4_worked_example(self):
        header = Text("4. Worked Example: Solving & Verifying Basis", font_size=34, color=BLUE_B).to_edge(UP, buff=0.4)
        self.play(Write(header), run_time=1.5)

        eq_setup = MathTex(
            r"c_1 \begin{bmatrix} 2 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 7 \end{bmatrix}",
            font_size=36
        ).next_to(header, DOWN, buff=0.35)

        step1_label = Text("Step 1: Augmented Matrix", font_size=25, color=YELLOW).shift(LEFT * 3.8 + UP * 0.7)
        mat1 = MathTex(
            r"\left[\begin{array}{cc|c} 2 & -1 & 4 \\ 1 & 2 & 7 \end{array}\right]",
            font_size=34
        ).next_to(step1_label, DOWN, buff=0.25)

        step2_label = Text("Step 2: Swap R1 and R2", font_size=25, color=YELLOW).shift(RIGHT * 3.2 + UP * 0.7)
        mat2 = MathTex(
            r"\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{cc|c} 1 & 2 & 7 \\ 2 & -1 & 4 \end{array}\right]",
            font_size=34
        ).next_to(step2_label, DOWN, buff=0.25)

        step3_label = Text("Step 3: Row Reduction (R2 - 2R1)", font_size=25, color=YELLOW).shift(LEFT * 3.5 + DOWN * 1.4)
        mat3 = MathTex(
            r"\xrightarrow{R_2 - 2R_1} \left[\begin{array}{cc|c} 1 & 2 & 7 \\ 0 & -5 & -10 \end{array}\right]",
            font_size=34
        ).next_to(step3_label, DOWN, buff=0.25)

        step4_label = Text("Step 4: Unique Coordinates", font_size=25, color=GREEN).shift(RIGHT * 3.2 + DOWN * 1.4)
        sol_tex = MathTex(
            r"-5c_2 = -10 \implies c_2 = 2 \\ c_1 + 2(2) = 7 \implies c_1 = 3",
            font_size=30, color=GREEN_B
        ).next_to(step4_label, DOWN, buff=0.25)

        pivot_note = Text(
            "2 Pivots in 2 Rows & 2 Columns  =>  Spans R² AND Linearly Independent  =>  Valid Basis!",
            font_size=23, color=BLUE_B
        ).to_edge(DOWN, buff=0.3).add_background_rectangle(color=BLACK, opacity=0.85, buff=0.12)

        self.play(Write(eq_setup), run_time=2.0)
        self.wait(4.0)
        self.play(FadeIn(step1_label), Write(mat1), run_time=1.8)
        self.wait(6.0)
        self.play(FadeIn(step2_label), Write(mat2), run_time=1.8)
        self.wait(6.0)
        self.play(FadeIn(step3_label), Write(mat3), run_time=1.8)
        self.wait(6.0)
        self.play(FadeIn(step4_label), Write(sol_tex), run_time=2.0)
        self.wait(6.0)
        self.play(FadeIn(pivot_note), run_time=1.5)
        self.wait(7.0)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 5: STANDARD VS NON-STANDARD BASIS & EXTENSION TO R^3 (~50 sec)
    # ---------------------------------------------------------
    def scene_5_r3_and_standard_basis(self):
        header = Text("5. Standard Basis, Redundancy & Dimension", font_size=34, color=BLUE_B).to_edge(UP, buff=0.4)
        self.play(Write(header), run_time=1.5)

        left_col = VGroup(
            Text("Many Bases, One Dimension", font_size=28, weight=BOLD, color=YELLOW),
            MathTex(r"\text{Standard Basis of } \mathbb{R}^2: \quad \mathcal{E} = \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\}", font_size=28),
            MathTex(r"\text{Our Rover Basis of } \mathbb{R}^2: \quad \mathcal{B} = \left\{ \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \begin{bmatrix} -1 \\ 2 \end{bmatrix} \right\}", font_size=28, color=GREEN_B),
            Text("Both have 2 vectors  =>  dim(R²) = 2", font_size=24, color=BLUE_C),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(LEFT * 3.1 + UP * 0.4)

        right_col = VGroup(
            Text("What about 3D Space (R³)?", font_size=28, weight=BOLD, color=ORANGE),
            MathTex(r"\text{Standard Basis: } \left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\}", font_size=28),
            Text("• 2 vectors span only a flat 2D plane.", font_size=23, color=GRAY_A),
            Text("• 3 independent vectors span all of R³.", font_size=23, color=GRAY_A),
            Text("• 4 vectors are always dependent.", font_size=23, color=RED_B),
            MathTex(r"\implies \dim(\mathbb{R}^3) = 3", font_size=32, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).shift(RIGHT * 3.3 + UP * 0.1)

        divider = Line(UP * 2.3, DOWN * 2.5, color=GRAY)

        bottom_rule = Text(
            "Golden Rule: In an n-dimensional space, EVERY basis contains exactly n vectors.",
            font_size=25, weight=BOLD, color=GREEN
        ).to_edge(DOWN, buff=0.45)

        self.play(FadeIn(left_col[0]), Write(left_col[1]), run_time=2.0)
        self.wait(6.0)
        self.play(Write(left_col[2]), FadeIn(left_col[3]), run_time=2.0)
        self.wait(6.0)
        self.play(Create(divider), FadeIn(right_col[0]), Write(right_col[1]), run_time=2.0)
        self.wait(6.0)
        self.play(FadeIn(right_col[2:]), run_time=2.5)
        self.wait(7.0)
        self.play(FadeIn(bottom_rule), run_time=1.5)
        self.wait(7.0)
        self.clear_screen()

    # ---------------------------------------------------------
    # SCENE 6: SUMMARY & CREDITS (~30 sec)
    # ---------------------------------------------------------
    def scene_6_summary_and_credits(self):
        header = Text("Key Takeaways", font_size=40, weight=BOLD, color=BLUE_B).to_edge(UP, buff=0.5)
        takeaways = VGroup(
            Text("1. Span: Every vector reachable via linear combinations.", font_size=28, color=WHITE),
            Text("2. Basis: A minimal, linearly independent spanning set.", font_size=28, color=WHITE),
            Text("3. Dimension: The exact count of vectors in any basis.", font_size=28, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(header, DOWN, buff=0.6)

        credits_box = VGroup(
            Text("References & Credits", font_size=26, weight=BOLD, color=YELLOW_B),
            Text("• Textbook: Strang, G. — Introduction to Linear Algebra (Chapter 2: Vector Spaces)", font_size=20, color=GRAY_B),
            Text("• Animation Engine: Manim Community Edition (Python)", font_size=20, color=GRAY_B),
            Text("• Audio: AI-generated voice-over; no background music.", font_size=20, color=GRAY_B),
            Text("• AI Disclosure: AI assisted with script structuring and Manim Python code.", font_size=20, color=GRAY_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_edge(DOWN, buff=0.5)

        self.play(Write(header), run_time=1.5)
        self.wait(2.0)
        for t in takeaways:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=1.5)
            self.wait(4.0)

        self.play(FadeIn(credits_box), run_time=1.8)
        self.wait(7.0)
        self.clear_screen()