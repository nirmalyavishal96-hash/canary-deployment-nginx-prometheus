#!/bin/bash

echo "Rolling back to stable (v1 only)..."

cat > nginx/nginx.conf <<EOF
events {}

http {
    upstream backend {
        server 172.17.0.1:8001 weight=10;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}
EOF

docker rm -f nginx-canary

docker run -d -p 8090:80 \
  -v $(pwd)/nginx/nginx.conf:/etc/nginx/nginx.conf \
  --name nginx-canary nginx

echo "Rollback complete"
