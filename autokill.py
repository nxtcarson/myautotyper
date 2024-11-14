# Patterns to match in process names
$patterns = @("Splashtop", "SR")
$dllName = "pciappctrl64.dll"

while ($true) {
    # Find and kill processes with matching patterns in their name
    foreach ($pattern in $patterns) {
        Get-Process | Where-Object { $_.Name -like $pattern } | ForEach-Object {
            try {
                $_.Kill()
                Write-Output "Killed process: $($_.Name) (PID: $($_.Id))"
            } catch {
                Write-Output "Failed to kill process: $($_.Name)"
            }
        }
    }

    # Look for processes that have the pciappctrl64.dll loaded and kill them
    $processesWithDll = Get-WmiObject Win32_Process | Where-Object { $_.Modules -match $dllName }
    foreach ($process in $processesWithDll) {
        try {
            Stop-Process -Id $process.ProcessId -Force
            Write-Output "Killed process with pciappctrl64.dll (PID: $($process.ProcessId))"
        } catch {
            Write-Output "Failed to kill process with pciappctrl64.dll (PID: $($process.ProcessId))"
        }
    }

    Start-Sleep -Seconds 2  # Adjust sleep time as needed
}
