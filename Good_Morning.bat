@ECHO OFF
:choice
echo HEY!! Have a Good day!!.
echo "TIME IS PASSING & DON't WASTE it OR else You'll regret soon"

echo[

echo Press 1=="Start with day with Updated News Sources"
echo Press 2=="It's Stock Time"
echo Press 3=="Navigate to Project Folder."

echo[
echo Jst a little bit more ...
echo[

echo Press 4=="Travel to Folders"
rem echo Press 5=="QR-Code"

echo[
set /P c=Feed me just Number so I can work for you!! [1-4] ?  
if /I "%c%" EQU "1" goto :somewhere
if /I "%c%" EQU "2" goto :somewhere_else
if /I "%c%" EQU "3" goto :faraway
if /I "%c%" EQU "4" goto :bitfar
rem if /I "%c%" EQU "5" goto :jstfar
goto :choice


:somewhere

echo "I am here because you want to be Updated"
echo[
echo Press 1=="World News"
echo Press 2=="Tech News"
echo Press 3=="Stock News"


   :ConfirmBox 
        set /P c= Which News you want to be updated with (1/2/3) ?  

    if /I "%c%" EQU "1" (
    goto :WorldNews
    ) else if /I "%c%" EQU "2" ( 
    goto :TechNews
    )  else if /I "%c%" EQU "3" ( 
    goto :StockNews
    ) else ( 
    goto :InValid 
    )


:WorldNews
    echo Travelling to Python Folder
    echo "I am here because you want to see News"
	start "Firefox" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bizshala.com/ https://merolagani.com/ https://www.cnbc.com/world/ https://www.setopati.com/ https://www.onlinekhabar.com/ https://www.ratopati.com/ https://ekantipur.com/ https://www.bloomberg.com/asia https://www.cnbc.com/world/ https://t.me/WorldNews https://www.theguardian.com/international https://www.businessinsider.com/sai https://www.vice.com/en https://www.thehimalayantimes.com/ https://www.hamropatro.com/news https://annapurnapost.com/ https://www.bbc.com/news/world https://nepsealpha.com/ https://www.sciencealert.com/ https://www.insider.com/asia? https://myrepublica.nagariknetwork.com/news/nepse-up-marginally-after-sunday-s-rally/ https://news.google.com/topstories/
	goto:END

rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic


:TechNews
    echo "I am here because you want to see Tech News"
	start "Firefox" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://news.ycombinator.com/ https://hackersonlineclub.com/ https://www.theverge.com/ https://www.xda-developers.com/ https://www.bleepingcomputer.com/ https://www.maketecheasier.com/ https://www.pcmag.com/ https://www.businessinsider.com/sai https://www.androidpolice.com/ https://www.windowscentral.com/blog https://www.computerworld.com/in/category/windows/ https://www.linuxtoday.com/ https://thehackernews.com/ https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://t.me/Science_News_Facts_Updates_daily https://t.me/Technology_updates https://www.makeuseof.com/  https://www.techpana.com/ 
    goto :END 

rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic

:StockNews
    echo "I am here because you want to see Stock News"
	start "Firefox" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.nepalstock.com/news/category/0 https://merolagani.com/ https://nepsealpha.com/ https://www.bizshala.com/ https://newweb.nepalstock.com.np/ https://www.sharebazarnepal.com.np/ http://nepalstockinfo.com/ https://investingnepal.com/ https://www.sharesansar.com/ https://www.nepalipaisa.com/ https://merocapital.com/
	goto: END

rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
 
rem pause

exit

:somewhere_else

echo "I am here because it's Business hrs"
start "Chrome" "C:\Program Files\Mozilla Firefox\firefox.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://newweb.nepalstock.com.np/ https://nepsealpha.com/trading/chart
%SystemRoot%\explorer.exe "D:\power"


rem start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
rem pause
exit


:faraway

echo "I am here because you want to see Your Project Folder "
%SystemRoot%\explorer.exe "D:\apple"

rem pause
exit

:bitfar
echo "I am here because you want to travel to folders "
echo[
echo Press 1 ==" File"
echo Press 2 ==" File"
echo Press 3 ==" File"


   :ConfirmBox 
        set /P c= Which Folder you want to Travel (1/2/3) ?  

    if /I "%c%" EQU "1" (
    goto :Fnpy 
    ) else if /I "%c%" EQU "2" ( 
    goto :Fncmd
    )  else if /I "%c%" EQU "3" ( 
    goto :Fnexcel
    ) else ( 
    goto :InValid 
    )


:Fnpy
    echo Travelling to  Folder
    %SystemRoot%\explorer.exe "D:\apple"
    goto :END
:Fncmd
    echo Travelling to Command Folder
    %SystemRoot%\explorer.  "D:\apple""
    goto :END
:Fnexcel
    echo Travelling to  Folder
    %SystemRoot%\explorer.exe  "D:\apple"

    goto :ENDWeb
:InValid
    echo Invalid selection. Enter given seleted number [1/2/3].
    goto :ConfirmBox


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

pause
exit
	
	 

     
 


