#!/bin/sh
set -e

echo "[INFO] Checking config file existing"
if [ ! -f "./data/config.yaml" ]; then
  echo "[WARN] Config file not found, copying default config..."
  cp ./templates/config.template.yaml ./data/config.yaml
else
  echo "[INFO] Config file found, skipping copy."
fi


echo "[INFO] Fixing permissions for kekicord user..."
chown -R kekicord:kekicord /app

echo "[INFO] Starting BOT"
exec gosu kekicord python3 main.py