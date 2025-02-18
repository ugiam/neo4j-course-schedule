from neo4j import GraphDatabase

def neo4j_connect(URI, AUTH, database="neo4j"):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()

    session = driver.session(database=database)
    return session

def register_course(code:int, course_new:str, session):
    session.run(
                """
                MATCH (A:STUDENT {code: $code}), (B:COURSE {name: $course_new})
                MERGE (A)-[:TAKE]->(B)
                """, code = code, course_new = course_new
                )
    
    courses_taken = session.run(
                                """
                                MATCH (s:STUDENT)-[:TAKE]->(c:COURSE)
                                WHERE s.code = $code
                                WITH COLLECT(c) as courses_taken
                                RETURN courses_taken
                                """, code=code
                                ).data()[0]['courses_taken']

    if courses_taken:
        courses_taken = [course['name'] for course in courses_taken]
        for course in courses_taken:
            if course == course_new:
                continue
            session.run(
                        """
                        MATCH (A:COURSE {name: $course_a}), (B:COURSE {name: $course_b}), (C:STUDENT {code:$code})
                        MERGE (A)<-[:CONFLICT]-(B)
                        MERGE (A)-[:CONFLICT]->(B);
                        """, course_a = course_new, course_b = course, code = code
                        )
            conflict = session.run(
                        """
                        OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                        Q = (A)<-[F:CONFLICT]-(B)
                        RETURN C.student, F.student
                        """, course_a = course_new, course_b = course
                        ).data()[0]
            conflict_count_a = conflict['C.student']
            conflict_count_b = conflict['F.student']
            if not conflict_count_a and not conflict_count_b:
                session.run(
                            """
                            OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                            Q = (A)<-[F:CONFLICT]-(B)
                            SET C.student = 1, F.student = 1
                            """, course_a = course_new, course_b = course
                            )
            else:
                conflict_count_a += 1
                conflict_count_b += 1
                session.run(
                            """
                            OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                            Q = (A)<-[F:CONFLICT]-(B)
                            SET C.student = $conflict_count_a, F.student = $conflict_count_a
                            """, course_a = course_new, course_b = course, conflict_count_a = conflict_count_a, conflict_count_b = conflict_count_b
                            )

def assign_course(code:int ,course_new:str, session):
    session.run(
                """
                MATCH (A:LECTURER {code: $code}), (B:COURSE {name: $course_new})
                MERGE (A)-[:TEACH]->(B)
                """, code = code, course_new = course_new
                )
    courses_assigned = session.run(
                                    """
                                    MATCH (l:LECTURER)-[:TEACH]->(c:COURSE)
                                    WHERE l.code = $code
                                    WITH COLLECT(c) as courses_assigned
                                    RETURN courses_assigned
                                    """, code=code
                                    ).data()[0]['courses_assigned']
    if courses_assigned:
        courses_assigned = [course['name'] for course in courses_assigned]
        for course in courses_assigned:
            if course == course_new:
                continue
            session.run(
                        """
                        MATCH (A:COURSE {name: $course_a}), (B:COURSE {name: $course_b}), (C:LECTURER {code:$code})
                        MERGE (A)<-[:CONFLICT]-(B)
                        MERGE (A)-[:CONFLICT]->(B);
                        """, course_a = course_new, course_b = course, code = code
                        )
            conflict = session.run(
                                    """
                                    OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                                    Q = (A)<-[F:CONFLICT]-(B)
                                    RETURN C.lecturer, F.lecturer
                                    """, course_a = course_new, course_b = course
                                    ).data()[0]
            conflict_count_a = conflict['C.lecturer']
            conflict_count_b = conflict['F.lecturer']
            if not conflict_count_a and not conflict_count_b:
                session.run(
                            """
                            OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                            Q = (A)<-[F:CONFLICT]-(B)
                            SET C.lecturer = 1, F.lecturer = 1
                            """, course_a = course_new, course_b = course
                            )
            else:
                conflict_count_a += 1
                conflict_count_b += 1
                session.run(
                            """
                            OPTIONAL MATCH P = (A:COURSE {name: $course_a})-[C:CONFLICT]->(B:COURSE {name: $course_b}),
                            Q = (A)<-[F:CONFLICT]-(B)
                            SET C.lecturer = $conflict_count_a, F.lecturer = $conflict_count_a
                            """, course_a = course_new, course_b = course, conflict_count_a = conflict_count_a, conflict_count_b = conflict_count_b
                            )