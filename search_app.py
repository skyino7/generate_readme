#!/usr/bin/env python3
"""
Searches for an app in available
package repositories and prompts
to install it.
"""

import os
import sys
import subprocess

def search_app(app_name):
    """
    Searches for an app in available package repositories and prompts to install it.
    """
    # Determine the package manager based on the operating system
    if os.path.exists("/usr/bin/apt"):
        package_manager = "apt"
    elif os.path.exists("/usr/local/bin/brew"):
        package_manager = "brew"
    else:
        print("Unsupported package manager. Please use a system with apt or brew.")
        sys.exit(1)

    # Construct the search command based on the package manager
    if package_manager == "apt":
        search_command = ["apt-cache", "search", app_name]
    elif package_manager == "brew":
        search_command = ["brew", "search", app_name]

    try:
        # Execute the search command
        result = subprocess.run(search_command, capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout:
                print(f"Search results for '{app_name}':")
                print(result.stdout)
                select_and_install_app(result.stdout, package_manager)
            else:
                print(f"No results found for '{app_name}'.")
        else:
            print(f"Error occurred while searching for '{app_name}'.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def select_and_install_app(search_results, package_manager):
    """
    Prompts the user to select an app from the search results and installs it.
    """
    apps = search_results.split('\n')
    apps = [app for app in apps if app.strip()]

    if not apps:
        print("No valid search results found.")
        return

    print("\nPlease select an app to install by entering the corresponding number:")
    for idx, app in enumerate(apps, start=1):
        print(f"{idx}. {app.split(' - ')[0]}")

    while True:
        try:
            choice = int(input("\nEnter the number of the app to install: "))
            if 1 <= choice <= len(apps):
                app_name = apps[choice - 1].split(' - ')[0].strip()
                install_app(app_name, package_manager)
                break
            else:
                print("Invalid selection. Please enter a number between 1 and", len(apps))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(1)

def install_app(app_name, package_manager):
    """
    Installs the selected app.
    """
    install_prompt = input(f"Do you want to install '{app_name}'? (y/n): ").strip().lower()
    if install_prompt == 'y':
        if package_manager == "apt":
            install_command = ["sudo", "apt", "install", app_name, "-y"]
        elif package_manager == "brew":
            install_command = ["brew", "install", app_name]

        try:
            # Execute the install command
            subprocess.run(install_command, check=True)
            print(f"'{app_name}' has been installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install '{app_name}'. Error: {e}")
    else:
        print("Installation aborted.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: search_app <app_name>")
        sys.exit(1)

    app_name = sys.argv[1]
    search_app(app_name)
