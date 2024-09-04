# 🧑‍✈️ GPT PILOT Evaluation by RagaAI AgentNeo🧑‍✈️

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oYBNowEBisOrZ-xdipbHvjy8dsla50jV?usp=sharing)

## Quick Start

To get started with the GPT PILOT evaluation using RagaAI AgentNeo, click the "Open in Colab" button above. This will open a Jupyter notebook in Google Colab where you can run the evaluation code and explore the results interactively.


## RagaAI AgentNeo Integration

We have integrated RagaAI AgentNeo for comprehensive tracing and monitoring of GPT Pilot. This integration provides valuable insights into the AI's decision-making process and performance. Here's how AgentNeo has been added:

1. **AgentNeo Session**: An AgentNeo session is initialized with the user's email and base URL.

2. **Tracer Setup**: A Tracer is configured to monitor LLM interactions and console output.

3. **Tool Metadata**: Various AI tools are defined with metadata, including:
   - codeMonkey: Writes and modifies code
   - commandLine: Executes and interprets command line operations
   - humanInterface: Interacts with users for information gathering
   - projectManager: Manages the development process flow
   - architect: Designs high-level application structure
   - productOwner: Defines product features and requirements
   - devOps: Handles deployment and operational tasks
   - techLead: Provides technical guidance and makes technology decisions

4. **Trace Uploading**: Console and LLM traces are uploaded for analysis.

5. **Cleanup**: Proper cleanup operations are performed at the end of the session.

This integration allows for detailed monitoring and analysis of GPT Pilot's performance, enabling better understanding and optimization of the AI-driven development process.

## Code for Tracing GPT Pilot

#### AgentNeo and Tracer Setup
```python
# Import required modules from agentneo
from agentneo import AgentNeo, Tracer
```

#### Initialize AgentNeo session
```py
# Replace EMAIL_ID with your actual email and BASE_URL with the appropriate URL
agent_session = AgentNeo(
    email="EMAIL_ID", base_url="BASE_URL"
)
```

#### Initialize Tracer
```py
# This sets up tracing for LLMs and console output, and defines metadata for various tools
tracer = Tracer.init(
    agent_session,
    trace_llms=True,
    trace_console=True,
    metadata={
        "tools": [
            {
                "name": "codeMonkey",
                "description": "Writes and modifies code based on instructions",
            },
            {
                "name": "commandLine",
                "description": "Executes command line operations and interprets their results",
            },
            {
                "name": "humanInterface",
                "description": "Interacts with the user to gather information or clarifications",
            },
            {
                "name": "projectManager",
                "description": "Manages the overall structure and flow of the development process",
            },
            {
                "name": "architect",
                "description": "Designs the high-level structure and components of the application",
            },
            {
                "name": "productOwner",
                "description": "Defines and prioritizes product features and requirements",
            },
            {
                "name": "devOps",
                "description": "Handles deployment, environment setup, and other operational tasks",
            },
            {
                "name": "techLead",
                "description": "Provides technical guidance and makes technology stack decisions",
            },
        ]
    },
)
```

#### Cleanup operations
```py 
# These should be called at the end of your script or in a finally block
tracer.upload_console_llm_trace()
tracer.cleanup()
```

**Note**: Once the trace upload is completed, the trace id is obtained, which is futher used to create Dataset for performing Evaluations. 

#### Project Creation
```py
from agentneo import Project

project_created = Project(session=agent_session, project_name="ProjectGPTPilot", description="A test project").create()
project_id = project_created['id']
```

#### Dataset Creation
```py
from agentneo import Dataset

# Create a dataset from a trace
dataset = Dataset(
    session=agent_session,
    project_id=project_id, 
    dataset_name="Dataset_GPTPilot", 
    description="A test dataset"
)

dataset_traced = dataset.from_trace(trace_id=1, trace_filter=None) # trace id is obtained after trace upload
```

#### Experiment Initialization
```py
from agentneo import Experiment

experiment = Experiment(
        session=agent_session,
        experiment_name="Experiment_GPTPilot1",
        description="A test experiment",
        dataset_id=dataset_traced['id'],
        project_id=dataset_traced['project_id']
    )

experiment_created = experiment.create()
```

#### Perform Evaluations
```py
# Execute Experiments
exp = experiment.execute(metrics=[
    {"name": "app_tool_selection_accuracy", "config": {"model": "gpt-4o-mini", "OPENAI_API_KEY": "OPENAI_API_KEY"}},
    {"name": "app_goal_decomposition_efficiency", "config": {"model": "gpt-4o-mini", "OPENAI_API_KEY": "OPENAI_API_KEY"}},
    {"name": "app_tool_usage_efficiency", "config": {"model": "gpt-4o-mini", "OPENAI_API_KEY": "OPENAI_API_KEY"}}
])
```

## Evaluations Performed

We conducted several evaluations using RagaAI AgentNeo to assess the performance of GPT Pilot. These evaluations provide insights into various aspects of the AI's capabilities:

1. **App Tool Selection Accuracy**
   This metric evaluates how accurately GPT Pilot selects the appropriate tools for specific tasks. It measures the AI's ability to choose the right tool from its toolkit based on the given context and requirements.

2. **App Goal Decomposition Efficiency**
   This evaluation assesses GPT Pilot's ability to break down complex goals into manageable sub-tasks. It measures how effectively the AI can analyze a project's objectives and create a structured plan of action.

3. **App Tool Usage Efficiency**
   This metric examines how efficiently GPT Pilot utilizes the selected tools. It evaluates whether the AI is using each tool to its full potential and in the most appropriate scenarios.

Each of these evaluations was performed using the GPT-4o-mini model and utilized the OpenAI API key for processing. The results of these evaluations provide valuable insights into GPT Pilot's decision-making processes and overall effectiveness in managing AI-driven development tasks.

## Evaluation Results Summary

The evaluations of GPT Pilot yielded promising results, with room for improvement:

1. **App Tool Selection Accuracy: 0.75**
   GPT Pilot demonstrated good judgment in selecting appropriate tools for most tasks. The use of 'Code Monkey' for coding and 'Tech Lead' for overseeing technical aspects was particularly effective. However, there's potential for improvement in choosing more specialized tools for specific tasks, such as dedicated testing tools.

2. **App Goal Decomposition Efficiency: 0.75**
   The AI showed a solid understanding of project goals and broke them down into logical, manageable sub-tasks. The decomposition was comprehensive and followed a clear structure. Areas for improvement include enhancing clarity for non-technical users, reducing redundancy in certain tasks, and ensuring all aspects of the goal are fully covered.

3. **App Tool Usage Efficiency: 0.68**
   GPT Pilot demonstrates effective use of its tools in most scenarios, but there's room for improvement. The AI could benefit from exploring a wider range of options to enhance efficiency, particularly in areas like testing and error handling. Leveraging more specialized tools for specific tasks and optimizing the sequence of tool usage could potentially boost overall performance and project outcomes.

GPT Pilot demonstrates strong capabilities in managing AI-driven development tasks, with consistent scores of 0.75 across evaluated metrics. These results indicate a good foundation with clear potential for further refinement and improvement in tool selection, goal decomposition, and tool usage efficiency.
