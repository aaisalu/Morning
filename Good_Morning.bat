@ECHO OFF
color 7
for /f "delims=:" %%A in ("%time%") do if %%A LSS 12 (
echo[
echo          .d8888b.                         888       888b     d888                           d8b                   
echo         .88P  Y88b                        888       8888b   d8888                           Y8P                   
echo        .888    888                        888       88888b.d88888                                                 
echo        .888         .d88b.   .d88b.   .d88888       888Y88888P888  .d88b.  888d888 88888b.  888 88888b.   .d88b.  
echo        .888  88888 d88""88b d88""88b d88" 888       888 Y888P 888 d88""88b 888P"   888 "88b 888 888 "88b d88P"88b 
echo         888    888 888  888 888  888 888  888       888  Y8P  888 888  888 888     888  888 888 888  888 888  888 
echo         Y88b  d88P Y88..88P Y88..88P Y88b 888       888   "   888 Y88..88P 888     888  888 888 888  888 Y88b 888 
echo          "Y8888P88  "Y88P"   "Y88P"   "Y88888       888       888  "Y88P"  888     888  888 888 888  888  "Y88888 
echo                                                                                                               888 
echo                                                                                                          Y8b d88P 
echo                                                                                                           "Y88P"  
)else if %%A LSS 18 (
echo[
echo         .oOOOo.                   o          Oo    oooo                                             
echo        .O     o                  O          o  O   O                                                
echo        o                         o         O    o  o     O                                          
echo        O                         o        oOooOoOo OoO  oOo                                          
echo        O   .oOOo .oOo. .oOo. .oOoO        o      O o     o    .oOo. `OoOo. 'OoOo. .oOo. .oOo.  ooOoo 
echo        o.      O O   o O   o o   O        O      o O     O    OooO'  o      o   O O   o O   o  o   O 
echo         O.    oO o   O o   O O   o        o      O o     o    O      O      O   o o   O o   O  O   o 
echo          `OooO'  `OoO' `OoO' `OoO'o       O.     O O     ooo  `OoO'  o      o   O `OoO' `OoO'  o   O   
echo[                                                                                                                                                                                           
) else if %%A LSS 22 (
echo[
echo        .d8888b.                         888       8888888888                            d8b                   
echo       .88P  Y88b                        888       888                                   Y8P                   
echo      .888    888                        888       888                                                         
echo      .888         .d88b.   .d88b.   .d88888       8888888    888  888  .d88b.  88888b.  888 88888b.   .d88b.  
echo      .888  88888 d88""88b d88""88b d88" 888       888        888  888 d8P  Y8b 888 "88b 888 888 "88b d88P"88b 
echo       888    888 888  888 888  888 888  888       888        Y88  88P 88888888 888  888 888 888  888 888  888 
echo        88b  d88P Y88..88P Y88..88P Y88b 888       888         Y8bd8P  Y8b.     888  888 888 888  888 Y88b 888 
echo        "Y8888P88  "Y88P"   "Y88P"   "Y88888       8888888888   Y88P    "Y8888  888  888 888 888  888  "Y88888 
echo                                                                                                           888 
echo                                                                                                      Y8b d88P
echo                                                                                                       "Y88P" 
) else (
echo[
echo         ::::::::   ::::::::   ::::::::  :::::::::       ::::    ::: ::::::::::: ::::::::  :::    ::: ::::::::::: 
echo        :+:    :+: :+:    :+: :+:    :+: :+:    :+:      :+:+:   :+:     :+:    :+:    :+: :+:    :+:     :+:     
echo        +:+        +:+    +:+ +:+    +:+ +:+    +:+      :+:+:+  +:+     +:+    +:+        +:+    +:+     +:+     
echo        :#:        +#+    +:+ +#+    +:+ +#+    +:+      +#+ +:+ +#+     +#+    :#:        +#++:++#++     +#+     
echo        +#+   +#+# +#+    +#+ +#+    +#+ +#+    +#+      +#+  +#+#+#     +#+    +#+   +#+# +#+    +#+     +#+     
echo        #+#    #+# #+#    #+# #+#    #+# #+#    #+#      #+#   #+#+#     #+#    #+#    #+# #+#    #+#     #+#     
echo         ########   ########   ########  #########       ###    #### ########### ########  ###    ###     ###     
)

echo %date% %time% 
rem echo It's a bird! It's a plane! - Nope, its %username% from %COMPUTERNAME% device!
echo Something just fell from the sky! - oh, its %username% from %COMPUTERNAME% device!

rem echo Copy this code to lunch Firefox browser :  start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe"
rem echo Copy this code to lunch Chrome  browser :   start "Chrome"  "C:\Program Files\Google\Chrome\Application\chrome.exe"

:choice
    echo[
    echo Press 1 = Start your day with Updated News Sources
    echo Press 2 = Beep..Beep Boop! It's Stock Time
    echo Press 3 = Travel to Folders
    echo Press 4 = Summon *.py
    echo Press 5 = Apply IPO
    echo Press 6 = Dress up
    echo Press 0 = Leave
    echo[
    :brain
    set /P brn=Feed me just Number so, I can work for you!! [1-6] ? 
    if /I "%brn%" EQU "1" ( goto :somewhere
    ) else if  /I "%brn%" EQU "2" ( goto :somewhere_else
    ) else if  /I "%brn%" EQU "3" ( goto :bitfar
    ) else if  /I "%brn%" EQU "4" ( goto :pyproj
    ) else if  /I "%brn%" EQU "5" ( goto :lazyme
    ) else if  /I "%brn%" EQU "6" ( goto :faraway
    ) else if  /I "%brn%" EQU "0" ( exit
    ) else (goto :choice) 
    
:somewhere
    echo[
    echo %username% Just teleported into the chat from Jungle!
    echo Press 1 = World News
    echo Press 2 = Tech News
    echo Press 3 = Stock News
    echo Press 0 = Depart
   :ConfirmBox 
        set /P n= Which News type do you want to be updated with (1/2/3) ?  

    if /I "%n%" EQU "1" (
    goto :WorldNews
    ) else if /I "%n%" EQU "2" ( 
    goto :TechNews
    )  else if /I "%n%" EQU "3" ( 
    goto :StockNews
    ) else if /I "%n%" EQU "0" (
    goto:choice 
    )else ( goto :InERROR 
    )
    :WorldNews
        echo[      
        echo I am here because you want to see World News
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bizshala.com/ https://merolagani.com/ https://www.cnbc.com/world/ https://www.setopati.com/ https://www.onlinekhabar.com/ https://www.ratopati.com/ https://ekantipur.com/ https://www.sciencealert.com/ https://www.insider.com/asia/ https://myrepublica.nagariknetwork.com/news/nepse-up-marginally-after-sunday-s-rally/ https://news.google.com/topstories/
        echo[
        echo Please! Don't close this Window. 
        echo Please! Wait for 2 min for the next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bloomberg.com/asia https://www.cnbc.com/world/ https://t.me/WorldNews https://www.theguardian.com/international https://www.businessinsider.com/sai https://www.vice.com/en https://www.thehimalayantimes.com/ https://www.hamropatro.com/news https://annapurnapost.com/ https://www.bbc.com/news/world https://nepsealpha.com/ https://www.sciencealert.com/ https://www.insider.com/asia/ https://myrepublica.nagariknetwork.com/news/
        goto :END      
        rem goto :ConfirmBox  
    	rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
    	rem pause

    :TechNews
        echo[
        echo I am here because you want to see Tech News 
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://news.ycombinator.com/ https://hackersonlineclub.com/ https://www.theverge.com/ https://www.xda-developers.com/ https://www.bleepingcomputer.com/ https://www.maketecheasier.com/   https://www.makeuseof.com/  https://www.techpana.com/ https://www.androidpolice.com/ https://www.windowscentral.com/blog https://t.me/Technology_updates https://www.makeuseof.com/
        
        echo[
        echo Please! Don't close this Window. 
        echo Please! Wait for 2 min for the next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 

        start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://t.me/Science_News_Facts_Updates_daily https://t.me/Technology_updates   https://www.techpana.com/ ttps://www.androidpolice.com/ https://www.windowscentral.com/blog https://t.me/Technology_updates/
        
        echo[
        echo Please! Don't close this Window. 
        echo Please! Wait for 2 min for the next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 

    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.pcmag.com/ https://www.businessinsider.com/sai  https://www.computerworld.com/in/category/windows/ https://www.linuxtoday.com/ https://thehackernews.com/ https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://t.me/Science_News_Facts_Updates_daily/
        goto :END 

    :StockNews
        echo[
        echo I am here because you want to see Stock News
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.nepalstock.com/news/category/0 https://merolagani.com/ https://nepsealpha.com/ https://www.bizshala.com/ https://newweb.nepalstock.com.np/ https://www.sharebazarnepal.com.np/ http://nepalstockinfo.com/ https://investingnepal.com/ https://www.sharesansar.com/ https://www.nepalipaisa.com/ https://merocapital.com/
        goto :END

    :InERROR
        echo[
        echo Looks like someone having a hard time selecting a digit: [1/2/3].
        goto :somewhere 
    exit

:somewhere_else
    pause
    echo[
    echo I'm here because it's Business hrs
    rem start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://newweb.nepalstock.com.np/ https://nepsealpha.com/trading/chart
    start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://mail.google.com/mail/u/0/#inbox https://newweb.nepalstock.com.np/ https://nepsealpha.com/trading/chart
    echo Opening your Excel balance sheet
    %SystemRoot%\explorer.exe "D:\excel Files\hello.xlsx"   
    goto:choice

:bitfar
    echo[
    echo Brace yourselves...Activating Jasmine flying carpet
    echo Press 1 = Folder 1
    echo Press 2 = Folder 2
    echo Press 3 = Folder 3
    echo Press 4 = Folder 4
    echo Press 0 = Depart

   :SUREBOX
        set /P t= Which folder do you want to Travel (1/2/3/4) ?  

    if /I "%t%" EQU "1" (
    goto :Fnpy 
    ) else if /I "%t%" EQU "2" ( 
    goto :Fncmd
    )  else if /I "%t%" EQU "3" ( 
    goto :Fnexcel
    ) else if /I "%t%" EQU "4" ( 
    goto :Fnproj
    ) else if /I "%t%" EQU "0" (
    goto:choice 
    )else ( 
    goto :InValid 
    )
    :Fnpy
        echo Traveling to Folder
        %SystemRoot%\explorer.exe "D:\Folder2"
        goto :END
    :Fncmd
        echo Traveling to Folder      
        %SystemRoot%\explorer.exe "D:\Folder2"
        goto :END
    :Fnexcel
        echo Traveling to Folder        
        %SystemRoot%\explorer.exe "D:\Folder3"
        goto :END
    :Fnproj
        echo Traveling to Folder
        %SystemRoot%\explorer.exe "D:\Folder4"
        goto :END
    :InValid
        echo Use your jet ticket wisely. [1-4]
        goto :bitfar
    exit

:lazyme
    echo[
    echo Roses are red, violets are blue, %username% joined this chat to apply IPO.
    echo Press 1 = Summon up Bot to apply IPO!
    rem echo Press 2 = Wake Bot to check IPO
    echo Press 0 = See ya!
   :CHECKBOX 
        set /P s= Welcome, press the secret key to activate God's eye: 

    if /I "%s%" EQU "1" (
    goto :APLYIPO
    ) else ( 
    goto :InWrong
    )

    :APLYIPO
        echo[
        echo             .d8888b.   .d88888b.   .d88888b.  8888888b.       888     888     888  .d8888b.  888    d8P  
        echo            d88P  Y88b d88P" "Y88b d88P" "Y88b 888  "Y88b      888     888     888 d88P  Y88b 888   d8P   
        echo            888    888 888     888 888     888 888    888      888     888     888 888    888 888  d8P    
        echo            888        888     888 888     888 888    888      888     888     888 888        888d88K     
        echo            888  88888 888     888 888     888 888    888      888     888     888 888        8888888b    
        echo            888    888 888     888 888     888 888    888      888     888     888 888    888 888  Y88b   
        echo            Y88b  d88P Y88b. .d88P Y88b. .d88P 888  .d88P      888     Y88b. .d88P Y88b  d88P 888   Y88b  
        echo             "Y8888P88  "Y88888P"   "Y88888P"  8888888P"       88888888 "Y88888P"   "Y8888P"  888    Y88b                                                                                                                                                                                                                                                                                       
        echo[
    	echo "IN WIP"
        ping -n 15 127.0.0.1 > nul         
        exit

    :InWrong
        echo[
        echo "Goodbye %username% ! It's gonna be lonely without ya.",
        goto :choice

:faraway
    echo[
    echo Feels like %username% device needs some medic kit! 
    echo Press 1 = Fly to the web of software
    echo Press 2 = Install/Update software through chocolatey
    echo Press 3 = Generate Battery report
    echo Press 4 = Reset Network Devices
    echo Press 5 = Repair your pc
    echo Press 0 = Depart
    rem echo Press 4 = Advanced kit

   :farbox 
        set /P k= Which kit would you like to proceed with (1/2/3) ?  

    if /I "%k%" EQU "1" (
    goto :websoft
    ) else if /I "%k%" EQU "2" ( 
    goto :choco
    ) else if /I "%k%" EQU "0" (
    goto:choice 
    ) else if /I "%k%" EQU "3" ( 
    goto :battreport
    )else if /I "%k%" EQU "4" ( 
    goto :repairnet
    )else if /I "%k%" EQU "5" ( 
    goto :repairpc
    ) else ( 
    goto :faraway 
    )
    :websoft
        echo[
        echo Press 1 = Fly to the web of Basic kit software
        echo Press 2 = Fly to the web of Intermediate kit software
        echo Press 0 = Depart
            set /P wb= Welcome, Which web of software do you want to fly ?[1/2]: 
        if /I "%wb%" EQU "1" (
        goto :basic
        ) else if /I "%wb%" EQU "2" ( 
         goto :mediate
        )else if /I "%wb%" EQU "0" ( 
         goto :faraway
        )else ( 
        goto :websoft
        )
        :basic
            echo[
            echo Flying to respective links of Basic kit software
            start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.mozilla.org/en-US/  https://discord.com/download http://bit.ly/2WZMML0 https://www.sublimetext.com/download http://obsproject.com/download http://www.google.com/chrome/ http://www.zoom.us/download https://www.videolan.org/vlc/download-windows.en_GB.html http://calibre-ebook.com/download http://www.7-zip.org/download.html  http://bit.ly/3Et0NB0 https://bit.ly/3OMQuMW
            goto:faraway
        :mediate
            echo[
            echo Flying to respective links of Intermediate kit software
            start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://bit.ly/3bhyTPG https://intel.ly/3bklcQ3 http://www.qbittorrent.org/download.php http://www.virtualbox.org/ http://github.com/hovancik/stretchly/releases  https://git-scm.com/downloads http://www.python.org/downloads/  http://codecguide.com/download_kl.htm http://bit.ly/3nikTZx  http://code.visualstudio.com/download
            goto:faraway
    :choco
        echo OFF
        :: Thanks to @blak3r for check admin rights stackoverflow.com/a/8995407
        rem NET SESSION >nul 2>&1
        rem IF %ERRORLEVEL% EQU 0 (
        rem     echo[ 
        rem     echo Admin user detected!
        rem     echo Installing Chocolatey Please be patient...
        rem     echo This should only take another few minutes or less, and then you'll be good to go!
        rem     echo[
        rem     echo             .d8888b.  888                                888          888                     
        rem     echo            d88P  Y88b 888                                888          888                     
        rem     echo            888    888 888                                888          888                     
        rem     echo            888        88888b.   .d88b.   .d8888b .d88b.  888  8888b.  888888 .d88b.  888  888 
        rem     echo            888        888 "88b d88""88b d88P"   d88""88b 888     "88b 888   d8P  Y8b 888  888 
        rem     echo            888    888 888  888 888  888 888     888  888 888 .d888888 888   88888888 888  888 
        rem     echo            Y88b  d88P 888  888 Y88..88P Y88b.   Y88..88P 888 888  888 Y88b. Y8b.     Y88b 888 
        rem     echo             "Y8888P"  888  888  "Y88P"   "Y8888P "Y88P"  888 "Y888888  "Y888 "Y8888   "Y88888 
        rem     echo                                                                                           888 
        rem     echo                                                                                      Y8b d88P 
        rem     echo                                                                                       "Y88P"  
        rem     rem powershell -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        rem     echo Sweet Chocolatey is ready to serve you!
        rem ) ELSE (
        rem    echo[
        rem    echo             `OooOOo.                                            Oo         o                    
        rem    echo              o     `o                                          o  O       O           o         
        rem    echo              O      O                                         O    o      o                     
        rem    echo              o     .O                                        oOooOoOo     o                     
        rem    echo              OOooOO'  O   o  'OoOo.       .oOoO' .oOo        o      O .oOoO  `oOOoOO. O  'OoOo. 
        rem    echo              o    o   o   O   o   O       O   o  `Ooo.       O      o o   O   O  o  o o   o   O 
        rem    echo              O     O  O   o   O   o       o   O      O       o      O O   o   o  O  O O   O   o 
        rem    echo              O      o `OoO'o  o   O       `OoO'o `OoO'       O.     O `OoO'o  O  o  o o'  o   O    
        rem    echo[                                                  
        rem    echo               ------------------  ERROR: ADMINISTRATOR PRIVILEGES REQUIRED  -------------------
        rem    echo This script must be run as administrator to work as it installs the chocolatey to install software 
        rem    echo[
        rem    echo If you're seeing this, then right click on this script and select "Run As Administrator".
        rem    echo OR Follow this guide: https://gearupwindows.com/how-to-open-command-prompt-as-administrator-in-windows-10-8-7/
        rem    echo[ 
        rem    PAUSE
        rem    EXIT /B 1
        rem )
        :: Thanks Chocolatey for being it so amazing chocolatey.org
        echo[                                
        echo                                                         Welcome To The
        echo                                                 Chocolatey Packages Repository
        echo                                   Select the corresponding number to the software to install!                                            
        echo[             
        echo       [1] Chrome            [9] Notepad++        [17] VirtualBox            [25] Viber          [33] CrystalDiskInfo
        echo       [2] Brave            [10] Git              [18] Discord               [26] Telegram       [34] Adobe Acrobat 
        echo       [3] Firefox          [11] FFmpeg           [19] K-Lite Codec Pack     [27] WhatsApp       [35] AutoHotkey
        echo       [4] Spotify          [12] qBittorrent      [20] VLC media player      [28] Youtube-dl     [36] Irfanview
        echo       [5] Calibre          [13] Malwarebytes     [21] Office 365            [29] Blender        [37] Audacity
        echo       [6] OBS Studio       [14] WinRAR           [22] Libreoffice           [30] Python         [38] Graphics
        echo       [7] VScode           [15] 7-Zip            [23] Zoom Meetings         [31] Atom           [39] PDF24 
        echo       [8] Sublime Text     [16] Google Drive     [24] Microsoft Teams       [32] Greenshot      [40]
        echo       _____________________________________________________________________________________________________________        
        echo                                                Install Recommended Software [100]
        echo                      Firefox,WinRAR,7-Zip,VLC media player,Zoom Meetings,Sublime Text,Spotify,Office 365 
        echo                                     ___________________________________________________________     
        echo[     
        echo                                                  Install Basic Software [200] 
        echo                         Visual Studio Code, Discord, Telegram, qBittorrent,OBS project, git ,Calibre 
        echo                                                __________________________________     
        echo[                                        
        echo                                                    Update all software [00]                                                                                                                              
        echo                                                             Exit [0]      
        echo[                                                                         
            set /P fun= Welcome, Which of the software would you like to taste? [1-30]: 
        if /I "%fun%" EQU "1" (
        goto :loveOne                                                       
        ) else if /I "%fun%" EQU "2" ( 
         goto :loveTwo                                          
        )else if /I "%fun%" EQU "3" ( 
         goto :loveThree
        )else if /I "%fun%" EQU "4" (                        
         goto :loveFour
        )else if /I "%fun%" EQU "4" ( 
         goto :loveFive
        )else if /I "%fun%" EQU "6" ( 
         goto :loveSix
        )else if /I "%fun%" EQU "7" ( 
         goto :loveSeven
        )else if /I "%fun%" EQU "8" ( 
         goto :loveEight
        )else if /I "%fun%" EQU "9" ( 
         goto :loveNine
        )else if /I "%fun%" EQU "10" ( 
         goto :loveTen
        )else if /I "%fun%" EQU "11" ( 
         goto :loveEleven
        )else if /I "%fun%" EQU "12" ( 
         goto :loveTwelve
        )else if /I "%fun%" EQU "13" ( 
         goto :loveThirteen
        )else if /I "%fun%" EQU "14" ( 
         goto :loveFourteen
        )else if /I "%fun%" EQU "15" ( 
         goto :loveFifteen
        )else if /I "%fun%" EQU "16" ( 
         goto :loveSixteen
        )else if /I "%fun%" EQU "17" ( 
         goto :loveSeventeen
        )else if /I "%fun%" EQU "18" ( 
         goto :loveEighteen
        )else if /I "%fun%" EQU "19" ( 
         goto :loveNineteen
        )else if /I "%fun%" EQU "20" ( 
         goto :loveTwenty
        )else if /I "%fun%" EQU "21" ( 
         goto :loveTwentyone
        )else if /I "%fun%" EQU "22" ( 
         goto :loveTwentytwo
        )else if /I "%fun%" EQU "23" ( 
         goto :loveTwentythree
        )else if /I "%fun%" EQU "24" ( 
         goto :loveTwentyfour
        )else if /I "%fun%" EQU "25" ( 
         goto :loveTwentyfive
        )else if /I "%fun%" EQU "26" ( 
         goto :loveTwentysix
        )else if /I "%fun%" EQU "27" ( 
         goto :loveTwentyseven
        )else if /I "%fun%" EQU "28" ( 
         goto :loveTwentyeight
        )else if /I "%fun%" EQU "29" ( 
         goto :loveTwentynine
        )else if /I "%fun%" EQU "30" ( 
         goto :loveThirty
        )else if /I "%fun%" EQU "31" ( 
         goto :loveThirtyOne
        )else if /I "%fun%" EQU "32" ( 
         goto :loveThirtyTwo
        )else if /I "%fun%" EQU "33" ( 
         goto :loveThirtyThree
        )else if /I "%fun%" EQU "34" ( 
         goto :loveThirtyFour
        )else if /I "%fun%" EQU "35" ( 
         goto :loveThirtyFive
        )else if /I "%fun%" EQU "36" ( 
         goto :loveThirtySix
        )else if /I "%fun%" EQU "37" ( 
         goto :loveThirtySeven
        )else if /I "%fun%" EQU "38" ( 
         goto :loveThirtyEight
        )else if /I "%fun%" EQU "39" ( 
         goto :loveThirtyNine
        )else if /I "%fun%" EQU "40" ( 
         goto :loveFourty
        )else if /I "%fun%" EQU "100" ( 
         goto :lovehundred
        )else if /I "%fun%" EQU "200" ( 
         goto :lovetwohundred
        )else if /I "%fun%" EQU "00" ( 
         goto :updateall
        )else if /I "%fun%" EQU "0" ( 
         goto :choice
        )else ( 
        goto :bitterchoco
        )
        echo[
        echo Installing choco GUI for software management
        choco install chocolateygui -y
        echo chocolatey GUI is installed and updated sucessfully !
        echo[
        :loveOne    
            choco install googlechrome -y  
            goto:choco           
        :loveTwo  
            choco install brave -y       
            goto:choco 
        :loveThree  
            choco install firefox -y 
            goto:choco   
        :loveFour   
            choco install spotify -y 
            goto:choco
        :loveFive  
            choco install calibre -y 
            goto:choco   
        :loveSix   
            choco install obs-studio.install -y 
            goto:choco       
        :loveSeven  
            choco install vscode -y 
            goto:choco   
        :loveEight  
            choco install sublimetext4 -y 
            goto:choco   
        :loveNine   
            choco install notepadplusplus.install -y 
            goto:choco   
        :loveTen  
            choco install git.install  
            goto:choco       
        :loveEleven  
            choco install ffmpeg
            goto:choco
        :loveTwelve 
            choco install qbittorrent -y 
            goto:choco
        :loveThirteen
            choco install malwarebytes -y 
            goto:choco
        :loveFourteen
            choco install winrar -y 
            goto:choco
        :loveFifteen  
            choco install 7zip.install -y  
            goto:choco
        :loveSixteen   
            choco install googledrive -y 
            goto:choco
        :loveSeventeen
            choco install virtualbox -y 
            goto:choco
        :loveEighteen
            choco install discord.install -y 
            goto:choco
        :loveNineteen
            choco install k-litecodecpackfull -y 
            goto:choco
        :loveTwenty 
            choco install vlc -y  
            :goto:choco
        :loveTwentyone
            choco install office365proplus -y  
            goto:choco
        :loveTwentytwo  
            choco install libreoffice-fresh -y 
            goto:choco
        :loveTwentythree 
            choco install zoom -y 
            goto:choco   
        :loveTwentyfour  
            choco install microsoft-teams.install -y 
            goto:choco
        :loveTwentyfive
            choco install viber -y 
            goto:choco
        :loveTwentysix 
            choco install telegram.install -y    
            goto:choco
        :loveTwentyseven
            choco install whatsapp -y 
            goto:choco   
        :loveTwentyeight
            choco install  youtube-dl -y  
            goto:choco
        :loveTwentynine
            choco install blender -y
            goto:choco
        :loveThirty 
            choco install python3 
            goto:choco
        :loveThirtyOne    
            choco install atom -y 
            goto:choco           
        :loveThirtyTwo  
            choco install greenshot -y       
            goto:choco 
        :loveThirtyThree  
            choco install crystaldiskinfo -y 
            goto:choco   
        :loveThirtyFour   
            choco install adobereader -y 
            goto:choco
        :loveThirtyFive  
            choco install autohotkey.install -y 
            goto:choco   
        :loveThirtySix   
            choco install irfanview -y
            goto:choco       
        :loveThirtySeven  
            choco install audacity -y 
            goto:choco   
        :loveThirtyEight
            echo[
            echo [1] Intel  Graphics DCH  
            echo [2] Nvidia Graphics DCH
            echo [0] Exit 
            set /P drv= Welcome, Which Graphics do you want to install?: 
            if /I "%drv%" EQU "1" (
            goto:intelgra
            ) else if /I "%drv%" EQU "2" ( 
            goto :nvidiagra
            )else if /I "%drv%" EQU "0" ( 
            goto :choco
            )else ( 
            goto :lovethirtyeight
            )
            :intelgra
                choco install intel-graphics-driver
                goto:choco
            :nvidiagra
                choco install nvidia-display-driver 
                goto:choco   
        :loveThirtyNine
            choco install pdf24 -y
            goto:choco
        :loveFourty
            goto:choco
        :lovehundred
            choco install winrar -y
            choco install vlc -y
            choco install firefox -y
            choco install 7zip.install -y
            choco install office365proplus -y   
            choco install zoom -y
            choco install sublimetext4 -y
            choco install spotify -y
            goto:choco

        :lovetwohundred
            choco install vscode -y
            choco install discord -y
            choco install telegram -y
            choco install git -y
            choco install obs-studio -y
            choco install calibre -y
            choco install qbittorrent -y
            goto:choco

        :updateall
            choco upgrade all -y
            goto:choco
        :bitterchoco
            echo "Ops! Don't you like to have choco bar? "
            goto:choco             
    :battreport
        echo[
        echo Generate battery report of your %COMPUTERNAME% device !
        cd %USERPROFILE%\Desktop
        powercfg /batteryreport
        echo Saved at %USERPROFILE%\Desktop
        goto:faraway
    :repairnet
        echo OFF
        :: Thanks to @blak3r for check admin rights stackoverflow.com/a/8995407
        NET SESSION >nul 2>&1
        IF %ERRORLEVEL% EQU 0 (
            echo[ 
            echo It resets your network devices and network stack
            echo This should only take another few minutes or less, and then you'll be good to go!
            echo Ref: https://intel.ly/3OP6luA
            echo[
            pause  
            ipconfig /release 
            ipconfig /flushdns
            ipconfig /renew   
            netsh int ip reset 
            netsh winsock reset 
            echo Please! Restart your pc
            goto:faraway
        ) ELSE (
           echo[
           echo             `OooOOo.                                            Oo         o                    
           echo              o     `o                                          o  O       O           o         
           echo              O      O                                         O    o      o                     
           echo              o     .O                                        oOooOoOo     o                     
           echo              OOooOO'  O   o  'OoOo.       .oOoO' .oOo        o      O .oOoO  `oOOoOO. O  'OoOo. 
           echo              o    o   o   O   o   O       O   o  `Ooo.       O      o o   O   O  o  o o   o   O 
           echo              O     O  O   o   O   o       o   O      O       o      O O   o   o  O  O O   O   o 
           echo              O      o `OoO'o  o   O       `OoO'o `OoO'       O.     O `OoO'o  O  o  o o'  o   O    
           echo[                                                  
           echo               ------------------  ERROR: ADMINISTRATOR PRIVILEGES REQUIRED  -------------------
           echo This script must be run as administrator to work as it resets your network devices and network stack
           echo[
           echo If you're seeing this, then right click on this script and select "Run As Administrator".
           echo OR Follow this guide: https://gearupwindows.com/how-to-open-command-prompt-as-administrator-in-windows-10-8-7/
           echo[ 
           PAUSE
           EXIT /B 1
        )

    :repairpc
        echo OFF
        :: Thanks to @blak3r for check admin rights stackoverflow.com/a/8995407
        NET SESSION >nul 2>&1
        IF %ERRORLEVEL% EQU 0 (
            echo[ 
            echo The Deployment Image Servicing and Management tool can be used to scan and repair potential issues with the .wim store in Windows that may impact system files.
            echo This should take 10-20 minutes to run, but depending on circumstances it can potentially take over an hour.
            echo Ref: https://dell.to/3d2EqtO
            echo[
            pause
            Dism /Online /Cleanup-Image /ScanHealth
            Dism /Online /Cleanup-Image /RestoreHealth
            ::for offline repair
            rem Dism /Image:C:\offline /Cleanup-Image /RestoreHealth /Source:c:\test\mount\windows
            rem Dism /Online /Cleanup-Image /CheckHealth
            echo Please! Restart your pc
            goto:faraway
        ) ELSE (
           echo[
           echo             `OooOOo.                                            Oo         o                    
           echo              o     `o                                          o  O       O           o         
           echo              O      O                                         O    o      o                     
           echo              o     .O                                        oOooOoOo     o                     
           echo              OOooOO'  O   o  'OoOo.       .oOoO' .oOo        o      O .oOoO  `oOOoOO. O  'OoOo. 
           echo              o    o   o   O   o   O       O   o  `Ooo.       O      o o   O   O  o  o o   o   O 
           echo              O     O  O   o   O   o       o   O      O       o      O O   o   o  O  O O   O   o 
           echo              O      o `OoO'o  o   O       `OoO'o `OoO'       O.     O `OoO'o  O  o  o o'  o   O    
           echo[                                                  
           echo               ------------------  ERROR: ADMINISTRATOR PRIVILEGES REQUIRED  -------------------
           echo This script must be run as administrator to work as it uses DISM to Repair a Windows image 
           echo[
           echo If you're seeing this, then right click on this script and select "Run As Administrator".
           echo OR Follow this guide: https://gearupwindows.com/how-to-open-command-prompt-as-administrator-in-windows-10-8-7/
           echo[ 
           PAUSE
           EXIT /B 1
        )

    :Errorkit 
        echo[
        echo You are playing it wrong, press only one digit! [1/2/3]
        goto:faraway


:pyproj 
    @echo off
    cd %~dp0\
    if not exist "%~dp0\venv\Scripts\activate" (
    echo[
    echo Creating venv for your *.py
    cd %~dp0\
    echo Changed directory to %~dp0
    echo[ 
    echo Please be patient...
    echo This should only take another few minutes or less, and then you'll be good to go!
    python -m venv venv
    echo Initialization of venv completed!
    echo I apologize for making you wait )
    echo[
    echo             dP                                   dP              dP                          
    echo             88                                   88          8b. 88 .d8                      
    echo             88        dP    dP 88d888b. .d8888b. 88d888b.     `8b88d8'     88d888b. dP    dP 
    echo             88        88    88 88'  `88 88'  `"" 88'  `88     .8P88Y8.     88'  `88 88    88 
    echo             88        88.  .88 88    88 88.  ... 88    88    8P' 88 `Y8 dP 88.  .88 88.  .88 
    echo             88888888P `88888P' dP    dP `88888P' dP    dP        dP     88 88Y888P' `8888P88 
    echo                                                                            88            .88 
    echo                                                                            dP        d8888P  
    echo[
    echo Press 1 = Download Youtube Videos
    echo Press 2 = Scrap IMDb Movies
    echo Press 0 = Depart

    :checkpy   
        set /P p= Welcome, press the secret key to lunch *.py: 
    if /I "%p%" EQU "1" (
    goto :ytdown
    ) else if /I "%p%" EQU "2" ( 
    goto :scrapimdb
    ) else if /I "%p%" EQU "0" (
    goto:choice
    ) else ( 
    goto :pyproj
    )

    :scrapimdb                                                                                                                                            
        echo Getting on board !
        echo[
        :: Thanks to Ashish Gupta user2350219 for the py injection through bat
        :: stackoverflow.com/a/30927921
        cmd /k "cd %~dp0\venv\Scripts & activate & cd /d  %~dp0 & pip install -U -r requirements.txt & cd /d %~dp0\modules & python imdb.py & cd /d%~dp0\venv\Scripts & deactivate.bat & exit"
        goto:pyproj
               
    :ytdown
        @echo off
        echo[
        echo I'm here because you want to download Youtube Videos
        cmd /k "cd %~dp0\venv\Scripts & activate & cd /d  %~dp0 & pip install -U -r requirements.txt & cd /d %~dp0\modules & python youtube.py & cd /d%~dp0\venv\Scripts & deactivate.bat & exit"
        goto:pyproj


rem :jstfar 
rem 	@echo off
	
rem 	echo[	
rem 	@echo off
rem 	md %USERPROFILE%\pictures\QRcode   
rem 	pip install qrcode[pil]		


rem 	set Output="%USERPROFILE%\pictures\QRcode"
rem 	set File="%USERPROFILE%\pictures\QRcode"
	
rem 	echo[	
	
rem 	echo Press 1=="Create QR code"
rem 	echo Press 2=="NO QR code"

rem    :Box 
rem         set /P c= Create QR to share Fast (1/2) ? 
rem 	echo[
rem 	if /I "%c%" EQU "1" (
rem 	goto :Yesqr 
rem     	) else if /I "%c%" EQU "2" ( 
rem     	goto :Noqr)
rem 	goto:Box


rem :Yesqr
rem 	set /p Qrask=Type desired text to convert into Qr code:
rem 	REM enter your desired output here
rem 	qr %Qrask% >> %Output%\Qr.png
rem 	echo Qrinput   = %Qrask% >> %Output%\Qrinputdata.txt
rem 	echo File has been placed %File%	
rem 	pause	
rem 	exit
	
rem :Noqr	
rem 	echo No Jokearound here!!
rem 	timeout 2 >nul
rem 	goto :END

rem pause
rem exit
	
	 

     
 


