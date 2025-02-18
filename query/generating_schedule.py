import pandas as pd
from neo4j_query import neo4j_connect
import sys

try:
    graph_name = sys.argv[1]
except:
    graph_name = ''

URI = "neo4j://localhost"
AUTH = ("neo4j", "password")

session = neo4j_connect(URI,AUTH)

if graph_name:
    session.run("""
            MATCH (source:COURSE)-[r:CONFLICT]->(target:COURSE)
            RETURN gds.graph.project(
            $graph_name,
            source,
            target,
            {},
            { maxIterations: 100 }
            )
            """, graph_name = graph_name)
    
data = session.run("""
                    CALL gds.k1coloring.stream('conflicted_course_1')
                    YIELD nodeId, color
                    RETURN gds.util.asNode(nodeId).name AS name, gds.util.asNode(nodeId).semester AS semester, gds.util.asNode(nodeId).credithour AS credithour,color
                    ORDER BY color, semester
                   """).data()

color_count = session.run("""
                            CALL gds.k1coloring.write('conflicted_course_1', {writeProperty: 'color'})
                            YIELD nodeCount, colorCount, ranIterations, didConverge 
                          """).data()[0]['colorCount']

schedule = {}
for i in range(color_count):
    schedule[f"Time Slot {i+1}"] = [course['name'] for course in data if i == course['color']]

max_color_node = max([(len(schedule[key])) for key in schedule])

df = pd.DataFrame.from_dict(schedule, orient='index', columns=[f"Room {i+1}" for i in range(max_color_node)]).transpose()
df.to_excel("Departement of Mathematics' Even Semester Schedule.xlsx")

