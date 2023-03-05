FROM python:3.10-slim

# Install Java
RUN apt-get update && apt-get install -y default-jre 
RUN apt-get install -y tree vim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy dag modules
COPY dags ./dags
WORKDIR /dags
ENV DAGSTER_HOME=/dags


CMD ["dagit", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]
