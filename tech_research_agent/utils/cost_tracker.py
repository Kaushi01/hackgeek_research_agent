def estimate_cost(tokens, model="gpt-4o-mini"):
    # Basic mock pricing
    price_per_1k_tokens = 0.00015
    return (tokens / 1000) * price_per_1k_tokens