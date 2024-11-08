def parse_input(user_input):
    cmd, *args = user_input.lower().split()
    cmd = cmd.strip().lower()
    return cmd, *args
