# GPTForMe

## Running the app locally

### Install Dependencies

```bash
brew install postgresql@14 pyenv poetry nodejs
```

```bash
pyenv install 3.11.2
source bin/activate
poetry install
poetry run playwright install chromium
```

This step is required even if you set up poetry in PyCharm.

### Set up your databases and environment

1. Run the script to generate the SQL that will create the databases on your local machine. **Note this will remove all local and test data from your Freeplay database**:

    ```bash
    brew services start postgresql@14 
    psql postgres < migrations/drop_and_create_databases.sql
    ```

1. Copy the `.env.example` file into a file called `.env`.
   Be sure to follow this naming convention to ensure secrets are not checked in by git.

    ```bash
    cp .env.example .env
    ```

1. Update this file with the correct environment variables

   * Set up [Stytch environment variables](https://www.notion.so/228labs/Provision-a-Stytch-account-for-local-development-2138d38a06724dc58de4d7cfd0c1ee4f).
   * Add your email address for `DEFAULT_ADMIN_USER_EMAIL_ADDRESSES`, and use this email address to sign in to the app.

1. Source the environment

    ```bash
    source .env
    ```
1. Migrate your databases:

    ```bash
    make migrate
    ```

1. Run tests to ensure database setup is correct:

    ```bash
    make test
    ```

### Run the app

```bash
make run
```

Navigate to [docs/sdk_example.py](docs/sdk_example.py) and hit the green triangle to run the SDK example.

## Running tests

To run the tests from the command line:

```bash
make test
```

## PyCharm
We typically use PyCharm.

We use the EnvFile plugin to source the .env file when running Python scripts. Update your default Python configuration
template to source the .env file before running Python scripts.

## Building React components

React is used in Freeplay Server for rich client experiences that cannot be handled by Flask server-side rendering alone.

This build is not yet automated, the produced files are currently checked-in.

1. Do any code edits in the `web`
1. Run `npm install` in the `web` directory 
1. Run tests with `npm test`
1. Build a new javascript file with `npm run build`

One file is produced:

* `freeplay_server/static/freeplay-react.js`

This file can then be imported as an ESModule in inline javascript on Flask rendered templates. 

## Building web components (deprecated)

*Note: web components are deprecated in favor of React.* 

This build is not yet automated, the produced files are currently checked-in instead.

1. Do any code edits in the `webcomponents`
1. Run tests with `npm run test`
1. Build a new javascript file with `npm run build`

Two files are produced:

* `freeplay_server/static/webcomponents.js`
* `freeplay_server/static/webcomponents.css`

### Web components folder structure

* Config files at the top level.
    * `eslint` for linting of our typescript code (recommended to setup in PyCharm with `run eslint on save`)
    * `package.json` and `lock` for dependencies
    * `tsconfig` for typescript compilation config
    * `vite` is our frontend build system
    * `web-test-runner` is configured here to leverage our build system, vite.
* `index.html` entry point to the build system, loads `main.ts` displays components
    * This can be loaded when running `npm run dev`
* `src/main.ts` needs to load all our components so they are built when running `npm run build`.
* `src/vite-end.d.ts` used by our build system.
* `src/components/*.ts` code for components, loads css files.
* `src/components/*.css` css for individual components.
* `test/components/*.ts` the tests for our components, we use the open web components testing library.

### Useful links and dependencies

* [lit](https://lit.dev), the framework we use for building the web components
* [open web components](https://open-wc.org), where we got our testing framework from
* [vite](https://vitejs.dev), our build system for the frontend
* [python](https://www.python.org/downloads/), runtime for the backend
* [pyenv](https://github.com/pyenv/pyenv), for installing specific versions of Python
* [poetry](https://python-poetry.org/docs/#installation), for dependency and python version management
* [postgres](https://www.postgresql.org/), our datastore
* [nodejs](https://nodejs.org), for building web components from typescript into minified javascript (currently not used
  in the build)


## Building and running a docker container

To build and run the docker container, run:

```bash
make docker/build
```

## Deployment

## FreePlay AI SDK

### Building and Publish SDK

#### Set up Pypi

````
poetry config repositories.testpypi https://test.pypi.org/legacy/

poetry config pypi-token.testpypi your-api-token
poetry config pypi-token.pypi your-api-token
````

#### Testpypi

````
cd freeplay_sdk 
poetry build
poetry publish -r testpypi
````

#### Pypi

````
cd freeplay_sdk
poetry build
poetry publish
````

## We use Alembic for migrations

To make a new migration:
```bash
cd migrations/
poetry run alembic revision -m "[MY REVISION]"
```
Migrations are run automatically for each GCP project when that project is deployed.
