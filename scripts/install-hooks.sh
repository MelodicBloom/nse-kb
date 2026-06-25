#!/bin/bash
# Run once after cloning to install the pre-commit front-matter validation hook.
set -e
HOOK_PATH=".git/hooks/pre-commit"
cat > "$HOOK_PATH" << 'HOOKEOF'
#!/bin/bash
echo "Running KB front-matter validation..."
python3 scripts/validate_frontmatter.py
if [ $? -ne 0 ]; then
  echo ""
  echo "Commit blocked: fix front-matter errors above."
  exit 1
fi
echo "Front-matter valid — proceeding with commit."
HOOKEOF
chmod +x "$HOOK_PATH"
echo "Pre-commit hook installed at $HOOK_PATH"
