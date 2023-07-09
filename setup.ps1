# Check if pipenv is installed
if (-not (Get-Command pipenv -ErrorAction SilentlyContinue)) {
    Write-Host "pipenv is not installed. Installing pipenv..."
    & python -m pip install pipenv
}

if ($env:VIRTUAL_ENV) {
    Write-Host "There is already an active current shell. Please type `exit` and run this script again"
}

# Install development dependencies if not already installed
Write-Host "Installing development dependencies..."
& pipenv install --dev

# Create the .venv folder if it doesn't exist
$venvPath = ".\.venv"
if (-not (Test-Path -Path $venvPath)) {
    Write-Host "Creating .venv folder..."
    New-Item -ItemType Directory -Path $venvPath | Out-Null
}

# Activate the pipenv shell if not already activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Activating pipenv shell..."
    & pipenv shell
} else {
    Write-Host "pipenv shell is already activated."
}

# Display success message
Write-Host "Python project setup complete!"