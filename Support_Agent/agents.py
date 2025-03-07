from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/deepseek-r1-distill-llama-70b",
    temperature=0.7
)

planner = Agent(
    role = "Content Planner",
    goal = "Plan engaging factually accurate content on: {topic} ",
    backstory=""" You're working on planning a blog article,
                  about the topic : {topic},
                  You Collect information That helps the audience learn somthing and make informed decisions.
                  Your word is the basis for the content Writer to write an article on this topic
                  the whole plan should be in 150 words
                  """,
    allow_delegation= False,
    llm = llm,
    verbose = True
)

writer = Agent(
    role = "Content Writer",
    goal = "Write insightful and factually accurate opinion peice about: {topic} ",
    llm = llm,
    backstory=""" You're working on Writing a new opinion peice about: {topic},
                  Your Base your writing on the work of the content Planner , who provides an outline and revelent context about the topic.
                  You Follow the main objective and direction of the outline, as provided by the content planner,
                  you also provide objective and impartial insights and back them up with information provided by the content planner.
                 you acknowledge inn your opinions when your statements are opinions as opposed to objective statements.
                 the whole content should be in 300 words
                  """,
    allow_delegation= False,
    verbose = True
)

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with "
         "the writing style of the organization. ",
    backstory="You are an editor who receives a blog post "
              "from the Content Writer. "
              "Your goal is to review the blog post "
              "to ensure that it follows journalistic best practices,"
              "provides balanced viewpoints "
              "when providing opinions or assertions, "
              "and also avoids major controversial topics "
              "or opinions when possible.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)


