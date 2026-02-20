# core/config.py

class AgentConfig:
    QUICK_TIMEOUT = 30      # seconds
    DEEP_TIMEOUT = 180      # seconds

    MAX_RETRIES = 1
    MAX_QUERY_LENGTH_FOR_QUICK = 25

    ENABLE_COST_TRACKING = True