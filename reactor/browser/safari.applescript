on run argv
  set buildpath to item 1 of argv & "/build"
  
  tell application "Safari"
    open location buildpath & "/index.html"
    activate
  end tell
end run
