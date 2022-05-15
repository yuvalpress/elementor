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
2. Change the namespace variable in the charts/values.yaml file to match the namespace name you created in the first command.
3. Run the following command:
```helm install <chart_name> <path_to_chart_folder> -f <path_to_values_file>```



