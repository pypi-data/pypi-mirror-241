# sky-atc

## Creating a cluster 
Create a cluster with a controller (currently max: 1) and optionally workers (all in a single region).
```
python cli.py create-cluster \
    --region_tag gcp:us-central1-a 
    --controller_instance_type e2-standard-2 \
    --worker_instance_type n1-standard-1 \
    --num_workers 2
```

Add workers with different instance types or from different regions: 
```
python cli.py add-worker --region_tag aws:us-west-1 --worker_instance_type g4dn.xlarge
```

## Deploying an inference service 
Create a deployment with: 
```
kubectl --kubeconfig  ~/.skyatc/skyatc/k3s.yaml apply -f kubernetes/deployment.yml
```
Create a service with: 
```
kubectl --kubeconfig  ~/.skyatc/skyatc/k3s.yaml apply -f kubernetes/service.yml
```
Once created, you can send requests with: 
```
curl http://35.209.44.206:30153/generate \                                                                                     ─╯
-d '{
"prompt": "San Francisco is a",
"use_beam_search": true,
"n": 4,
"temperature": 0
}'

Output: 
{"text":["San Francisco is a pretty of for start, but I I is not a great place to work.","San Francisco is a very city to live in. \nI also a place to\n live.","San Francisco is a great place to live., but it's not the best place to live in","San Francisco is a city that. go and work.  I a for everyone.  work."]}% 
```

## Autoscaler 
The autoscaler is a docker container that runs on the controller node. You can update it with the following: 
```
cd ./cluster
sudo docker build -t sarahwooders/skyatc-autoscaler .
docker push sarahwooders/skyatc-autoscaler:latest
```