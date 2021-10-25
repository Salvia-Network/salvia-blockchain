$ErrorActionPreference = "Stop"

if ([Environment]::Is64BitOperatingSystem -eq $false)
{
    Write-Output "Salvia requires a 64-bit Windows installation"
    Exit 1
}

if (-not (Get-Item -ErrorAction SilentlyContinue "$env:windir\System32\msvcp140.dll").Exists)
{
    Write-Output "Unable to find Visual C++ Runtime DLLs"
    Write-Output ""
    Write-Output "Download and install the Visual C++ Redistributable for Visual Studio 2019 package from:"
    Write-Output "https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2019"
    Exit 1
}

if ($null -eq (Get-Command git -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find git"
    Exit 1
}

git submodule update --init mozilla-ca

if ($null -eq (Get-Command py -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find py"
    Write-Output "Note the check box during installation of Python to install the Python Launcher for Windows."
    Write-Output ""
    Write-Output "https://docs.python.org/3/using/windows.html#installation-steps"
    Exit 1
}

$pythonVersion = (py --version).split(" ")[1]
if ([version]$pythonVersion -lt [version]"3.7.0")
{
    Write-Output "Found Python version:" $pythonVersion
    Write-Output "Installation requires Python 3.7 or later"
    Exit 1
}
Write-Output "Python version is:" $pythonVersion

py -m venv venv
.\venv\Scripts\Activate.ps1

py -m pip install pip --upgrade
pip install --upgrade setuptools
pip install --upgrade wheel
pip install --extra-index-url https://pypi.chia.net/simple/ miniupnpc==2.2.2
pip install --editable . --extra-index-url https://pypi.chia.net/simple/

Write-Output ""
Write-Output "Salvia blockchain .\Install.ps1 complete."
Write-Output "For assistance join us on Keybase in the #support chat channel:"
Write-Output "https://keybase.io/team/salvia_network.public"
Write-Output ""
Write-Output "Try the Quick Start Guide to running salvia-blockchain:"
Write-Output "https://github.com/Salvia-Network/salvia-blockchain/wiki/Quick-Start-Guide"
Write-Output ""
Write-Output "To install the GUI type '.\Install-gui.ps1' after '.\venv\scripts\Activate.ps1'."
Write-Output ""
Write-Output "Type '.\venv\Scripts\Activate.ps1' and then 'salvia init' to begin."