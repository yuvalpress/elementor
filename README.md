# Rick And Morty Exercise

## The Application:
The application itself is a Flask API server which exposes port 8080 and allows the following methods to be performed:
1. Using the */healthcheck* endpoint, the end user can check if the API is active.
2. Using the */fetch* endpoint, the end user can get the json which was fetched from the rickandmorty API.
3. Using the */download_csv* endpoint, the end user can download the generated CSV file for self use.

## Build the Docker Image:
To build and run the docker image, use the following commands:
1. ```docker build -t <image_name> <path_to_Dockerfile>```
2. ```docker run -d -p 8080:8080 --name <name_of_container> <image_name>```

## Deploy HELM Chart
1. run the command ```kubectl create namespace <name_of_namespace>```
2. Change the namespace variable in the charts/rickmorty/values.yaml file to match the namespace name you created in the first command.
3. Run the following command:
```helm install <chart_name> <path_to_chart_folder> -f <path_to_values_file>```

## Git Actions Pipeline
The pipeline is built with 2 jobs:
1. Build the docker image (using secrets stored in the github project)
2. Create a kubernetes test cluster, deploy the chart and check if the /healthcheck path exposed by the flask app is available.

The kubernetes cluster is deployed using "kind" cluster.
The helm installation is made using port-forwarding.
The check itself is performed if 



