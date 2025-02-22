# Stock-Analysis
It fetches the stock market data of each day. And help you analyze the Stock Market data. 


# DB SETUP via docker (Setup verified on windows)
# 1 -> Install Docker Desktop
# 2 -> Verify installation using this command
       "docker --version"
# 3 -> Run this Download the official ClickHouse image from Docker Hub
       "docker pull clickhouse/clickhouse-server"
# 4 -> Run this command to start the server 
       "docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 --ulimit nofile=262144:262144 -e CLICKHOUSE_USER=<user_name> -e CLICKHOUSE_PASSWORD=<password> clickhouse/clickhouse-server"
# 5 -> JDBC Connection string will be 
       "jdbc:clickhouse://localhost:8123?user=<user_name>&password=<password>"
# 6 -> Run this command to open client (Optionally you can create tables/databases etc here)
       "docker exec -it clickhouse-server clickhouse-client"
# 7 -> Sample queries that you can use
       "CREATE DATABASE <db_name>;" => For creating a DB
       "USE <db_name>;" => To select a DB

