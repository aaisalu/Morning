@ECHO OFF
:choice
echo HEY!! Have a Good day!!.
echo "TIME IS PASSING & DON't WASTE it OR else You'll regret soon"

echo[

echo Press 1=="Darling it's News"
echo Press 2=="Tech News"
echo Press 3=="Stock"

echo[
echo Jst a little bit more ...
echo[

echo Press 4=="Travel to Folders"
echo Press 5=="QR-Code"

echo[
set /P c=Feed me just Number so I can work for you!! [1-5] ?  
if /I "%c%" EQU "1" goto :somewhere
if /I "%c%" EQU "2" goto :somewhere_else
if /I "%c%" EQU "3" goto :faraway
if /I "%c%" EQU "4" goto :bitfar
if /I "%c%" EQU "5" goto :jstfar
goto :choice


:somewhere 

echo "I am here because you want to see News"
start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe" https://www.bizshala.com/ https://merolagani.com/ https://www.cnbc.com/world/ https://www.setopati.com/ https://www.onlinekhabar.com/ https://www.ratopati.com/ https://ekantipur.com/ https://www.bloomberg.com/asia https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en https://www.cnbc.com/world/ https://t.me/WorldNews

 
#pause
exit

:somewhere_else

echo "I am here because you want to see Tech News"
start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe" https://www.theverge.com/ https://www.xda-developers.com/ https://www.bleepingcomputer.com/ https://www.maketecheasier.com/ https://www.pcmag.com/ https://www.businessinsider.com/sai https://www.androidpolice.com/ https://www.windowscentral.com/blog https://www.computerworld.com/in/category/windows/ https://www.linuxtoday.com/ https://thehackernews.com/ https://www.androidauthority.com/ https://www.gadgetbytenepal.com/ https://mspoweruser.com/ https://beebom.com/ https://www.kitploit.com/ https://t.me/Science_News_Facts_Updates_daily https://t.me/Technology_updates 
#start /min "" explorer.exe shell:AppsFolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
#pause
exit


:faraway

echo "I am here because you want to see Stock "
start "Firefox" "C:\Program Files\Mozilla Firefox\firefox.exe" https://tms51.nepsetms.com.np/login http://www.nepalstock.com/news/category/0 https://meroshare.cdsc.com.np/#/login https://merolagani.com/ https://newweb.nepalstock.com.np/ https://www.sharebazarnepal.com.np/ http://nepalstockinfo.com/ https://investingnepal.com/ https://www.bizshala.com/ http://www.mexnepal.com/webpages/technical_analysis_mex.html https://merocapital.com/company/nepse/nepal-stock-exchange-limited/advanced_technical_chart/ https://nepsealpha.com/trading/chart https://www.sharesansar.com/ https://www.nepalipaisa.com/
%SystemRoot%\explorer.exe "D:\DEca.xlsx"

#pause
exit

:bitfar
echo "I am here because you want to travel to folders "
echo[
echo Press 1=="fFile"
echo Press 2=="f File"
echo Press 3=="file"


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
    echo Travelling to Python Folder
    %SystemRoot%\explorer.exe "D:\Aozlrkasteck"
    goto :END
:Fncmd
    echo Travelling to Command Folder
    %SystemRoot%\explorer.exe "D:\Aozlrkasteckn"
    goto :END
:Fnexcel
    echo Travelling to Excel Folder
    %SystemRoot%\explorer.exe "D:\Aozlrkasteck"
    goto :END
:InValid
    echo Invalid selection. Enter given seleted number [1/2/3].
    goto :ConfirmBox


:jstfar 
	@echo off
	
	echo[	
	@echo off
	md %USERPROFILE%\pictures\QRcode   
	pip install qrcode[pil]		


	set Output="%USERPROFILE%\pictures\QRcode"
	set File="%USERPROFILE%\pictures\QRcode"
	
	echo[	
	
	echo Press 1=="Create QR code"
	echo Press 2=="NO QR code"

   :Box 
        set /P c= Create QR to share Fast (1/2) ? 
	echo[
	if /I "%c%" EQU "1" (
	goto :Yesqr 
    	) else if /I "%c%" EQU "2" ( 
    	goto :Noqr)
	goto:Box


:Yesqr
	set /p Qrask=Type desired text to convert into Qr code:
	REM enter your desired output here
	qr %Qrask% >> %Output%\Qr.png
	echo Qrinput   = %Qrask% >> %Output%\Qrinputdata.txt
	echo File has been placed %File%	
	pause	
	exit
	
	

	
:Noqr	
	echo No Jokearound here!!
	timeout 2 >nul
	goto :END

pause
exit
	
	 

     
 


