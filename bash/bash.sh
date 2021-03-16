set -o nounset
printf "Input time in seconds: "
read t
for ((i=0;i<${#t};i++));do
	if ! [[ ${t:$i:1} =~ [0-9] ]]; then
		echo "No se ha ingresado un número"
		exit 1
	fi
done
echo $(expr $t / 60}):$(expr $t % 60)
