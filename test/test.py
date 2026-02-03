import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.database import engine

print("DB engine OK:", engine)
