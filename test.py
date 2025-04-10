from bearshell import BearShell

def test_bear_shell():
    # Create an instance of BearShell
    shell = BearShell(max_buffer_lines=100)

    # Add a command preset
    shell.add_preset("search_exploit", ["searchsploit", "{query}"])

    # Run the preset
    response = shell.run_preset("search_exploit", query="apache")
    print("Preset Response:", response.to_json())

    # Set allow-list and block-list
    shell.set_allow_list(["echo", "ls"])
    shell.set_block_list(["rm", "shutdown"])

    # Run a custom command
    response = shell.run("echo 'Hello World'")
    print("Echo Command Response:", response.to_json())

    # Run a command with blocked patterns
    response = shell.run("rm -rf /")
    print("Blocked Command Response:", response.to_json())


if __name__ == "__main__":
    test_bear_shell()
