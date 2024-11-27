import sys
from autogen from AssistantAgent, UserProxyAgent

def InitAI():
    config_list = [
        {
            "model": "llama3.2",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama"
        }
    ]

    assistant = AssistantAgent(
        name="assistant",
        llm_config={
            "config_list": config_list,
            "seed": 42,
            "temperature": 0,
        },
        system_message="YOU ARE AN AI THAT HELPS DEVELOPERS WRITE TESTS FOR THEIR CODE WITH C# AND THE HELP OF NSubstitude for mocking",
    )

    userProxy = UserProxyAgent(
        name="proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg="",
        code_execution_config={"work_dir": "code", "use_docker": False},
    )

    userProxy.initiate_chat(
        assistant,
        message="""{}""",
        summary_method="reflection_with_llm",
    )