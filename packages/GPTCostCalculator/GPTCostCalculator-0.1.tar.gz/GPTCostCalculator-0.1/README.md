# GPT Cost Estimator

This Python package, `GPTCostCalculator`, provides a simple yet effective tool for estimating the cost of using different ChatGPT models. It is designed for anyone using ChatGPT models in their applications and need to estimate the cost of a particular query.
You do NOT need an OpenAI API key to use this package.

## Features

- Provides cost estimation for input and output tokens of various ChatGPT models.
- Supports multiple models including GPT-4, GPT-4-32k, GPT-4-1106-preview, GPT-3.5-turbo-1106, and GPT-3.5-turbo-instruct.
- Easy integration with existing Python projects.

## Supported Models

As of the current release, the package supports the following ChatGPT models:

- `gpt-4`: Input Price - $0.03, Output Price - $0.06 per 1000 tokens.
- `gpt-4-32k`: Input Price - $0.06, Output Price - $0.12 per 1000 tokens.
- `gpt-4-1106-preview`: Input Price - $0.01, Output Price - $0.03 per 1000 tokens.
- `gpt-3.5-turbo-1106`: Input Price - $0.001, Output Price - $0.002 per 1000 tokens.
- `gpt-3.5-turbo-instruct`: Input Price - $0.0015, Output Price - $0.002 per 1000 tokens.

## Installation

To install the package, simply run the following command:

```bash
pip install GPTCostCalculator
```

## Usage

Here is a basic example of how to use the package:

```python
from GPTCostCalculator import Calculator

# Initialize the calculator
calculator = Calculator()

# Estimate the cost
report = estimator.cost_estimate(model="gpt-4", input_text="Your input text here", output_text="Expected output text")
print(report)
```

`output_text` is not mandatory.

## Dependencies

- `tiktoken`: Used for tokenizing the input and output texts.

## Contributing

Contributions to the `GPTCostCalculator` package are welcome. Please feel free to fork the repository, make your changes, and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or feedback, please contact [Your Email](mailto:amato.gregoire@gmail.com).

## Disclaimer

Please note that the costs provided by this package are estimates and may vary based on actual usage of ChatGPT models.
