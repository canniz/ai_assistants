from actions import tools
from prompts import main_system_prompt
import os

# I primi due messaggi sono riservati ai system prompt
# self.memory[0] = il system_prompt principale
# self.memory[1] ) il system_prompt della memoria, 
# aggiornato ogni volta che il modello pensa ci sia da aggiornarlo

class Assistant():
    def __init__(self, openai_client, action_module):
        self.openai_client = openai_client
        self.action_module = action_module
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')  # Default to gpt-4o-mini if not set
        self.history = [{"role": "system", "content": main_system_prompt},
                        {"role": "system", "content": f"Memoria permanente: {self.action_module.memory_service.get_permanent_memory()}"}]
        self.action_module.set_assistant(self)

    def generate_response(self, question):
        self.update_history({"role": "user", "content": question})

        completion = self.openai_client.chat.completions.create(
            model=self.model,
            messages=self.history,
            tools=tools,
            temperature=0.5
        )

        calls = completion.choices[0].message.tool_calls

        if calls:
            completion = self.execute_tool_calls(calls, completion)

        answer = completion.choices[0].message.content
        self.update_history({"role": "assistant", "content": answer})
        return answer
    

    def execute_tool_calls(self, calls, completion):
        self.update_history(completion.choices[0].message)

        for tool_call in calls:
            data = self.action_module.execute_action(tool_call)

            self.update_history({                               
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(data)
                    })
        
        new_completion = self.openai_client.chat.completions.create(
            model=self.model,
            messages=self.history,
            tools=tools,
        )

        return new_completion

    def update_history(self, new_message):
        self.history.append(new_message)
        # Ensure the history does not exceed 30 messages, keeping the first one
        if len(self.history) > 30:
            self.history = [self.history[0]] + self.history[1:30]

    def update_permanent_memory(self, new_memory):
        self.history[1] = {"role": "system", "content": f"Memoria permanente: {new_memory}"}