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
    ) else ( goto :choice ) 
    

:somewhere
    echo[
    echo %username% Just teleported into the chat from Jungle
    echo Press 1 = World News
    echo Press 2 = Tech News
    echo Press 3 = Stock News
   :ConfirmBox 
        set /P n= Which News type you want to be updated with (1/2/3) ?  

    if /I "%n%" EQU "1" (
    goto :WorldNews
    ) else if /I "%n%" EQU "2" ( 
    goto :TechNews
    )  else if /I "%n%" EQU "3" ( 
    goto :StockNews
    ) else ( 
    goto :InERROR 
    )
    :WorldNews
        echo[      
        echo I am here because you want to see World News
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bizshala.com/ https://merolagani.com/ https://www.cnbc.com/world/ https://www.setopati.com/ https://www.onlinekhabar.com/ https://www.ratopati.com/ https://ekantipur.com/ https://www.sciencealert.com/ https://www.insider.com/asia/ https://myrepublica.nagariknetwork.com/news/nepse-up-marginally-after-sunday-s-rally/ https://news.google.com/topstories/
        echo[
        echo Please ! Don't close this Window. 
        echo Please ! Wait for 2 min for next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bloomberg.com/asia https://www.cnbc.com/world/ https://t.me/WorldNews https://www.theguardian.com/international https://www.businessinsider.com/sai https://www.vice.com/en https://www.thehimalayantimes.com/ https://www.hamropatro.com/news https://annapurnapost.com/ https://www.bbc.com/news/world https://nepsealpha.com/ https://www.sciencealert.com/ https://www.insider.com/asia/ https://myrepublica.nagariknetwork.com/news/
        goto :END      
        rem goto :ConfirmBox  
    	rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
    	rem pause

    :TechNews
        echo I am here because you want to see Tech News 
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://news.ycombinator.com/ https://hackersonlineclub.com/ https://www.theverge.com/ https://www.xda-developers.com/ https://www.bleepingcomputer.com/ https://www.maketecheasier.com/   https://www.makeuseof.com/  https://www.techpana.com/ https://www.androidpolice.com/ https://www.windowscentral.com/blog https://t.me/Technology_updates https://www.makeuseof.com/
        
        echo[
        echo Please ! Don't close this Window. 
        echo Please ! Wait for 2 min for next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 

        start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://t.me/Science_News_Facts_Updates_daily https://t.me/Technology_updates   https://www.techpana.com/ ttps://www.androidpolice.com/ https://www.windowscentral.com/blog https://t.me/Technology_updates/
        
        echo[
        echo Please ! Don't close this Window. 
        echo Please ! Wait for 2 min for next wave of news to lunch
        ping -n 120 127.0.0.1 > nul 

    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.pcmag.com/ https://www.businessinsider.com/sai  https://www.computerworld.com/in/category/windows/ https://www.linuxtoday.com/ https://thehackernews.com/ https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://t.me/Science_News_Facts_Updates_daily/
        goto :END 

    :StockNews
        echo I am here because you want to see Stock News
    	start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.nepalstock.com/news/category/0 https://merolagani.com/ https://nepsealpha.com/ https://www.bizshala.com/ https://newweb.nepalstock.com.np/ https://www.sharebazarnepal.com.np/ http://nepalstockinfo.com/ https://investingnepal.com/ https://www.sharesansar.com/ https://www.nepalipaisa.com/ https://merocapital.com/
        goto :END

    :InERROR
        echo Invalid selection. Enter given seleted number [1/2/3].
        goto :somewhere 
    exit

:somewhere_else
    echo I'm here because it's Business hrs
    rem start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://newweb.nepalstock.com.np/ https://nepsealpha.com/trading/chart
    start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://newweb.nepalstock.com.np/ https://nepsealpha.com/trading/chart
    %SystemRoot%\explorer.exe "D:\excel Files\hello.xlsx"   
    goto:choice

:bitfar
    echo[
    echo Brace yourselves..Activating Jasmine flying carpet
    echo Press 1 =  Folder 1
    echo Press 2 =  Folder 2
    echo Press 3 =  Folder 3
    echo Press 4 =  Folder 4

   :SUREBOX
        set /P t= Which Folder you want to Travel (1/2/3/4) ?  

    if /I "%t%" EQU "1" (
    goto :Fnpy 
    ) else if /I "%t%" EQU "2" ( 
    goto :Fncmd
    )  else if /I "%t%" EQU "3" ( 
    goto :Fnexcel
    ) else if /I "%t%" EQU "4" ( 
    goto :Fnproj
    ) else ( 
    goto :InValid 
    )
    :Fnpy
        echo Travelling to  Folder
        %SystemRoot%\explorer.exe "D:\Folder2"
        goto :END
    :Fncmd
        echo Travelling to  Folder      
        %SystemRoot%\explorer.exe "D:\Folder2"
        goto :END
    :Fnexcel
        echo Travelling to  Folder        
        %SystemRoot%\explorer.exe "D:\Folder3"
        goto :END
    :Fnproj
        echo Travelling to  Folder
        %SystemRoot%\explorer.exe "D:\Folder4"
        goto :END
    :InValid
        echo Invalid selection. Enter given seleted number [1/2/3/4].
        goto :bitfar
    exit

:lazyme
    echo[
    echo Roses are red, violets are blue, %username% joined this chat to apply IPO.
    echo Press 1 = Summon up Bot!
    echo Press * = See ya!
   :CHECKBOX 
        set /P s= Welcome, press secret key to activate God's eye:   

    if /I "%s%" EQU "1" (
    goto :APLYIPO
    ) else ( 
    goto :InWrong
    )

    :APLYIPO
        echo[
        echo       .d8888b.   .d88888b.   .d88888b.  8888888b.       888     888     888  .d8888b.  888    d8P  
        echo      d88P  Y88b d88P" "Y88b d88P" "Y88b 888  "Y88b      888     888     888 d88P  Y88b 888   d8P   
        echo      888    888 888     888 888     888 888    888      888     888     888 888    888 888  d8P    
        echo      888        888     888 888     888 888    888      888     888     888 888        888d88K     
        echo      888  88888 888     888 888     888 888    888      888     888     888 888        8888888b    
        echo      888    888 888     888 888     888 888    888      888     888     888 888    888 888  Y88b   
        echo      Y88b  d88P Y88b. .d88P Y88b. .d88P 888  .d88P      888     Y88b. .d88P Y88b  d88P 888   Y88b  
        echo       "Y8888P88  "Y88888P"   "Y88888P"  8888888P"       88888888 "Y88888P"   "Y8888P"  888    Y88b                                                                                                                                                                                                                                                                                       
        echo[
    	echo "IN WIP"
        ping -n 15 127.0.0.1 > nul         
        exit

    :InWrong
        echo "Goodbye %username% ! It's gonna be lonely without ya.",
        goto :choice

:faraway
    echo[
    echo Smells like %username% device is fresh! 
    echo Press 1 = Basic kit
    echo Press 2 = Intermediate kit
    rem echo Press 3 = Advanced kit
   :farbox 
        set /P k= Which kit would you like to proceed with (1/2) ?  

    if /I "%k%" EQU "1" (
    goto :Basic
    ) else if /I "%k%" EQU "2" ( 
    goto :Intermediate
    ) else ( 
    goto :Errorkit 
    )
    :Basic
        start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.mozilla.org/en-US/  https://discord.com/download http://bit.ly/2WZMML0 https://www.sublimetext.com/download http://obsproject.com/download http://www.google.com/chrome/ http://www.zoom.us/download https://www.videolan.org/vlc/download-windows.en_GB.html http://calibre-ebook.com/download http://www.7-zip.org/download.html  http://bit.ly/3Et0NB0 https://bit.ly/3OMQuMW
        goto:farbox
    :Intermediate
        start "Edge" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://bit.ly/3bhyTPG https://intel.ly/3bklcQ3 http://www.qbittorrent.org/download.php http://www.virtualbox.org/ http://github.com/hovancik/stretchly/releases  https://git-scm.com/downloads http://www.python.org/downloads/  http://codecguide.com/download_kl.htm http://bit.ly/3nikTZx  http://code.visualstudio.com/download
        goto:END    
    :Errorkit 
        goto:faraway


:pyproj 
    @echo off
    cd %~dp0\
    if not exist "%~dp0\venv\Scripts\activate" (
    echo Creating venv for your *.py
    cd %~dp0\
    echo Changed directory to %~dp0
    python -m venv venv
    echo Initialization of venv completed!)

    echo[
    echo Press 1 = Download Youtube Videos
    echo Press 2 = Scrap IMDb Movies
    echo Press * = Give up!
    :checkpy 
        set /P p= Welcome, press secret key to lunch *.py :      
    if /I "%p%" EQU "1" (
    goto :ytdown
    ) else if /I "%p%" EQU "2" ( 
    goto :scrapimdb
    ) else ( 
    goto :Wrongpy
    )

    :scrapimdb                                                                                                                                            
        echo Getteing on board !
        echo[
        cmd /k "cd %~dp0\venv\Scripts & activate & cd /d  %~dp0 & pip install -U -r requirements.txt & cd /d %~dp0\modules & python imdb.py & cd /d%~dp0\venv\Scripts & deactivate.bat & exit"
        goto:pyproj
               
    :ytdown
        @echo off
        echo[
        echo I'm here because you want to download Youtube Videos
        cmd /k "cd %~dp0\venv\Scripts & activate & cd /d  %~dp0 & pip install -U -r requirements.txt & cd /d %~dp0\modules & python youtube.py & cd /d%~dp0\venv\Scripts & deactivate.bat & exit"
        goto:pyproj

    :Wrongpy
        echo "Goodbye %username% ! It's gonna be lonely without ya.",
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
	
	 

     
 


