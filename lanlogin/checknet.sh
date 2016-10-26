#!/bin/bash
# title: checknet.sh
# version: 0.1
# date: october 11, 2016
# author: Abo Tang 
#echo "enter your sgatway"

#read sgateway

ip="8.8.8.8"
echo "the orgin ip is $ip"
delay=5000
echo "the set max delay is $delay ms"
nexttime=600
echo "check every $nexttime s"
echo "########################################"
while :
do
network=`ping -c 1 $ip  |  awk 'NR==2 {print $7}' | sed "s/=/ /g"  | awk '{print $2}'`

expr ${network} + 0 1>/dev/null 2>&1
if [ $? -eq 0 ]; then
        python3 /home/admint/bin/lanlogin/login.py
else
        value_n=`echo $network | sed "s/\.//g"`
        if [ "$value_n" -lt "$delay" ];
        then
                echo "the network is OK"
                echo "the delay time is $network ms"
                echo "########################"
        else
                python3 /home/admint/bin/lanlogin/login.py
        fi
fi

sleep $nexttime
done 
