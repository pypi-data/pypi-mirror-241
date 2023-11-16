import os
from importlib import resources

def main():
    os.environ["STREAMLIT_THEME_BASE"] = "dark"
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run 0_👋_Hello.py")
