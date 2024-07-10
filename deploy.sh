#!/usr/bin/env bash
source ".env"

REMOTE="$ZOLA_USER@$ZOLA_DOMAIN:$ZOLA_REMOTE_FOLDER/slides/vortraege/ep2024-python-unplugged"
pnpm run build && scp -i "$ZOLA_KEY" -r dist/* "$REMOTE"

