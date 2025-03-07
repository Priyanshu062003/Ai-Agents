from agents import planner, writer, editor
from tasks import plan, write, edit
from crewai import Crew

crew = Crew(
    agents = [planner, writer],
    tasks = [plan, write],
    verbose = True
)

result = crew.kickoff(inputs={"topic":"Artificial Intelligence"})
print(result)

