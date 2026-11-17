
import asyncio
import edge_tts
import os

VOICE = "en-IN-PrabhatNeural"
OUTPUT_DIR = "audio"

os.makedirs(OUTPUT_DIR, exist_ok=True)

narrations = {
    "opening": """
    Welcome to our presentation on Span, Basis, and Dimension
    in Linear Algebra. In this animation, we will understand
    these three important concepts through visual examples
    and mathematical reasoning.
    """,

    "scene1": """
    Imagine a rover exploring a two-dimensional surface.
    It has two thrusters, each pointing in a different direction.
    The first thruster moves it two units horizontally
    and one unit vertically. The second moves it one unit
    to the left and two units upward.
    By combining these movements, can we reach our target?
    This is the central idea behind the concept of span.
    """,

    "scene2": """
    Before solving the problem, let's understand five
    important definitions.

    First, a linear combination is created by multiplying
    vectors by scalars and adding the results.

    Second, the span is the set of all possible linear
    combinations of a given collection of vectors.

    Third, vectors are linearly independent when no vector
    can be expressed as a combination of the others.

    Fourth, a basis is a set of vectors that is both
    linearly independent and spans the entire space.

    Finally, dimension is the number of vectors
    in any basis of that space.
    """,

    "scene3": """
    Let's understand span geometrically.

    In the first case, our two vectors are not parallel.
    They point in different directions and are linearly
    independent.

    By combining these vectors with different scalar
    multiples, we can reach every point in the two-dimensional
    plane. Therefore, their span is the entire R two plane,
    and its dimension is two.

    Now consider the second case. The second vector becomes
    one point five times the first vector.

    Both vectors now point in the same direction.
    The second vector adds no new direction.

    As a result, the span collapses from the entire plane
    to a single straight line. Its dimension is now one.
    """,

    "scene4": """
    Now let's solve our rover navigation problem.

    We want to express the target vector, four comma seven,
    as a linear combination of our two given vectors.

    We introduce two unknown scalars, C one and C two.

    First, write the equations as an augmented matrix.

    Next, swap the first and second rows.

    Then subtract two times the first row from the second row.

    This gives us zero, minus five, and minus ten
    in the second row.

    Therefore, C two equals two.

    Substituting this into the first equation,
    we get C one equals three.

    So our target vector is three times the first vector
    plus two times the second vector.

    Since we have two pivots in two columns,
    the vectors are linearly independent and span R two.
    Therefore, they form a valid basis.
    """,

    "scene5": """
    We have already seen that a basis is not unique.

    The standard basis of R two contains the vectors
    one comma zero and zero comma one.

    Our rover basis contains two different vectors,
    but both sets have exactly two vectors.

    Therefore, the dimension of R two is two.

    Now let's extend this idea to three-dimensional space.

    The standard basis of R three contains three vectors:
    one comma zero comma zero;
    zero comma one comma zero;
    and zero comma zero comma one.

    Two independent vectors can span only a plane.
    Three independent vectors can span the entire
    three-dimensional space.

    Any collection of four vectors in R three
    must be linearly dependent.

    Therefore, the dimension of R three is three.

    Remember this golden rule:
    every basis of an n-dimensional vector space
    contains exactly n vectors.
    """,

    "conclusion": """
    Let's quickly summarize what we have learned.

    Span represents every vector reachable through
    linear combinations.

    A basis is a linearly independent spanning set.

    Dimension tells us the exact number of vectors
    in any basis of a vector space.

    These concepts help us understand the structure
    of vector spaces and solve problems in linear algebra.

    Thank you for watching our presentation.
    """
}


async def generate_audio():
    for name, text in narrations.items():
        output_file = os.path.join(OUTPUT_DIR, f"{name}.mp3")

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate="-5%",
            volume="+0%"
        )

        await communicate.save(output_file)
        print(f"Generated: {output_file}")


if __name__ == "__main__":
    asyncio.run(generate_audio())



