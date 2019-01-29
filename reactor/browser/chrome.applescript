on run argv
  set buildpath to item 1 of argv & "/build"
  
  tell application "Google Chrome"
    set allwins to every window
    repeat with w in allwins
    	set alltabs to every tab of w
      set tabnum to 0
    	repeat with t in alltabs
        set tabnum to tabnum + 1
        # find open page
    		if (URL of t contains buildpath) then
          # set focus on window
          tell w
            set index to 1
            set visible to false
            set visible to true
          end tell
          # set focus on tab
          set active tab index of w to tabnum
    		  tell t
            reload
          end tell
          activate
          return
    		end if
    	end repeat
    end repeat
    
    # if not already open
    open location buildpath & "/index.html"
    activate
  end tell
end run
