import sys
import os

# Set working directory to project root
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Launch Master Zaifer 14-Titan Architecture
import zaifer_app

if __name__ == "__main__":
    zaifer_app.main()
