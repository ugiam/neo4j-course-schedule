from neo4j_query import neo4j_connect ,register_course

URI = "neo4j://localhost"
AUTH = ("neo4j", "password")

session = neo4j_connect(URI,AUTH)

students = [
            #1st year
            {9540110170001: ["Mathematical Logic A", "Geometry A", "Calculus 2 A", "Statistics Method A", "Programming and Algorithm A", "Introduction to Operational Research A", "Discrete Mathematics A"]},
            {9540110170002: ["Mathematical Logic B", "Geometry B", "Calculus 2 B", "Statistics Method B", "Programming and Algorithm B", "Introduction to Operational Research B", "Discrete Mathematics B"]},
            {9540110170003: ["Mathematical Logic A", "Geometry A", "Calculus 2 A", "Statistics Method A", "Programming and Algorithm A", "Introduction to Operational Research A", "Discrete Mathematics A"]},
            #2nd year
            {9540110160001: ["Forecasting Methods A", "Database A", "Ordinary Differential Equations A", "Algebra Structure 1 A", "Mathematics Statistics A", "Special Function A", "Complex Function A", "Entrepreneurship A"]},
            {9540110160002: ["Forecasting Methods B", "Database B", "Ordinary Differential Equations B", "Algebra Structure 1 B", "Mathematics Statistics B", "Special Function B", "Complex Function B", "Entrepreneurship B"]},
            {9540110160003: ["Forecasting Methods A", "Database A", "Ordinary Differential Equations A", "Algebra Structure 1 A", "Mathematics Statistics A", "Special Function A", "Complex Function A"]},
            #3rd year
            ## pure
            {9540110150001 : ["Difference Equation", "Fractal Geometry", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A"]},
            {9540110150002 : ["Difference Equation", "Linear Algebra", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B", "Algebra Structure B"]},
            {9540110150009 : ["Difference Equation", "Linear Algebra", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A", "Algebra Structure A"]},
            {9540110150010 : ["Linear Algebra", "Fractal Geometry", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B"]},
            ## financial
            {9540110150003 : ["Time Series Analysis", "Investment Model and Asset Management", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A"]},
            {9540110150004 : ["Time Series Analysis", "Multivariate Statistics", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B"]},
            {9540110150014 : ["Time Series Analysis", "Investment Model and Asset Management", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B"]},
            {9540110150013 : ["Investment Model and Asset Management", "Multivariate Statistics", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A"]},
            ## industrial
            {9540110150006 : ["Modeling and Simulation", "Population Mathematics", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B"]},
            {9540110150007 : ["Modeling and Simulation", "Non Linear Programming", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A", "Algebra Structure A"]},
            {9540110150008 : ["Modeling and Simulation", "Survival Model", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B", "Algebra Structure B"]},
            {9540110150011 : ["Population Mathematics", "Survival Model", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A"]},
            {9540110150012 : ["Population Mathematics", "Non Linear Programming", "Real Analysis 2 B", "Combinatoric Analysis 2 B", "Entrepreneurship B", "Research Methodology B"]},
            {9540110150005 : ["Survival Model", "Non Linear Programming", "Real Analysis 2 A", "Combinatoric Analysis 2 A", "Entrepreneurship A", "Research Methodology A"]},
            ]

for student in students:
    for npm in student:
        for course in student[npm]:
            register_course(npm, course, session)