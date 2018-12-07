#!/usr/bin/env bash
read -p "Please set image tag:" tag
echo create docker image hyman-web:${tag}
docker build -t hyman-web:${tag} /opt/case/stress-test/web
docker tag hyman-web:${tag} 10.10.65.200/hyman/hyman-web:${tag}
docker push 10.10.65.200/hyman/hyman-web:${tag}
typeset -u yn
read -p "Please set tag latest and push registry(y/N)?" yn
if [[ ${yn} == Y ]]; then
    echo push latest registry!
    docker tag hyman-web:${tag} hyman-web:latest
    docker tag hyman-web:${tag} 10.10.65.200/hyman/hyman-web:latest
    docker push 10.10.65.200/hyman/hyman-web:latest
fi
