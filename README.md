
# Test Creating Agent

This agent was made for a exam in Machine learning. its task is too create tests based on a project you give it. There is a test solution where some projects has been made for testing its capabilites. Remeber this is just a proof of concept it should not actually be used, you can see the tests it produced in TestingSolution/test.




## Dependencies
All Dependencies can for the project can be installed from the requirments.txt.¨
run the ```pip install -r requirements.txt``` command to automaticly install all the dependencies

You need to have Ollama installed on your pc https://ollama.com/ <- link to it. And then install the model llama3.2 or change the agent.py file where it specifies the model use.

```python
config_list = [
        {
            "model": "llama3.2",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama"
        }
    ]
```
## Deployment

After installing the dependencies navigate to the root folder and run

```bash
  python main.py
```
you will then be promped to paste in a solution file path.
after select your desired project to create test for, it will then beging to talk to the ai and the creation of your test will then begin.
