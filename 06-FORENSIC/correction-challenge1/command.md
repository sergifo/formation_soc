regripper/rip.exe -r correction-challenge1/SYSTEM -p compname
regripper/rip.exe -r correction-challenge1/SYSTEM -p timezone
regripper/rip.exe -r correction-challenge1/SOFTWARE -p winver
cat correction-challenge1/access.log | tail -n 10

regripper/rip.exe -r correction-challenge1/SAM -f sam > sam.txt
regripper/rip.exe -r correction-challenge1/SAM -p samparse | grep Username

Xampp
dvwa

sqlmap/1.0-dev-nongit-20150902
hosts

