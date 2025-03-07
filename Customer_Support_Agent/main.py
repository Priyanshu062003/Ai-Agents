from crewai import Crew
from agent import support_quality_assurance_agent, support_agent
from task import inquiry_resolution, quality_assurance_review

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=False
  # memory=True
)

inputs = {
    "customer": "Vppcoe",
    "person": "Priyanshu Dubey",
    "inquiry": """I need help with setting up a Crew 
               and kicking it off, specifically 
               how can I use diffrent llm models  my crew Agents? 
               Can you provide guidance?"""
}
result = crew.kickoff(inputs=inputs)