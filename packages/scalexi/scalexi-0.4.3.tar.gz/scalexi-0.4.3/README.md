# scalexi Python API  

_Simplifying LLM Development and Fine-Tuning with Python_


# Overview

[![PyPI version](https://img.shields.io/pypi/v/scalexi.svg)](https://pypi.org/project/scalexi/)

`scalexi` is a versatile open-source Python library, optimized for Python 3.11+, focuses on facilitating low-code development and fine-tuning of diverse Large Language Models (LLMs). It extends beyond its initial OpenAI models integration, offering a scalable framework for various LLMs.

Key to `scalexi` is its low-code approach, significantly reducing the complexity of dataset preparation and manipulation. It features advanced dataset conversion tools, adept at transforming raw contextual data into structured datasets fullfilling LLMs fine-tuning requirements. These tools support multiple question formats, like open-ended, closed-ended, yes-no, and reflective queries, streamlining the creation of customized datasets for LLM fine-tuning.

A standout feature is the library's automated dataset generation, which eases the workload involved in LLM training. `scalexi` also provides essential utilities for cost estimation and token counting, aiding in effective resource management throughout the fine-tuning process.

Developed by [scalexi.ai](https://scalexi.ai/), the library leverages a robust specification to facilitate fine-tuning context-specific models with OpenAI API. Alsom `scalexi` ensures a user-friendly experience while maintaining high performance and error handling.

Explore the full capabilities of Large Language Models with `scalexi`'s intuitive and efficient Python API with minimal coding for easy LLM development and fine-tuning from dataset creation to LLM evaluation.

## Documentation

For comprehensive guides, API references, and usage examples, visit the [`scalexi` Documentation](http://docs.scalexi.ai/). It provides an up-to-date information you need to effectively utilize the `scalexi` library for LLM development and fine-tuning.


## Features

- **Low-Code Interface**: `scalexi` offers a user-friendly, low-code platform that simplifies interactions with LLMs. Its intuitive design minimizes the need for extensive coding, making LLM development accessible to a broader range of users.

- **Automated Dataset Generation**: The library excels in converting raw data into structured formats, aligning with specific LLM fine-tuning requirements. This automation streamlines the dataset preparation process, saving time and reducing manual effort.

- **Versatile Dataset Format Support**: `scalexi` is designed to handle various dataset formats including CSV, JSON, and JSONL. It also facilitates effortless conversion between these formats, providing flexibility in dataset management and utilization.

- **Simplified Fine-Tuning Process**: The library provides simplified interfaces for fine-tuning LLMs. These user-friendly tools allow for easy customization and optimization of models on specific datasets, enhancing model performance and applicability.

- **Efficient Model Evaluation**: `scalexi` includes utilities for the automated evaluation of fine-tuned models. This feature assists in assessing model performance, ensuring the reliability and effectiveness of the fine-tuned models.

- **Token Usage Estimation**: The library incorporates functions to accurately estimate token usage and associated costs. This is crucial for managing resources and budgeting in LLM projects, providing users with a clear understanding of potential expenses.


## Installation

Easily install `scalexi` with pip. Just run the following command in your terminal:

```bash
pip install scalexi
```
This will install scalexi and its dependencies, making it ready for use with Python 3.11 and above (not tested on lower Python versions). 


## Usage
Here's a quick start on how to use `scalexi`:

```python
# Import necessary modules
import os
from scalexi.dataset_generation.prompt_completion import PromptCompletionGenerator
from scalexi.document_loaders.context_loaders import context_from_csv_as_df

# Set your OpenAI API key here
api_key = "your-openai-api-key"
os.environ["OPENAI_API_KEY"] = api_key

# Initialize the PromptCompletionGenerator
generator = PromptCompletionGenerator()

# Define the model to be used
model = "gpt-3.5-turbo"  # or "gpt-4"

# Specify the path to your context CSV file
context_filename = "path/to/your/context.csv"

# Define the output path for the generated dataset
generated_dataset_path = "path/to/generated_dataset.csv"

# Function to create a dataset with different types of questions
def create_dataset(context_path, num_questions=3):
    context_df = context_from_csv_as_df(context_path, encoding="utf-8")
    question_types = ["open-ended", "yes-no", "reflective", "multiple-choice", "closed-ended"]

    for index, row in context_df.iterrows():
        context = row['context']
        for question_type in question_types:
            output_filename = f"generated_{question_type}_dataset.csv"
            try:
                print(f"Generating {question_type} questions for context at index {index}")
                questions = generator.generate_prompt_completions(
                    context,
                    output_filename,
                    num_questions=num_questions,
                    question_type=question_type,
                    model=model,
                    detailed_explanation=True
                )
                print(f'Results for {question_type}:', questions)
            except Exception as e:
                print(f"Error: {e}")

# Create the dataset
create_dataset(context_filename)
```
# Initialize the package with your API key
scalexi.init(api_key="your-openai-api-key")

# Fine-tune a model
scalexi.fine_tune_model("model-name", "dataset.csv")

# Evaluate a model
score = scalexi.evaluate_model("model-name", "evaluation-dataset.csv")
print(f"Model Score: {score}")



# Contributing

We warmly welcome contributions to `scalexi`! Whether you're fixing bugs, adding new features, or improving documentation, your help is invaluable.

Before you start, please take a moment to review our contribution guidelines. They provide important instructions and best practices to follow, ensuring a smooth and efficient contribution process.

You can find all the necessary details in our [Contribution Guidelines](CONTRIBUTING.md). Thank you for your interest in enhancing `scalexi`!

# License

`scalexi` is released under the ScaleXI License 1.0. This license ensures that the software can be freely used, reproduced, and distributed, both for academic and business purposes, while requiring proper attribution to ScaleX Innovation company in any derivative works or distributions.

For full details of the terms and conditions, please refer to the [LICENSE](LICENSE) file included with the software.


# Contact
For support or queries, reach out to us at Anis Koubaa <akoubaa@scalexi.com>.

