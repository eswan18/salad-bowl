REPO_LOCATION="/Users/eswan18/Develop/salad-bowl/back-end"

docker run --name salad-bowl-redis -d --rm -p 6379:6379 -v "$REPO_LOCATION/redis_data:/data" redis:latest redis-server --appendonly yes
