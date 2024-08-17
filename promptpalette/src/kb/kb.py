import pkg_resources
import os


def load_md_files():
    kb_content = ""
    example_content = {}

    # kb_dir = pkg_resources.resource_filename("promptpalette.src.kb")
    kb_dir = pkg_resources.resource_filename("promptpalette", "src/kb")

    kb_path = os.path.join(kb_dir, "knowledgebase")

    for filename in os.listdir(kb_path):
        if filename.endswith(".md"):
            file_path = os.path.join(kb_path, filename)
            with open(file_path, 'r') as fp:
                content = fp.read()
            name = os.path.splitext(filename)[0]
            kb_content += f"""<prompt>\n\t<name>{name}</name>\n<content>\n{content}\n</content>\n</prompt>\n"""
    examples_path = os.path.join(kb_dir, "examples")
    for filename in os.listdir(examples_path):
        if filename.endswith(".md"):
            file_path = os.path.join(examples_path, filename)
            with open(file_path, 'r') as fp:
                content = fp.read()
            name = os.path.splitext(filename)[0]
            example_content[
                name] = f"""<prompt>\n<name>{name}</name>\n<example>{content}</example>\n</prompt>\n"""

    return kb_content, example_content


class PromptKnowledge:
    PromptKnowledge, PromptExamples = load_md_files()


if __name__ == "__main__":
    print(list(PromptKnowledge.PromptExamples.keys()))
