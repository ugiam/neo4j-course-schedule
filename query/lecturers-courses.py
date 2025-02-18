from neo4j_query import neo4j_connect ,assign_course

URI = "neo4j://localhost"
AUTH = ("neo4j", "password")

session = neo4j_connect(URI,AUTH)

lecturers = [
            {1: ["Population Mathematics", "Difference Equation"]},
            {2: ["Research Methodology B", "Modeling and Simulation", "Introduction to Operational Research A"]},
            {3: ["Time Series Analysis"]},
            {4: ["Investment Model and Asset Management"]},
            {5: ["Discrete Mathematics B", "Real Analysis 2 A"]},
            {6: ["Algebra Structure 1 A"]},
            {7: ["Calculus 2 A", "Complex Function B"]},
            {8: ["Introduction to Operational Research B", "Forecasting Methods A"]},
            {9: ["Mathematical Logic B"]},
            {10: ["Special Function B", "Linear Algebra"]},
            {12: ["Mathematical Logic A", "Real Analysis 2 B"]},
            {13: ["Ordinary Differential Equations A", "Ordinary Differential Equations B"]},
            {14: ["Algebra Structure 1 B", "Combinatoric Analysis A"]},
            {15: ["Calculus 2 B", "Discrete Mathematics A"]},
            {17: ["Special Function A", "Multivariate Statistics"]},
            {18: ["Mathematics Statistics B"]},
            {19: ["Entrepreneurship A"]},
            {20: ["Research Methodology A", "Population Mathematics"]},
            {21: ["Non Linear Programming"]},
            {22: ["Special Function A"]},
            {23: ["Complex Function A", "Survival Model"]},
            {24: ["Mathematics Statistics A", "Forecasting Methods B"]},
            {25: ["Geometry A", "Fractal Geometry", "Complex Function B"]},
            {26: ["Geometry B", "Entrepreneurship B"]},
            {27: ["Discrete Mathematics B", "Combinatoric Analysis B", "Fractal Geometry"]},
            {28: ["Statistics Method A"]},
            {29: ["Statistics Method B"]},
            {30: ["Programming and Algorithm A", "Programming and Algorithm B"]},
            {31: ["Database A"]},
            {32: ["Database B"]},
            {34: ["Introduction to Operational Research B"]},
            ]

for lecturer in lecturers:
    for code in lecturer:
        for course in lecturer[code]:
            assign_course(code, course, session)