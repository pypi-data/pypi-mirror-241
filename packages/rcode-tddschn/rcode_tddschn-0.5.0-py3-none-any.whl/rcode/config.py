from pathlib import Path

# RCODE_HOME = Path.home() / ".rcode" # this is not a dir, but a csv file
RCODE_HOME = Path.home() / ".rcode-tddschn.csv"


vscode_release_channel_to_cli_name = {
    "stable": "code",
    "insiders": "code-insiders",
}
