# country-blocker-firewalld
Used to block selected countries

There's two folders, v4 and v6 for IPv4 and IPv6 respectively. There's two .tar.gz files in each of these, with ALL the countries from https://www.ipdeny.com/

Requires python3.8 & firewalld

To use:- 

cd v4
tar -zvzf all-zones.tar.gz

cd ../v6
tar -xvzf all-zones.tar.gz


**Important** 

Make sure to REMOVE the countries you want to keep. Run this code in screen, as it will take a long time.

ASYNC/IO is on the to do list.

This list is *not* conclusive. There may still be some IPs/ranges NOT on this list. 


chmod +x ipblock.sh init.py

./init.py 


Once the script has finished, you'll have to **reload the firewall** and restart the server. 

