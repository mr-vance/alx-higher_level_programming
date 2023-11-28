all:  # Target name

    # Set permissions to 700 for all files in the directory
    chmod 700 *

    # Check Python code style using pycodestyle for the most recently modified .py file
    pycodestyle $$(shell ls -t *.py | head -1)

    # Check if pycodestyle returned an error
    if [ $$? -ne 0 ]; then \  # If the exit code is not 0 (indicating an error)
        echo "error on style"; \  # Print an error message
        exit 1; \  # Exit with a non-zero status code
    fi  # End of if statement

    # Add all changes in the directory to the Git staging area
    git add .

    # Commit changes with a message indicating the most recently modified .py file
    git commit -a -m "$$(shell ls -t *.py | head -1)"

    # Push changes to the remote Git repository
    git push
