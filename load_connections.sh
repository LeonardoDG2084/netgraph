curl -X POST "localhost:9200/tivit/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
   "source_ip" : "1.1.1.1",
   "source_port" : "45345",
   "destination_ip" : "8.8.8.8",
   "destination_port" : "53",
   "status" : "ESTABLISHED"
}'

curl -X POST "localhost:9200/tivit/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
   "source_ip" : "1.1.1.1",
   "source_port" : "45345",
   "destination_ip" : "8.8.8.8",
   "destination_port" : "22",
   "status" : "TIME_WAIT"
}'


curl -X POST "localhost:9200/tivit/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
   "source_ip" : "2.2.2.2",
   "source_port" : "1231",
   "destination_ip" : "10.10.10.10",
   "destination_port" : "22",
   "status" : "TIME_WAIT"
}'
