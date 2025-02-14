from actions import tools
from prompts import main_system_prompt

class Assistant():
    def __init__(self, openai_client, action_module):
        self.openai_client = openai_client
        self.history = [{"role": "system", "content":main_system_prompt}]
        self.action_module = action_module

    def generate_response(self, question):
        self.history.append({"role": "user", "content": question})

        completion = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.history,
            tools=tools,
            temperature=0.5
        )

        calls = completion.choices[0].message.tool_calls

        if calls:
            completion = self.execute_tool_calls(calls, completion)

        answer = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": answer})
        return answer
    

    def execute_tool_calls(self, calls, completion):
        self.history.append(completion.choices[0].message)

        for tool_call in calls:
            data = self.action_module.execute_action(tool_call)

            self.history.append({                               
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(data)
                    })
        
        new_completion = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.history,
            tools=tools,
        )

        return new_completion