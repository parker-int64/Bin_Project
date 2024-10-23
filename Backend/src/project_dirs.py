from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent.parent

STATIC_DIR = BASE_DIR/"Frontend/dist"

FRONTEND_DIR = BASE_DIR/"Frontend/"

BACKEND_DIR = Path(__file__).absolute().parent

# if __name__ == "__main__":
#     print(f"Base directory: {BASE_DIR}\nFrontend Directory: {FRONTEND_DIR}\n" +
#            f"Backend directory: {BACKEND_DIR}\nStatic directory: {STATIC_DIR}")