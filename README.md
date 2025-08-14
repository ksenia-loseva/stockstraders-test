# To run tests:
## Locally:
After cloning project, install requirements:
```shell
pip install -r requirements.txt
```

Create .env file with the following contents:
```.dotenv
EMAIL=<registered user email>
PASSWORD=<registered user password>
```
Run
```shell
pytest
```

If you have allure cli installed, you can then see results after running:
```shell
allure report
allure serve
```

## CI:
Go to Actions page, choose 'Run tests' workflow and click 'Run workflow'.

Wait for workflow to finish. If any tests fail, you can then download a zip archive with screenshots of failed tests.

Right now, CI run fails since the site asks for identity confirmation — the behavior which is not consistent with 
how the test runs locally on my computer. Since I cannot reproduce the behavior, I can't describe locators of the confirmation
form inputs and pass the test. This behavior would probably be more consistent and reproducible on test environments, so
I opted out of trying to fix something that wouldn't be a problem.

Since Allure for pytest doesn't allow masking secrets and passwords if they are passed to a function, 
I have not included generating allure report as a test artifact. This also wouldn't be a problem on test env in a protected
environment.

See https://github.com/allure-framework/allure-python/issues/805.