import cli

# Function to execute the command and process the output
def show_alias_output(alias):
    # Build the command
    command = f"show run | include {alias}"
    
    # Execute the command
    output = cli.execute(command)
    
    # Replace semicolons with newlines
    processed_output = output.replace(';', '\n')
    
    # Print the processed output
    print(processed_output)

# Replace 'your_alias_here' with your actual alias
show_alias_output('your_alias_here')
