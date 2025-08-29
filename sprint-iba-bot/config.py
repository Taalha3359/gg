# Bot token from Discord Developer Portal
BOT_TOKEN = "MTQxMDkzMjQzNTcwODkzNjIwMg.G7XYxz.prl5D1eAUZWeOw-v5boxNC7VdEm_NMx-JC06vQ"

# Bot prefix for commands
BOT_PREFIX = "!"

# Time limits for questions (in seconds)
TIME_LIMITS = {
    "math": 90,           # 1.5 minutes
    "english": 45,        # 45 seconds
    "analytical": 60,     # 1 minute
    "puzzle": 300         # 5 minutes for puzzles
}

# Mock test settings
MOCK_TEST_CONFIG = {
    "math_count": 25,
    "english_count": 30,
    "analytical_count": 15,
    "time_limit": 3600  # 1 hour
}

# Scoring system
SCORING = {
    "correct": 1,
    "incorrect": -0.25
}

# Image folder paths
IMAGE_PATHS = {
    "math": "./images/math/",
    "english": "./images/english/",
    "analytical": "./images/analytical/"
}

# Math topics (must match your folder names)
MATH_TOPICS = [
    "age", "average", "fraction", "interest", "number",
    "permutation", "profit-loss", "ratio", "solids", "triangle",
    "angle", "circle", "inequality", "mixture", "percentage",
    "probability", "quadrilateral", "set", "speed", "workdone"
]

# English topics (must match your folder names)
ENGLISH_TOPICS = [
    "analogy", "correct-use-of-word", "error-detection",
    "reading-comprehension", "rearrange", "sentence-completion",
    "sentence-correction", "suffix-prefix", "syn-ant"
]

# Analytical topics (must match your folder names)
ANALYTICAL_TOPICS = [
    "cr", "ds", "puzzle"
]