import os
import re
import subprocess
from autogen import AssistantAgent, UserProxyAgent

def InitAI(entireCode, projectPath):
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
            "temperature": 0,
        },
        system_message=f"YOU ARE A CODING ASSITENT HELPING WITH CREATING TESTS FOR C#. IF ANYTHING REQURIES TO BE MOCKED YOU HAVE THE NSUBSTITUDE PACKAGE AVAIBLE FOR MOCKING PORPUSES. A XUNIT PROJECT HAS BEEN MADE FOR YOU, YOU JUST HAVE TO CREATE XUNIT CS FILE WITH YOUR TEST IN IT USE THE NAMESPACE {os.path.basename(projectPath)}. DONT INCLUDE MUTIPLE CODE BLOCKS IN ONE RESPONSE. WHEN EVERYTHING IS DONE AND THE RESULT IS CORRECT REPLY WITH 'TERMINATE'",
    )

    userProxy = UserProxyAgent(
        name="proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg="",
        code_execution_config={"work_dir": "code", "use_docker": False},
    )

    def execute_csharp_code(csharp_code):
        file_path = os.path.join(os.path.dirname(projectPath), "TestingUnit.cs")
        with open(file_path, "w") as file:
            file.write(csharp_code)

        # Compile and run the code
        compile_process = subprocess.run(["dotnet", "build", projectPath], capture_output=True)
        if compile_process.returncode != 0:
            return f"Compilation error: {compile_process.stderr.decode()}"

        run_process = subprocess.run(["dotnet", "test", projectPath], capture_output=True)
        return run_process.stdout.decode()
            
        
    def csharp_execution_hook(message):
        match = re.search(r'```csharp\n(.*?)```', message[1]['content'], re.DOTALL)
        if match:
            print("C# Detected custom c# executiong")
            result = execute_csharp_code(match.group(1).strip())
            print(f"C# Execution Result:\n{result}")
            return result

    userProxy.register_hook("process_all_messages_before_reply", csharp_execution_hook)

    userProxy.initiate_chat(
        assistant,
        message=entireCode,
        summary_method="reflection_with_llm",
    )