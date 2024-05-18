#!/usr/bin/env python3

import openai
import os
import sys

# OpenAI API key from the system environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_readme(project_name):
    """
    Generate a README file for a project using the OpenAI API.
    """
    prompt = f"""
    Write a detailed README file for a project named "{project_name}".
    Include the following sections:
    Explain "{project_name}" in a few sentences.
    1. Project Description
    2. Installation Instructions
    3. Usage Instructions
    4. Contributing Guidelines
    5. License Information
    """

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return res.choices[0].message['content'].strip()


def main():
    """
    Main function to generate the README file for a project.
    """
    if len(sys.argv) == 1:
        print("Usage: Add the Project Name as an argument.")
        sys.exit(1)
    elif len(sys.argv) != 2:
        print("Usage: Add the Project Name as a single argument.")
        sys.exit(1)

    project_name = sys.argv[1]
    readme_content = generate_readme(project_name)

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    print("README.md file has been generated successfully!")


if __name__ == "__main__":
    main()
