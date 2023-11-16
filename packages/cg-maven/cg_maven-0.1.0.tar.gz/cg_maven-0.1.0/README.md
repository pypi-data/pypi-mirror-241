# Maven
Maven: _"one who is experienced or knowledgeable."_

This repository holds the software interacting with the maven database. Maven is currently a work in progress.

## Aims

The maven database will be used to store quality metrics for cases and their analysis that come through Clinical Genomics.

## Developing Maven

Steps to start developing on Maven locally:
1. Clone the repo
   ```shell
   git clone https://github.com/Clinical-Genomics/maven
   ```
2. Create a working environment 
   - Requires poetry to be installed: https://python-poetry.org/docs/

2a. Create a virtual python environment in the directory
   ```shell
   # Go into the directory
   cd ./maven
   # Create a virtual environment
   python3 -m venv maven
   # Activate the virtual environment
   source venv/bin/activate
   # Install packages
   poetry install
   ```
2b. If you are using pycharm setup a `poetry interpreter`
   - https://www.jetbrains.com/help/pycharm/poetry.html#poetry-pyproject

3. Install a mongodb client locally (for now) follow steps outlined here
    - https://www.mongodb.com/docs/v7.0/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition
4. Start a mongo server locally that runs the database
   ```shell
      brew services start mongodb-community@7.0
   ```
      - to stop the service when wanted
   ```shell
   brew services stop mongodb-community@7.0
   ```

5. To establish a connection to the database with FastApi and uvicorn run:
```shell
python3 -m uvicorn --reload --app-dir ./api main:app
```
   - If this step worked you should see "Connected to database." in the terminal

6. To view the database in Compass
    - https://www.mongodb.com/products/tools/compass
    - Setup a connection to the localhost
    - Create a new database called "maven"

7. Alternatively to the steps above one can also run maven using docker
   7a. Install docker and start the docker application: https://docs.docker.com/engine/install/ 
      - After step 1
      ```shell
      cd ./maven
      docker compose up
      ```