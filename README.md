### A simple app to process some transaction using kafka and py-flink


### To bring up the dagster serve, un in root mode on Unix Based System

- Install Docker from [here](https://docs.docker.com/get-docker/)

- Navigate to folder `dagster_flows`. Once there run below command

        - you@yourmachine:~/somefolder/dagster_flows$ make build && make up

- You can see the loaded assets at http://localhost:3000/assets/
- To add your custom flows 
    - add your modules in the [dags](/dags) folder
    - update the [workspace.yaml](/dags/workspace.yaml) file


