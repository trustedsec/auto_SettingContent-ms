### Auto .SettingContent-ms

This is a simple script for automating the creation of a MSHTA downloader (HTA) through the .SettingContent-ms extension type discovered by Matt Nelson (@engima0x3) from SpecterOps. Simply run the tool, and ensure that Metasploit and Apache is installed. It will generate a Metasploit Meterpreter (reverse https) payload through a malicious HTA. THe .SettingContent-ms can then be used inside of an office document, an attachment, or downloaded from the Internet to coax victim to clicking.

Simply run:

python auto_settingcontent-ms.py

Enter the IP address or hostname of the reverse shell
Enter the port

Let the magic happen.

CREDIT: Matt Nelson (@enigma0x3) for the discovery
Written by: Dave Kennedy (@HackingDave, @TrustedSec)
