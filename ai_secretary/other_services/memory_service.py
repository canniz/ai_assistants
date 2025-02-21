TEMPORARY_MEMORY_FILE_PATH = 'data/temporary_memory.txt'  # Define the path to memory.txt
PERMANENT_MEMORY_FILE_PATH = 'data/permanent_memory.txt'  # Define the path to memory.txt

class MemoryService():
    def __init__(self):
        with open(TEMPORARY_MEMORY_FILE_PATH, 'r') as file:
            self.short_memory = file.read()  # Initialize memory variable
        with open(PERMANENT_MEMORY_FILE_PATH, 'r') as file:
            self.permanent_memory = file.read()  # Initialize memory variable

    def set_assistant(self, assistant):
        self.assistant = assistant  # Store the Assistant instance

    def delete_and_update_temporary_memory(self, new_memory):
        self.temporary_memory = new_memory  # Update the memory variable
        with open(TEMPORARY_MEMORY_FILE_PATH, 'w') as file:
            file.write(new_memory)  # Write the new memory to the file
        return "Memory updated"

    def append_string_to_permanent_memory(self, string_to_append):
        string_to_append = "\n" + string_to_append
        self.permanent_memory += string_to_append  # Append the string to the memory variable
        with open(PERMANENT_MEMORY_FILE_PATH, 'a') as file:  # Open the file in append mode
            file.write(string_to_append)  # Append the string to the file
        self.assistant.update_permanent_memory(self.permanent_memory)
        return f"Updated memory with: {string_to_append}"

    def get_temporary_memory(self):
        return self.short_memory  # Return the stored memory
    
    def get_permanent_memory(self):
        return self.permanent_memory  # Return the stored memory