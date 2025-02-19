MEMORY_FILE_PATH = 'data/memory.txt'  # Define the path to memory.txt

class MemoryService():
    def __init__(self):
        with open(MEMORY_FILE_PATH, 'r') as file:
            self.memory = file.read()  # Initialize memory variable

    def set_assistant(self, assistant):
        self.assistant = assistant  # Store the Assistant instance

    def update_memory(self, new_memory):
        self.memory = new_memory  # Update the memory variable
        with open(MEMORY_FILE_PATH, 'w') as file:
            file.write(new_memory)  # Write the new memory to the file
        self.assistant.update_memory(self.memory)
        return "Memory updated"

    def append_string_to_memory(self, string_to_append):
        string_to_append = "\n" + string_to_append
        self.memory += string_to_append  # Append the string to the memory variable
        with open(MEMORY_FILE_PATH, 'a') as file:  # Open the file in append mode
            file.write(string_to_append)  # Append the string to the file
        self.assistant.update_memory(self.memory)
        return f"Updated memory with: {string_to_append}"

    def get_memory(self):
        return self.memory  # Return the stored memory