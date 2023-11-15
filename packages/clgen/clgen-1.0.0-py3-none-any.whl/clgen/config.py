# config.py
from dotenv import load_dotenv, set_key
import click
import os

import datetime
from openai import OpenAI

# ? Store config files here
CONFIG_DIR = os.path.expanduser("~") + "/.clgen"

MODEL = ""  # Set by the user with cli arg

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def configure_profile():
    # Load existing .env file or create one if it doesn't exist
    load_dotenv(f"{CONFIG_DIR}/.env")

    # Check if a profile already exists
    if os.getenv("FULL_NAME"):
        if click.confirm("Profile already exists. Update?"):
            _ask_and_set_config()
        else:
            click.echo("Configuration unchanged.")
    else:
        _ask_and_set_config()


def _ask_and_set_config():
    # Ask for user input
    full_name = click.prompt("Enter your full name")
    street = click.prompt("Enter your street")
    street_number = click.prompt("Enter your street number")
    zip_code = click.prompt("Enter your zip")
    city = click.prompt("Enter your city")
    country = click.prompt("Enter your country")

    # Persist configuration
    set_key(f"{CONFIG_DIR}/.env", "FULL_NAME", full_name)
    set_key(f"{CONFIG_DIR}/.env", "STREET", street)
    set_key(f"{CONFIG_DIR}/.env", "STREET_NUMBER", street_number)
    set_key(f"{CONFIG_DIR}/.env", "ZIP", zip_code)
    set_key(f"{CONFIG_DIR}/.env", "CITY", city)
    set_key(f"{CONFIG_DIR}/.env", "COUNTRY", country)

    click.echo("Configuration saved.")


def add_cv():
    cv_name = click.prompt("Enter the name for the CV")
    cv_content = click.edit("Enter the CV content (multiline supported):")
    if cv_content:
        cv_path = f"{CONFIG_DIR}/cvs/{cv_name}.txt"
        with open(cv_path, "w") as cv_file:
            cv_file.write(cv_content)
        click.echo(f'CV "{cv_name}" saved.')


def delete_cv():
    cvs = _get_cv_list()
    if cvs:
        for idx, cv in enumerate(cvs, start=1):
            click.echo(f"{idx}. {cv}")
        cv_index = click.prompt("Enter the number of the CV to delete", type=int)
        if 0 < cv_index <= len(cvs):
            os.remove(f"{CONFIG_DIR}/cvs/{cvs[cv_index - 1]}")
            click.echo(f'CV "{cvs[cv_index - 1]}" deleted.')
        else:
            click.echo("Invalid CV number.")
    else:
        click.echo("No CVs found.")


def display_cv():
    cvs = _get_cv_list()
    if cvs:
        for idx, cv in enumerate(cvs, start=1):
            click.echo(f"{idx}. {cv}")
        cv_index = click.prompt("Enter the number of the CV to display", type=int)
        if 0 < cv_index <= len(cvs):
            cv_path = f"{CONFIG_DIR}/cvs/{cvs[cv_index - 1]}"
            with open(cv_path, "r") as cv_file:
                click.echo(cv_file.read())
        else:
            click.echo("Invalid CV number.")
    else:
        click.echo("No CVs found.")


def _get_cv_list():
    return [cv for cv in os.listdir(f"{CONFIG_DIR}/cvs") if cv.endswith(".txt")]


# ! OpenAI Logic


def generate_cover_letter(model: str):
    # Set model to use for generation
    global MODEL
    MODEL = model

    # Get user input
    job_description = click.edit("Enter the job description:")
    company_name = click.prompt("Enter the company name")
    cvs = _get_cv_list()
    if not cvs:
        click.echo("No CVs found. Please add a CV first.")
        return

    for idx, cv in enumerate(cvs, start=1):
        click.echo(f"{idx}. {cv}")
    cv_index = click.prompt("Choose a CV to use for generation", type=int)
    if 0 < cv_index <= len(cvs):
        cv_path = f"{CONFIG_DIR}/cvs/{cvs[cv_index - 1]}"
        with open(cv_path, "r") as cv_file:
            cv_content = cv_file.read()
    else:
        click.echo("Invalid CV number.")
        return

    prompt = f"""Generate a friendly cover letter for an application to the company {company_name} based on the following CV and job description:
"CV":
{cv_content}

"JOB DESCRIPTION":
{job_description}

Do not focus too much on the technical details of the cv and do not repeat it, but rather emphasize why the candidate is a good fit for the company and the position based on the skills, do not focus on experience too much.
Response only with the letter content text, not any headings or similar.
"""

    messages = [
        {
            "role": "system",
            "content": "You are a professional cover letter generator for job applications. Your task is to generate friendly and professional cover letters for job applications based on a given CV and job description.",
        },
        {"role": "user", "content": prompt},
    ]
    response = call_openai_api(messages=messages)
    handle_response(response, prompt, company_name, messages)


def call_openai_api(messages, temperature=0.7):
    response = client.chat.completions.create(
        messages=messages,
        model=MODEL,
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def handle_response(response, prompt, company_name, messages):
    print(response)
    action = click.prompt(
        "Choose an action (a / accept, e / edit, r / regenerate)",
        type=click.Choice(["a", "e", "r"], case_sensitive=False),
    )
    if action == "a":
        save_markdown(response, company_name)
    elif action == "e":
        user_prompt = click.prompt("Enter your prompt for editing")

        # ? Append previous response to message history
        messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        # ? Append new prompt to history
        messages.append(
            {
                "role": "user",
                "content": user_prompt,
            }
        )
        new_response = call_openai_api(messages=messages)
        handle_response(new_response, prompt, company_name, messages)
    elif action == "r":
        temperature = click.prompt("Enter a new temperature", type=float)
        new_response = call_openai_api(messages=messages, temperature=temperature)
        handle_response(new_response, prompt, company_name, messages)


def save_markdown(cover_letter, company_name):
    profile = load_profile_from_env()
    today = datetime.date.today().strftime("%Y-%m-%d")
    file_name = f"{today}-{company_name.replace(' ', '_')}"
    markdown_content = f"""
---
title: "Cover Letter for {company_name}"
author: "{profile['FULL_NAME']}"
date: "{today}"
---

# {profile['FULL_NAME']}
{profile['STREET']} {profile['STREET_NUMBER']}
{profile['ZIP']} {profile['CITY']}
{profile['COUNTRY']}

# {company_name}

{today}

{cover_letter}
"""
    md_file_path = f"{CONFIG_DIR}/letters/{file_name}.md"
    with open(md_file_path, "w") as md_file:
        md_file.write(markdown_content)

    click.edit(filename=md_file_path)

    # convert_markdown_to_pdf(md_file_path, f"{file_name}.pdf")


def load_profile_from_env():
    load_dotenv(f"{CONFIG_DIR}/.env")
    return {
        "FULL_NAME": os.getenv("FULL_NAME"),
        "STREET": os.getenv("STREET"),
        "STREET_NUMBER": os.getenv("STREET_NUMBER"),
        "ZIP": os.getenv("ZIP"),
        "CITY": os.getenv("CITY"),
        "COUNTRY": os.getenv("COUNTRY"),
    }


# Make sure the cvs and letter directory exists
os.makedirs(f"{CONFIG_DIR}/cvs", exist_ok=True)
os.makedirs(f"{CONFIG_DIR}/letters", exist_ok=True)
