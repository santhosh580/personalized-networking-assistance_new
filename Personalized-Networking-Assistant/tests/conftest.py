# tests/conftest.py

import sys
from pathlib import Path

# Add root directory to sys.path to allow imports from app
sys.path.append(str(Path(__file__).resolve().parent.parent))
