# GPT-Based Cover Letter Generator

`clgen` is a cover letter generator CLI based on GPT-4. It reduces the effort to create customized cover letters for job applications.

Setting up the application takes about two minutes, and saves you from the effort of interacting with ChatGPT manually.

# Installation

```bash
pip install clgen
```

# Usage

`clgen` requires the `OPENAI_API_KEY` environment variable to be set.

```bash
$ export OPENAI_API_KEY=sk-W...m
$ clgen --help

Usage: clgen [OPTIONS] COMMAND [ARGS]...

  Cover Letter Generator CLI.

Options:
  --help  Show this message and exit.

Commands:
  configure   Configure user profile.
  cv-add      Add a new CV.
  cv-delete   Delete an existing CV.
  cv-display  Display an existing CV.
  generate    Generate a cover letter.
```

### Configure

Adds information about yourself:

```bash
$ clgen configure
Enter your full name: John Doe
Enter your street: Doe Street
Enter your street number: 5
Enter your zip: 123456
Enter your city: Berlin
Enter your country: Germany
Configuration saved.
```

Rerun to update saved information.

### Manage CVs

#### Add CV

```bash
clgen cv-add
```

This command asks for a name to save the cv / resume as and open an interactive window to paste the plain text cv. Recommended to paste everything from job experience and skills, maybe exclude your contact information.

#### Display CVs

```bash
clgen cv-display
```

Lists list of saved CVs with option to print them.

#### Delete CV

```bash
clgen cv-delete
```

Deletes a saved CV.

## Generating Cover Letters

```bash
clgen generate --model gpt-3.5-turbo-1106
```

Generate takes an additional (optional) argument model, which should correspond to a model found [here](https://platform.openai.com/docs/models). Defaults to `gpt-4-1106-preview`.

Upon running the command, an interactive window opens to copy-paste the job description into. Next you are asked to provide the company name.

The CLI will then leverage the OpenAI API to generate a friendly cover letter focussing on your skills, explaining why you are a good match for the position. The result will be printed to the terminal.

Once the result is available, you can proceed in three ways:
`Choose an action (a / accept, e / edit, r / regenerate) (a, e, r):`

### Accept

Upon accepting, you can edit the output interactively before it is automatically saved to the `~/.clgen/letters` directory as markdown file. Congrats, go to get that job!

### Edit

If you are not satisfied with the result, you can choose to pass the existent generation with an additional prompt. An example prompt which works quite good is:

```text
Rewrite the letter with a stronger focus on me being a good match for the position and less focus on my past emplyoment history.
```

### Regenerate

If you are not satisfied with the result, you can regenerate the last input with a different temperature (aka. creativeness). Default tempeature is `0.7`, where a higher value (e.g. `1.5`) would create in more creative writing, be aware about hallucinations though.

# Disclaimer

## Costs

> By using this open source project, you agree to provide your own OpenAI API key to access the OpenAI services. You acknowledge that you will be solely responsible for any costs incurred by the use of your OpenAI API key in connection with this project. The usage of the OpenAI API through this project will be billed to your account with OpenAI according to their pricing policies.

> The author(s) of this project shall not be held liable for any charges, fees, costs, or expenses that you may incur as a result of your use of your OpenAI API key with this project. It is your responsibility to secure your API key and to ensure that any use of the key complies with OpenAI's terms and conditions. You should monitor your usage to prevent unexpected charges, as the author(s) provide no warranty or guarantee regarding the cost or billing of your use of the OpenAI API.

## Data Privacy

> When using this open source project, you may input information that will be processed by the OpenAI API. Please be aware that any data you provide may be shared with OpenAI and will be subject to OpenAI's privacy policy. The author(s) of this project do not have control over, and assume no responsibility for, the data privacy practices of OpenAI or any data handling once it has been transmitted to OpenAI's systems.

> You are responsible for ensuring that any data you input into the tool complies with data protection laws applicable to you and does not infringe upon the rights of any third parties. It is your duty to review OpenAI's privacy policy to understand how your data will be used and to ensure that you consent to this usage. By using your OpenAI API key in conjunction with this project, you acknowledge and agree to OpenAI's data processing practices as outlined in their privacy policy.
