# Snapshot file
# Unset all aliases to avoid conflicts with functions
unalias -a 2>/dev/null || true
# Functions
# Shell Options
setopt nohashdirs
setopt login
# Aliases
alias -- run-help=man
alias -- which-command=whence
# Check for rg availability
if ! command -v rg >/dev/null 2>&1; then
  alias rg='/usr/local/lib/node_modules/\@anthropic-ai/claude-code/vendor/ripgrep/arm64-darwin/rg'
fi
export PATH=/opt/local/bin\:/opt/local/sbin\:/opt/homebrew/bin\:/opt/homebrew/sbin\:/usr/local/bin\:/System/Cryptexes/App/usr/bin\:/usr/bin\:/bin\:/usr/sbin\:/sbin\:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin\:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin\:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin\:/Applications/Trae.app/Contents/Resources/app/bin\:/Users/tszkinlai/.local/bin\:/opt/local/bin\:/opt/local/sbin\:/Users/tszkinlai/.cargo/bin
