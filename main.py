#!/usr/bin/env python


import os.path
import sys

from agentneo import AgentNeo, Tracer

agent_session = AgentNeo(
    email="EMAIL_ID", base_url="BASE_URL"
)

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

try:
    from core.cli.main import run_pythagora
except ImportError as err:
    pythagora_root = os.path.dirname(__file__)
    venv_path = os.path.join(pythagora_root, "venv")
    requirements_path = os.path.join(pythagora_root, "requirements.txt")
    if sys.prefix == sys.base_prefix:
        venv_python_path = os.path.join(
            venv_path, "scripts" if sys.platform == "win32" else "bin", "python"
        )
        print(
            f"Python environment for Pythagora is not set up: module `{err.name}` is missing.",
            file=sys.stderr,
        )
        print(
            f"Please create Python virtual environment: {sys.executable} -m venv {venv_path}",
            file=sys.stderr,
        )
        print(
            f"Then install the required dependencies with: {venv_python_path} -m pip install -r {requirements_path}",
            file=sys.stderr,
        )
    else:
        print(
            f"Python environment for Pythagora is not completely set up: module `{err.name}` is missing",
            file=sys.stderr,
        )
        print(
            f"Please run `{sys.executable} -m pip install -r {requirements_path}` to finish Python setup, and rerun Pythagora.",
            file=sys.stderr,
        )
    tracer.cleanup()
    sys.exit(255)

try:
    exit_code = run_pythagora()
finally:
    tracer.upload_console_llm_trace()
    tracer.cleanup()

sys.exit(exit_code)
