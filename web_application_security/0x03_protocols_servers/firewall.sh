#!/bin/bash
iptables -A INPUT -p tcp --dport ssh -j ACCEPT
iptables -A INPUT -j DROP
