from neo4j_query import neo4j_connect ,assign_course

URI = "neo4j://localhost"
AUTH = ("neo4j", "password")

session = neo4j_connect(URI,AUTH)

session.run("""
            CREATE
            (:COURSE{name: "Mathematical Logic A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Mathematical Logic B", status: "major", class: "b", semester: 2, credithour: 3}),
            (:COURSE{name: "Geometry A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Geometry B", status: "major", class: "b", semester: 2, credithour: 3}),
            (:COURSE{name: "Calculus 2 A", status: "major", class: "a", semester: 2, credithour: 4}),
            (:COURSE{name: "Calculus 2 B", status: "major", class: "b", semester: 2, credithour: 4}),
            (:COURSE{name: "Statistics Method A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Statistics Method B", status: "major", class: "b", semester: 2, credithour: 3}),
            (:COURSE{name: "Programming and Algorithm A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Programming and Algorithm B", status: "major", class: "b", semester: 2, credithour: 3}),
            (:COURSE{name: "Introduction to Operational Research A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Introduction to Operational Research B", status: "major", class: "b", semester: 2, credithour: 3}),
            (:COURSE{name: "Discrete Mathematics A", status: "major", class: "a", semester: 2, credithour: 3}),
            (:COURSE{name: "Discrete Mathematics B", status: "major", class: "b", semester: 2, credithour: 3}),

            (:COURSE{name: "Forecasting Methods A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Forecasting Methods B", status: "major", class: "b", semester: 4, credithour: 3}),
            (:COURSE{name: "Database A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Database B", status: "major", class: "b", semester: 4, credithour: 3}),
            (:COURSE{name: "Ordinary Differential Equations A", status: "major", class: "a",  semester: 4, credithour: 3}),
            (:COURSE{name: "Ordinary Differential Equations B", status: "major", class: "b",  semester: 4, credithour: 3}),
            (:COURSE{name: "Algebra Structure 1 A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Algebra Structure 1 B", status: "major", class: "b", semester: 4, credithour: 3}),
            (:COURSE{name: "Mathematics Statistics A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Mathematics Statistics B", status: "major", class: "b", semester: 4, credithour: 3}),
            (:COURSE{name: "Special Function A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Special Function B", status: "major", class: "b", semester: 4, credithour: 3}),
            (:COURSE{name: "Complex Function A", status: "major", class: "a", semester: 4, credithour: 3}),
            (:COURSE{name: "Complex Function B", status: "major", class: "b", semester: 4, credithour: 3}),

            (:COURSE{name: "Real Analysis 2 A", status: "major", class: "a", semester: 6, credithour: 3}),
            (:COURSE{name: "Real Analysis 2 B", status: "major", class: "b", semester: 6, credithour: 3}),
            (:COURSE{name: "Combinatoric Analysis A", status: "major", class: "a", semester: 6, credithour: 3}),
            (:COURSE{name: "Combinatoric Analysis B", status: "major", class: "b", semester: 6, credithour: 3}),
            (:COURSE{name: "Entrepreneurship A", status: "major", class: "a", semester: 6, credithour: 3}),
            (:COURSE{name: "Entrepreneurship B", status: "major", class: "b", semester: 6, credithour: 3}),
            (:COURSE{name: "Research Methodology A", status: "major", class: "a", semester: 6, credithour: 3}),
            (:COURSE{name: "Research Methodology B", status: "major", class: "b", semester: 6, credithour: 3}),
            (:COURSE{name: "Population Mathematics", status: "cross-major", class: "industrial", semester: 6, credithour: 3}),
            (:COURSE{name: "Modeling and Simulation", status: "cross-major", class: "industrial", semester: 6, credithour: 3}),
            (:COURSE{name: "Non Linear Programming", status: "cross-major", class: "industrial", semester: 6, credithour: 3}),
            (:COURSE{name: "Survival Model", status: "cross-major", class: "financial", semester: 6, credithour: 3}),
            (:COURSE{name: "Multivariate Statistics", status: "cross-major", class: "financial", semester: 6, credithour: 3}),
            (:COURSE{name: "Investment Model and Asset Management", status: "cross-major", class: "financial", semester: 6, credithour: 3}),
            (:COURSE{name: "Time Series Analysis", status: "cross-major", class: "financial", semester: 6, credithour: 3}),
            (:COURSE{name: "Difference Equation", status: "cross-major", class: "pure", semester: 6, credithour: 3}),
            (:COURSE{name: "Linear Algebra", status: "cross-major", class: "pure", semester: 6, credithour: 3}),
            (:COURSE{name: "Fractal Geometry", status: "cross-major", class: "pure", semester: 6, credithour: 3}),

            (:LECTURER{name: "Prof. Dr. Asep K Supriatna, MS", code:1}),
            (:LECTURER{name: "Prof. Dr. Sudradjat MS", code:2}),
            (:LECTURER{name: "Prof. Dr.Budi Nurani Ruchjana MS.", code:3}),
            (:LECTURER{name: "Dr. Sukono, MM., M.Si", code:4}),
            (:LECTURER{name: "Dr. Endang Rusyaman, MS", code:5}),
            (:LECTURER{name: "Dr. Ema Carnia M.Si.", code:6}),
            (:LECTURER{name: "Dra. Betty Subartini M.Si.", code:7}),
            (:LECTURER{name: "Drs. Eman Lesmana,MSIE", code:8}),
            (:LECTURER{name: "Dr. Sri Purwani Dra., M.Sc.", code:9}),
            (:LECTURER{name: "Edi Kurniadi, M.Si., Ph.D", code:10}),
            (:LECTURER{name: "Badrulfalah, M.Si.", code:12}),
            (:LECTURER{name: "Drs. Muhamad Deni Johansyah MM", code:13}),
            (:LECTURER{name: "Drs. Mochamad Suyudi M.Sc.", code:14}),
            (:LECTURER{name: "Dra. Kankan Parmikanti M.Stat.", code:15}),
            (:LECTURER{name: "Iin Irianingsih, M.Stat", code:17}),
            (:LECTURER{name: "Firdaniza M.Si.", code:18}),
            (:LECTURER{name: "Endang Soeryana H, Ph.D", code:19}),
            (:LECTURER{name: "Dr. Nursanti Anggriani S.Si.,M.Si.", code:20}),
            (:LECTURER{name: "Dr.Diah Chaerani S.Si., M.Si.", code:21}),
            (:LECTURER{name: "Dwi Susanti, Dra.,M.Si", code:22}),
            (:LECTURER{name: "Riaman S.Si., M.Si.", code:23}),
            (:LECTURER{name: "Nurul Gusriani, M.Si.", code:24}),
            (:LECTURER{name: "Alit Kartiwa S.Si., M.Si.", code:25}),
            (:LECTURER{name: "Dr. Dianne Amor Kusuma S.Pd., M.Pd.", code:26}),
            (:LECTURER{name: "Herlina Napitupulu, Ph.D", code:27}),
            (:LECTURER{name: "Dra. Titi Purwandari MS.", code:28}),
            (:LECTURER{name: "Dra. Neneng Sunengsih M.Stat.", code:29}),
            (:LECTURER{name: "Drs. Akik Hidayat M.Kom.", code:30}),
            (:LECTURER{name: "Dr. Intan Nurma Yulita, MT", code:31}),
            (:LECTURER{name: "Drs. R. Sudrajat M.Si.", code:32}),
            (:LECTURER{name: "Monika Hidayanti, MT", code:34}),

            (:STUDENT{name: "Russell Westbrook", code: 9540110170001}),
            (:STUDENT{name: "LeBron James", code: 9540110170002}),
            (:STUDENT{name: "Anthony Davis", code: 9540110170003}),
            (:STUDENT{name: "Ja Morant", code: 9540110160001}),
            (:STUDENT{name: "Luka Doncic", code: 9540110160002}),
            (:STUDENT{name: "Kevin Durant", code: 9540110160003}),
            (:STUDENT{name: "Kristaps Porzingis", code: 9540110150001}),
            (:STUDENT{name: "James Harden", code: 9540110150002}),
            (:STUDENT{name: "Giannis Antetokounmpo", code: 9540110150003}),
            (:STUDENT{name: "Khris Middleton", code: 9540110150004}),
            (:STUDENT{name: "Joel Embiid", code: 9540110150005}),
            (:STUDENT{name: "Tobias Harris", code: 9540110150006}),
            (:STUDENT{name: "Frank Vogel", code: 9540110150007}),
            (:STUDENT{name: "Robby Setiawan", code: 9540110150008}),
            (:STUDENT{name: "Shidqi Gozhi", code: 9540110150009}),
            (:STUDENT{name: "Owen Galendino", code: 9540110150010}),
            (:STUDENT{name: "Dafaa Azhar", code: 9540110150011}),
            (:STUDENT{name: "Ashmi Hablani", code: 9540110150012}),
            (:STUDENT{name: "Juratman", code: 9540110150013}),
            (:STUDENT{name: "Tommy Haryanto", code: 9540110150014});
            """
            )