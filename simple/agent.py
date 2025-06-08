# adk_client_agent.py
import asyncio
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset



root_agent = LlmAgent(
        name="GreetingAgent",
        model="gemini-2.0-flash",
        instruction="You are a helpful agent that can do basic arithmetic using the 'Calculator Demo' tool.",
        description="An agent that can do math",
        tools=[
            MCPToolset(
                connection_params=StreamableHTTPServerParams(
                    url="http://localhost:8080/mcp"
                ),
            ),
        ],
    )

