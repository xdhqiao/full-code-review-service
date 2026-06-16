param(
    [string]$Python = "python",
    [string]$Destination = "vendor",
    [string]$Platform = "manylinux_2_17_x86_64",
    [string]$Implementation = "cp",
    [string]$PythonVersion = "311",
    [string]$Abi = "cp311"
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
& $Python -m pip download `
    --only-binary=:all: `
    --platform $Platform `
    --implementation $Implementation `
    --python-version $PythonVersion `
    --abi $Abi `
    --dest $Destination `
    -r requirements.txt
