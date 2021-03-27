
action="$1"
mp="$2"
adr="$3"
pwd="$4"

case $action in

	"init")		
		python3 ./init.py "--mp" $mp	
	;;
	
	"get")
		if [ "$adr" = "" ]; then
			echo "Address parameter must be given"
			exit 1
		fi		
		python3 ./get.py "--mp" $mp	"--adr" $adr
	;;
	
	"put")
		if [ "$adr" = "" || "$pwd" = " " ]; then
			echo "Both address parameter and password parameter must be given"
			exit 1
		fi		
		python3 ./put.py "--mp" $mp	"--adr" $adr "--pwd" $pwd
	;;
	
	*)
		echo "Invalid action argument"
	;;

esac


