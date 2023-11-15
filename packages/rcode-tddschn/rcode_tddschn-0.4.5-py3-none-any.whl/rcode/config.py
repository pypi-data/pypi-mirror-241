from pathlib import Path

RCODE_HOME = Path.home() / ".rcode"

vscode_release_channel_to_cli_name = {
    "stable": "code",
    "insiders": "code-insiders",
}
