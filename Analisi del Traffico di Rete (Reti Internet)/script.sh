#!/bin/bash

#file .tie
classtie="/home/peppe/Desktop/OutputCatture/2018-10-24_cattura_12_bin.tie"

#file .log
strace="/home/peppe/Desktop/gruppo16/1540374487/strace.log"

#file .gt.tie
classgttie="/home/peppe/Desktop/gedit_tie/1540374487.gt.tie"

#file .pcap
traffic="/home/peppe/Desktop/gruppo16/1540374487/traffic.pcap"

#dns request
dnsfile="/home/peppe/Desktop/gruppo16/1540374487/dns.txt"
dnscmd=$(tshark -r "$traffic" -T fields -e frame.time_epoch -e frame.protocols -e dns.a -e dns.qry.name -Y "(dns.flags.response == 1 )")
echo -e "${dnscmd[*]}" > $dnsfile

echo -e "# id\tsrc_ip\t\tdst_ip\t\tproto\tsport\tdport\tdwpkts\tuppkts\tdwbytes\tupbytes\tt_start\t\t\tt_last\t\t\tapp_id\tsub_id\tapp_details\tconfidence\t\tPACKAGE\t\tDNS\t\tDIG\t\tWHOIS" > $classgttie

while IFS='' read -r LINE || [[ -n "$LINE" ]];
do
	id=`echo $LINE | awk '{printf $1}'`
	src_ip=`echo $LINE | awk '{printf $2}'`
	dst_ip=`echo $LINE | awk '{printf $3}'`
	proto=`echo $LINE | awk '{printf $4}'`
	sport=`echo $LINE | awk '{printf $5}'`
	dport=`echo $LINE | awk '{printf $6}'`
	dwpkts=`echo $LINE | awk '{printf $7}'`
	uppkts=`echo $LINE | awk '{printf $8}'`
	dwbytes=`echo $LINE | awk '{printf $9}'`
	upbytes=`echo $LINE | awk '{printf $10}'`
	t_start=`echo $LINE | awk '{printf $11}'`
	t_last=`echo $LINE | awk '{printf $12}'`
	app_id=`echo $LINE | awk '{printf $13}'`
	sub_id=`echo $LINE | awk '{printf $14}'`
	app_details=`echo $LINE | awk '{printf $15}'`
	confidence=`echo $LINE | awk '{printf $16}'`

	#src_ip:sport->dst_ip:dport
	rsearch=$src_ip':'$sport'->'$dst_ip':'$d_port

	#package
	rpackage=`cat $strace | grep $rsearch | awk '{print $1}' | uniq`

	#dns
	rdns=`cat $dnsfile | grep $dst_ip | awk '{print $4}' | uniq`

	#whois
	rwhois=$(whois $dst_ip | grep -i "orgname\|org-name")

	if [ "$rpackage" = "" ]; then
		RIS1="UNKNOWN"
	else
		RIS1=$rpackage
	fi

	if [ "$rdns" = "" ]; then
		RIS2="UNKNOWN"

		#dig
		rdig=$(dig +short @8.8.8.8 -x $dst_ip)

		if [ "$rdig" = "" ]; then
			RIS3="UNKNOWN"
		else
			RIS3=$rdig
		fi
	else
		RIS2=$rdns
		RIS3="NOT_REQUIRED"
	fi

	if [ "$rwhois" = "" ]; then
		RIS4="UNKNOWN"
	else
		RIS4=$rwhois
	fi

	#output risultati
	echo -e "• ${id}\t${src_ip}\t${dst_ip}\t${proto}\t${sport}\t${dport}\t${dwpkts}\t${uppkts}\t${dwpkts}\t${upbytes}\t${t_start}\t${t_last}\t${app_id}\t${sub_id}\t${app_details}\t${confidence}\t\t${RIS1}\t\t${RIS2}\t\t${RIS3}\t\t${RIS4}" >> $classgttie

done < $classtie

# IFS='' ( oppure IFS= ) impedisce che gli spazi bianchi iniziali o finali vengano tagliati
# -r previene che i backslash escape vengano interpretati
# || [[ -n "$LINE" ]]; previene che l'ultima riga venga ignorata se non finisce con \n

# cat legge i file specificati e produce la concatenazione del loro contenuto
# grep cerca in uno o più file di testo le linee che corrispondono ad uno o più modelli specificati e produce un elenco delle linee per cui è stata trovata corrispondenza
# awk estrae il campo di un record specificato
