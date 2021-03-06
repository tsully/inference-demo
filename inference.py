import json
import os.path
from os import path

with open('package.json') as json_file:
    data = json.load(json_file)
    test_script = data['scripts']['test'].strip()

    if path.isfile('yarn.lock') == True:
        package_manager = 'yarn'
    else:
        package_manager = 'npm'
    
    config = f'''
version: 2.1
orbs:
  node: circleci/node@4.1.0
jobs:
  test:
    docker:
      - image: cimg/node:12.20.0
    steps:
      - checkout
      - node/install-packages:
          pkg-manager: {package_manager}
      - run:
          command: {package_manager} test
          name: {package_manager} test
workflows:
  node-tests:
    jobs:
      - test        
        '''
print("Writing config \n" + config)
with open('.circleci/continue-config.yml', 'w') as fp:
    fp.write(config)