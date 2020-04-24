# insert codecov badge here
# TODO DEV: Rename to the name of your service.
Pinecone Service Template

### Getting started
Be sure to install the git hooks after cloning the repo.
```
pipenv install --dev
pipenv shell
cd config
pre-commit install
pre-commit install -t prepare-commit-msg
pre-commit install -t pre-push
```


### Unit Test Coverage
This template includes some sample Pinecone models and tests for them. The coverage for these models is 100%.
You can get a report of the coverage at any time by invoking `tox -e test-unit-coverage` from the command line.

You can also get a html view of the coverage by running `tox -e test-unit-html-coverage`. It will create a static
"website" that you can browse by opening up the index.html file within the htmlcov directory. This is quite useful for
visually determining uncovered lines of code.


### Deploying
#### install plugins
```
npm i
```
#### deploy
`please see the documentation here for use with RL Tool: https://ridgelineapps.atlassian.net/wiki/spaces/PE/pages/148865282/DevOps+Deployment+Tool+Home+Rl-Tool `

### Reset the Pipenv
```
pipenv uninstall --all
pipenv lock --clear
pipenv install --dev
```
