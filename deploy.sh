#!/usr/bin/env bash
source ".env"

REMOTE="$ZOLA_USER@$ZOLA_DOMAIN:$ZOLA_REMOTE_FOLDER/slides/vortraege/ep2024-python-unplugged"
LOCAL="$HOME/project/lokidev-blog/static/slides/vortraege/ep2024-python-unplugged"

pnpm run build --base /slides/vortraege/ep2024-python-unplugged/
scp -i "$ZOLA_KEY" -r dist/* "$REMOTE"
cp -r dist "$LOCAL"

