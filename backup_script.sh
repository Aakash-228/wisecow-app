# backup_script.sh

#!/bin/bash

SOURCE_DIR="/path/to/source/directory"
DEST_DIR="/path/to/destination/directory"
LOG_FILE="/path/to/logfile.log"

# Create a timestamp
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Backup the directory
if rsync -av --delete "$SOURCE_DIR" "$DEST_DIR" >> "$LOG_FILE" 2>&1; then
    echo "Backup successful at $TIMESTAMP" >> "$LOG_FILE"
else
    echo "Backup failed at $TIMESTAMP" >> "$LOG_FILE"
fi