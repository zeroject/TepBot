import sys
import os
import subprocess
from autogen import AssistantAgent, UserProxyAgent

def InitAI(entireCode):
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
        system_message="YOU ARE A CODING ASSITENT HELPING WITH CREATING TESTS FOR C#. IF ANYTHING REQURIES TO BE MOCKED USE NSUBSTITUDE FOR MOCKING PORPUSES. IF YOU WANT THE USER TO SAVE THE CODE IN A FILE BEFORE EXECUTING IT, PUT # filename: <filename> inside the code block as the first line. DONT INCLUDE MUTIPLE CODE BLOCKS IN ONE RESPONSE. WHEN EVERYTHING IS DONE AND THE RESULT IS CORRECT REPLY WITH 'TERMINATE'",
    )

    userProxy = UserProxyAgent(
        name="proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg="",
        code_execution_config={"work_dir": "code", "use_docker": False},
    )

    def execute_csharp_code(csharp_code):
        file_path = "Program.cs"
        with open(file_path, "w") as file:
            file.write(csharp_code)

        # Compile and run the code
        try:
            compile_process = subprocess.run(["csc", file_path], capture_output=True)
            if compile_process.returncode != 0:
                return f"Compilation error: {compile_process.stderr.decode()}"

            executable_path = "Program.exe"
            run_process = subprocess.run([executable_path], capture_output=True)
            return run_process.stdout.decode()
        finally:
            os.remove(file_path)
            if os.path.exists("Program.exe"):
                os.remove("Program.exe")
        
    def csharp_execution_hook(agent, message):
        """Intercepts messages containing C# code and executes them."""
        if message.startswith("# filename:"):
            print("C# Detected custom c# executiong")
            result = execute_csharp_code(message.split("\n", 1)[1])
            print(f"C# Execution Result:\n{result}")
            return result

    userProxy.register_hook("execute_csharp_code", csharp_execution_hook)

    userProxy.initiate_chat(
        assistant,
        message=entireCode,
        summary_method="reflection_with_llm",
    )