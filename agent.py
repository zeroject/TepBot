import os
import re
import subprocess
from autogen import AssistantAgent, UserProxyAgent

def InitAI(entireCode, projectPath, unitTestName, otherProjects):
    config_list = [
        {
            "model": "llama3.2",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama"
        }
    ]

    def execute_csharp_code(csharp_code):
        file_path = os.path.join(os.path.dirname(projectPath), unitTestName)
        with open(file_path, "w") as file:
            file.write(csharp_code)

        # Compile and run the code
        compile_process = subprocess.run(["dotnet", "build", projectPath], capture_output=True)
        if compile_process.returncode != 0:
            error_message = compile_process.stdout.decode()
            print(f"Compilation failed with error: {error_message}")
            return f"Compilation error:\n{error_message}"

        run_process = subprocess.run(["dotnet", "test", projectPath], capture_output=True)
        if run_process.returncode != 0:
            runtime_error = run_process.stdout.decode()
            print(f"Runtime error: {runtime_error}")
            return f"Runtime error:\n{runtime_error}"

        output = run_process.stdout.decode()
        print(f"C# Execution Output:\n{output}")
        return output
            
        
    def csharp_execution_hook(messages):
        try:
            match = re.search(r'```csharp\n(.*?)```', messages[-1]['content'], re.DOTALL)
            if match:
                print("C# code detected for custom execution")
                exe_result = execute_csharp_code(match.group(1).strip())
                format_result = {
                    "role": "function",
                    "name": "csharp_execution_hook",
                    "content": exe_result
                }
                messages.append(format_result)
                return messages
            messages.append({"role": "function", "name": "csharp_execution_hook", "content": "No code was found"})
            return messages
        except Exception as e:
            error_msg = f"Error during C# custom execution of code: {str(e)}"
            print(error_msg)
            messages.append({"role": "function", "name": "csharp_execution_hook", "content": error_msg})
            return messages
        
    extraMsg = "ADD THEESE PROJECTS AS 'USING projectName' IN THE TOP OF THE FILE, HERE ARE ALL OF THE PROJECTS YOU NEED TO ADD USING INFRONT OF"
    for project in otherProjects:
        extraMsg += project.split('\\')[0]

    assistant = AssistantAgent(
        name="assistant",
        llm_config={
            "config_list": config_list,
            "temperature": 0,
        },

        system_message="YOU ARE A CODING ASSITENT HELPING WITH CREATING TESTS FOR C#."+
                        "IF ANYTHING REQURIES TO BE MOCKED YOU HAVE THE MOQ PACKAGE AVAIBLE FOR MOCKING PORPUSES."+ 
                        f"A XUNIT PROJECT HAS BEEN MADE FOR YOU, YOU JUST HAVE TO CREATE XUNIT CS FILE WITH YOUR TEST IN IT USE THE NAMESPACE {os.path.basename(projectPath)}."+ 
                        "ALLWAYS INCLUDE THE ENTIRE CS FILE EVEN IF YOU JUST MADE A SMALL CHANGE TO IT."+
                        f"AND REMEBER THIS {extraMsg}."+ 
                        "IGNORE ALL WARNINGS GIVEN TOO YOU ONLY FOCUS ON ERRORS. "+
                        "DONT INCLUDE MUTIPLE CODE BLOCKS IN ONE RESPONSE. "+
                        "WHEN EVERYTHING IS DONE AND THE RESULT IS CORRECT REPLY WITH 'TERMINATE'",
    )

    userProxy = UserProxyAgent(
        name="proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={"work_dir": "code", "use_docker": False},
    )

    userProxy.register_hook("process_all_messages_before_reply", csharp_execution_hook)

    userProxy.initiate_chat(
        assistant,
        message=entireCode,
        summary_method="reflection_with_llm",
    )