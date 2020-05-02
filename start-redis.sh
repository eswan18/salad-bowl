REPO_LOCATION="/Users/eswan18/Develop/salad-bowl"

docker run --name salad-bowl-redis -d -v "$REPO_LOCATION/redis_data:/data" redis:latest redis-server --appendonly yes
