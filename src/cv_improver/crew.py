from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

@CrewBase
class CvImprover:
    def __init__(self, resume_path='./fake_resume.md'):
        # 初始化工具
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        self.read_resume = FileReadTool(file_path=resume_path)
        self.semantic_search_resume = MDXSearchTool(mdx=resume_path)

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            tools = [self.scrape_tool, self.search_tool],
            verbose=True
        )

    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler'], # type: ignore[index]
            tools = [self.scrape_tool, self.search_tool,
             self.read_resume, self.semantic_search_resume],
            verbose=True
        )
    
    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'], # type: ignore[index]
            tools = [self.scrape_tool, self.search_tool,
             self.read_resume, self.semantic_search_resume],
            verbose=True
        )
    
    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_preparer'], # type: ignore[index]
            tools = [self.scrape_tool, self.search_tool,
             self.read_resume, self.semantic_search_resume],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            async_execution=True,
        )

    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'], # type: ignore[index]
            async_execution=True,
        )

    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_strategy_task'],
            output_file="tailored_resume.md",
            context=[self.research_task(), self.profile_task()],
        )

    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task'],
            output_file='interview_materials.md',
            context=[self.research_task(), self.profile_task(), self.resume_strategy_task()],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the CvImprover crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )