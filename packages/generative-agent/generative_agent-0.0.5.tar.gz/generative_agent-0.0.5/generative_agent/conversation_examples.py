import os

template_conv = """globals()['{character_type}_CONV_EX'] = \"\"\"{conversation}\"\"\""""
template_guard = """globals()['{character_type}_GUARD_EX'] = \"\"\"{guard}\"\"\"\n\n"""

root_folder = os.path.join(os.path.dirname(__file__), "characters")
for subdir, dirs, files in os.walk(root_folder):
    for dir_name in dirs:
        character_folder = os.path.join(root_folder, dir_name)
        character_type = dir_name.upper()
        conversation_examples = ""
        guard_examples = ""

        for file_name in os.listdir(character_folder):
            if file_name.endswith(".txt"):
                with open(os.path.join(character_folder, file_name), "r") as input_file:
                    if "conversation" in file_name:
                        conversation_examples += input_file.read() + "\n\n"
                    elif "guard" in file_name:
                        guard_examples += input_file.read() + "\n\n"
        exec(
            template_conv.format(
                character_type=character_type,
                conversation=conversation_examples.strip(),
            )
        )

        exec(
            template_guard.format(
                character_type=character_type,
                guard=guard_examples.strip(),
            )
        )
