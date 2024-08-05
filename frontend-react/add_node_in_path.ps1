# Define the path to be added
$nodeJsPath = "C:\nodejs"

# Get the current PATH environment variable
$currentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

# Check if the path already exists
if ($currentPath -notlike "*$nodeJsPath*") {
    # Add the new path
    $newPath = "$currentPath;$nodeJsPath"
    
    # Set the new PATH variable
    [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
    
    Write-Host "Added $nodeJsPath to the system PATH variable."
} else {
    Write-Host "$nodeJsPath is already in the system PATH variable."
}
