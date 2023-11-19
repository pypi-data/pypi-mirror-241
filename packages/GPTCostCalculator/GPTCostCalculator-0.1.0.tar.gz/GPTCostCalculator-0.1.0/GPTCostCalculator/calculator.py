import tiktoken
import logging

class Calculator:
    """
    A class to estimate the cost of using different ChatGPT models based on the number of input and output tokens.

    Attributes:
        models (dict): A dictionary mapping model names to their respective input and output prices.
        tokenizers (dict): A cache for tokenizer instances for different models.
    """
    def __init__(self, max_cached_tokenizers=2):
        """
        Initializes the Calculator with supported models and their respective pricing.
        """
        self.models = {
            "gpt-4": {"input_price": 0.03, "output_price": 0.06},
            "gpt-4-32k": {"input_price": 0.06, "output_price": 0.12},
            "gpt-4-1106-preview": {"input_price": 0.01, "output_price": 0.03},
            "gpt-3.5-turbo-1106": {"input_price": 0.001, "output_price": 0.002},
            "gpt-3.5-turbo-instruct": {"input_price": 0.0015, "output_price": 0.002}
        }
        self.tokenizers = {}
        self.max_cached_tokenizers = max_cached_tokenizers
        logging.basicConfig(level=logging.INFO)

    def get_tokenizer(self, model: str):
        """
        Retrieves the tokenizer using tiktoken library for a given model, caching it if not already present.

        Args:
            model (str): The model name for which to get the tokenizer.

        Returns:
            The tokenizer instance for the specified model.

        Raises:
            ValueError: If the model is not supported.
        """

        if model not in self.tokenizers:
            try:
                if model not in self.models:
                    raise ValueError("Unsupported model.")
                self.tokenizers[model] = tiktoken.encoding_for_model(model)
                if len(self.tokenizers) > self.max_cached_tokenizers:
                    self.tokenizers.pop(next(iter(self.tokenizers)))
                logging.info(f"Tokenizer for {model} loaded.")
            except Exception as e:
                logging.error(f"Error loading tokenizer for {model}: {e}")
                raise
        return self.tokenizers[model]

    def cost_estimate(self, model: str, input_text: str, output_text: str = "") -> str:
        """
        Estimates the cost for a given input and output text using a specified GPT model.

        Args:
            model (str): The GPT model to use for estimation.
            input_text (str): The input text.
            output_text (str): The output text (optional).

        Returns:
            A string report detailing the estimated costs.

        Raises:
            ValueError: If the model is not supported.
        """
        if model not in self.models:
            raise ValueError("Unsupported model.")

        tokenizer = self.get_tokenizer(model)
        nombre_tokens_inputs = len(tokenizer.encode(input_text))
        nombre_tokens_outputs = len(tokenizer.encode(output_text))

        cout_input = nombre_tokens_inputs / 1000 * self.models[model]["input_price"]
        cout_output = nombre_tokens_outputs / 1000 * self.models[model]["output_price"]
        cout_total = cout_input + cout_output

        rapport = (f"Input cost: {cout_input}$ ({nombre_tokens_inputs} tokens). "
                   f"Output cost: {cout_output}$ ({nombre_tokens_outputs} tokens). "
                   f"Total cost: {cout_total:.3f}$ (rounded). "
                   "Please note that these costs are estimates and may vary depending on the actual response from OpenAi API.")

        if not output_text:
            rapport += (" Warning: No output example provided. "
                        "The actual cost could be higher due to the output tokens not included in this estimate.\n")

        return rapport