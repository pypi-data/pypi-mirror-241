# dummy_app

# Planning
  - Create model train + score api -- done
  - Write training/test data to db -- done
      - update model train to read database -- done
          - to do:  need to figure how to pass large datasets through api - jsonify?
  - create dash app that can visualise -- done
      - train/test data scatter plot with linear model predictions
      - return predictions
          - to do: update to make prettier and include time stamps etc.....
  - stand up ci/cd practices - done
      - set up git hooks - done
          - linting pre-hooks?
          - pytest unit tests?
      - github actions - done
          - Steps
          - build simple tests
          - run on github actions on push
  - create docker file that can run and query data -- done
      - docker to create and publish dockerfile?
  - Package pipeline - done
    - Test building + importing package
    - wrap testing function and running locally?
    - Publish package?
  - Convert env to poetry - done
  - host App + serve dataset on cloud platform
      - Get app to deploy to hosted service
        - how to connect api to app -- done
            - Update Docker App 
                - use Gunicorn
                - Run API + App in same env -- done
                    -  https://docs.docker.com/config/containers/multi-service_container/
      - Get deployment to use package
      - Connect deployments to github actions
      
  
# Useful code
```
# Run app
python  dummy_app/model_api_v2.py & 
sleep 5 
python dummy_app/app.py

# Docker commands
docker ps
docker run -d -it flask-api-image bash
docker exec -it ubuntu bash
docker exec -it flask-api-image bash
docker exec -it <container id or name> bash

# Other 
docker-compose down  # Stop container on current dir if there is a docker-compose.yml
docker rm -fv $(docker ps -aq)  # Remove all containers
sudo lsof -i -P -n | grep 8000 # List who's using the port
sudo lsof -i -P -n | grep python 

# Kill jobs
sudo lsof -i -P -n | grep python 
sudo lsof -i -P -n | grep python | awk '{print $2}'
sudo lsof -i -P -n | grep python | awk '{print $2}' | xargs sudo kill -9 
```
