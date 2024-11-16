start_num=1
end_num=$((start_num + 9))

folder="pe$start_num ~ pe$end_num"
mkdir -p "$folder"

for i in $(seq -f "%02g" $start_num $end_num); do
  mv "pe$i"* "$folder" 2>/dev/null
done

echo "Files for $folder moved successfully!"