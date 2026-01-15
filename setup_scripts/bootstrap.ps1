$ErrorActionPreference = "Stop"

Write-Host "🔧 Bootstrapping environment..."

# Detect uv
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Installing uv..."
    Invoke-WebRequest -Uri https://astral.sh/uv/install.ps1 -UseBasicParsing | Invoke-Expression
} else {
    Write-Host "✅ uv already installed"
}

# Ensure PATH is refreshed (important on Windows)
$env:PATH += ";$HOME\.cargo\bin"

# Create venv & install deps
uv venv .venv
uv sync

Write-Host "🎉 Environment ready"
