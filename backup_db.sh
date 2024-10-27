#!/bin/bash

source .env

DB_USER=$REMOTE_DB_USER
DB_HOST=$REMOTE_DB_HOST
DB_NAME=$REMOTE_DB_NAME
DB_PASSWORD=$REMOTE_DB_PASSWORD
BACKUP_DIR="db_backups"
CURRENT_DATETIME=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILENAME="${CURRENT_DATETIME}.sql"

mkdir -p "$BACKUP_DIR"
PGPASSWORD="$DB_PASSWORD" pg_dump -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -F p -f "${BACKUP_DIR}/${BACKUP_FILENAME}"
echo "Database backup completed: ${BACKUP_DIR}/${BACKUP_FILENAME}"