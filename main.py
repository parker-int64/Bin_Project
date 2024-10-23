#!/usr/bin/env python3

import os
import sys
import logging
import subprocess
import platform
import argparse
from Backend.src.project_dirs import (BASE_DIR, BACKEND_DIR, FRONTEND_DIR,STATIC_DIR)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

APP_VERSION_MAJOR = 0
APP_VERSION_MINOR = 0
APP_VERSION_PATCH = 1




CURRENT_PLATFORM = platform.system()

def env_check() -> bool:
    """
        check the environments
    """
    try:
        logging.info("Current platform %s", CURRENT_PLATFORM)

         # we can directly output the python version, 'python -V' is unnecessary
        logging.info("Python version %s", sys.version)
        pip_check = subprocess.run(["pip", "-V"],capture_output=True, text=True, check=False)
        logging.info("pip version %s", pip_check.stdout.strip())
        node_check = subprocess.run(["node", "-v"], capture_output=True, text=True, check=False)
        logging.info("Node version %s", node_check.stdout.strip())

        # Who the hell know why npm in windows is not a executable file...
        npm_check = subprocess.run(["npm", "-v"],
                                   shell=CURRENT_PLATFORM == "Windows",
                                   capture_output=True, text=True, check=False)

        logging.info("npm version %s", npm_check.stdout.strip())


    except subprocess.CalledProcessError as e:
        logging.error("Some of the requirements were not satisfied: \n %s", e.output)
        return False
    except FileNotFoundError:
        logging.error("Script or executable not found")
        return False

    return True


def build_frontend():
    """
        build frontend files
    """
    logging.info("Building the frontend files...")

    try:
        with subprocess.Popen([
            "npm", "install"
        ], cwd=FRONTEND_DIR, shell= CURRENT_PLATFORM == "Windows") as p:
            p.wait()
        # if we have the 'dist' directory, usually dont need to rebuild
        # this should save some time.

        with subprocess.Popen([
                "npm", "run", "build"
            ], cwd=FRONTEND_DIR, shell= CURRENT_PLATFORM == "Windows") as p1:
            p1.wait()
         
    except subprocess.CalledProcessError as e:
        logging.error("Error building the frontend... \n %s", e.output)
        logging.info("Consider running 'npm install' and 'npm run build' in frontend directory.")



def start_uvicorn(module: str):
    """
        start uvicorn
    """
    try:
        with subprocess.Popen([
            "uvicorn", f"{module}:app", "--reload"
        ], cwd=BACKEND_DIR, shell= CURRENT_PLATFORM == "Windows") as uvicorn:
            uvicorn.wait()

    except subprocess.CalledProcessError as e:
        logging.error("Error starting uvicorn \n %s", e.output)



def start_npm_server():
    """
        start the npm server (Vite)
    """
    # try:
    #     with subprocess.Popen([
    #             "npm", "run", "dev"
    #         ], cwd=FRONTEND_DIR, shell= CURRENT_PLATFORM == "Windows") as vite:
    #         vite.wait()
         
    # except subprocess.CalledProcessError as e:
    #     logging.error("Error starting vite \n %s", e.output)  
    logging.info("Please open a new terminal and execute 'cd Frontend && npm run dev'")

def launch_dev(module: str):
    """
        Run our application in development mode
    """
    start_npm_server() # So, why am I doing this...
    start_uvicorn(module)

def launch_rel(module: str):
    """
        Build and launch application
    """

    build_frontend()

    start_uvicorn(module)


def main():
    """
        running the FastAPI app 
    """

    parser = argparse.ArgumentParser(
        prog="Dashboard",
        description=f"Bin Project v{APP_VERSION_MAJOR}.{APP_VERSION_MINOR}.{APP_VERSION_PATCH}",
        epilog="Copyright(r) 2024, Team 404"
    )

    parser.add_argument("module", help="Which backend module to execute")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-d", "--dev", action="store_true",help="Run application in development mode")

    group.add_argument("-r", "--rel", action="store_true",help="Build project and launch in release mode")

    args = parser.parse_args()


    if args.dev:
        logging.info("Launching the application in development mode.")
        launch_dev(args.module)
    elif args.rel:
        logging.info("Launching the application in release mode, using uvicorn to serve the app.")
        launch_rel(args.module)
    else:
        parser.print_help()
        parser.error("Please choose launch the app either in development or release mode.")



if __name__ == "__main__":
    main()
    