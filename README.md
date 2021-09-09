# Fortinet-Subnet-Checker
A quick tool designed to check if a list of subnets or an AS Number contains any IP addresses affected by the Fortinet credential dump. This list simply contains the IP addresses and not the leaked details. More details on the leak can be found here; https://thehackernews.com/2021/09/hackers-leak-vpn-account-passwords-from.html

Code has only been tested on Python 3.9, no additional dependencies are required.

Thanks to https://gist.github.com/crypto-cypher for the SFW IP list.

NOTE: The script makes use of the built in linux whois command, so it's unlikely to run properly on windows.
