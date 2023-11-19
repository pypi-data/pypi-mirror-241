import os
from importlib import resources

def main():
    package_dir = resources.path(package='test_tele', resource="").__enter__()
    print(package_dir)
    path = os.path.join(package_dir, "0_👋_Hello.py")

    os.environ["STREAMLIT_THEME_BASE"] = "dark"
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run {path}")
