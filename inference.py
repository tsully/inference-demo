
# Get the Package.json file
# Parse the package.json
# Find the user's test command
# If the user is using yarn, use generated config with node orb commands
# If user is using npm, use node orb job
import json

with open('package.json') as json_file:
    data = json.load(json_file)
    test_script = data['scripts']['test'].strip()
    if test_script.find('yarn ') == 0:
        config = '''
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
          pkg-manager: yarn
      - run:
          command: yarn run test
          name: Run YARN tests
workflows:
  node-tests:
    jobs:
      - test
        
        '''
    else:
        config = '''
version: 2.1
orbs:
  node: circleci/node@3.0.0
workflows:
  node-tests:
    jobs:
      - node/test

        '''
with open('.circleci/continue-config.yml', 'w') as fp:
    fp.write(config)
