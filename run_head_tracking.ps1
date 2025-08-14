Write-Host "Starting Head Tracking Project..." -ForegroundColor Green
Write-Host ""

Write-Host "Running MonitorTracking.py..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python MonitorTracking.py" -WindowStyle Normal

Write-Host "Running CursorCircle.py..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python CursorCircle.py" -WindowStyle Normal

Write-Host ""
Write-Host "Both scripts are now running!" -ForegroundColor Green
Write-Host ""
Write-Host "Controls:" -ForegroundColor Cyan
Write-Host "- F7: Toggle mouse control on/off" -ForegroundColor White
Write-Host "- C: Calibrate when looking straight ahead" -ForegroundColor White
Write-Host "- Q: Quit the application" -ForegroundColor White
Write-Host ""
Write-Host "Press any key to close this window..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")


