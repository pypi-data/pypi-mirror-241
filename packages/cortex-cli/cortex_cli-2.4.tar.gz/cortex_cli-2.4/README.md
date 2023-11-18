<p align="center">
    <img src="https://www.nearlyhuman.ai/wp-content/uploads/2022/04/virtual-copy.svg" width="200"/>
</p>

# Nearly Human Cortex CLI

A simple CLI that abstracts the Cortex API. The application should reflect all of the Cortex routes, and provide a way
to interact with models within an approved client.

## Prerequisites

- Mamba
- Create a github token with repo permissions and set the `GH_TOKEN` environment variable

## Build

```bash
mamba env create -f ./conda.yml

# Build version of Nearly Human Cortex CLI for release
python -m build
```

## Installing the CLI

```bash
mamba create -n cortex_cli python=3.10 pip -c conda-forge
mamba activate cortex_cli
pip install cortex-cli
```

## Running the CLI

```bash
mamba activate cortex_cli
cortex-cli [resource] [action] [parameters ...]
```

Resources include configure, clients, models, pipelines, and inferences.
Actions include get, list, and create.
Parameters are action+resource specific.

### Configure

The profile for the CLI must be configured before use. An API key needs to be generated from the Settings page in the Cortex UI.

```bash
$ cortex-cli configure
Profile [default]:
API Url [https://api.nearlyhuman.ai]:
API Key []: nh_asdfasdfasdf1341234
```

### Client

#### Get a List of Clients

The registered profile may only associate with one client. The get command returns information about their client license, profile, and name.

```bash
$ cortex-cli clients get

[{'_id': '6317eceaeef27d972e86b4ff',
  'clientKey': 'demo',
  'createdDate': '2022-09-07T00:59:22.582Z',
  'description': 'The Cortex Demo Client',
  'experimentId': '1',
  'licensePlan': 'enterprise',
  'name': 'Demo',
  'supportEmail': 'karl.haviland@nearlyhuman.ai',
  'supportPhone': '717-111-2222',
  'updatedDate': '2022-09-07T00:59:22.582Z',
  'website': 'https://www.nearlhuman.ai'}]
```

### Models

#### Initialize a New Model

_NOTE:_ Only needed if you want to both create a brand new Cortex ready model and automatically register it with the server. Start from the workspace directory where the model repo is going to be created locally.

```bash
$ cortex-cli models init -n my-demo-name
```

#### Register a Model\*

_NOTE:_ Only needed if you have an existing Cortex Github repository and you want to register it with the server. First, cd to the model's local directory.

```bash
$ cortex-cli models register -n "My Demo Model" -r my-demo-name
```

#### Get a List of Models

```bash
$ cortex-cli models list

[{'_id': '632b32731d2faa4ffbade76d',
  'clientKey': 'demo',
  'createdDate': '2022-09-20T15:49:06.882Z',
  'description': 'A model that is initialized through the Cortex CLI.',
  'experimentId': '1',
  'name': 'nmci-chat-2',
  'organization': 'nearlyhuman',
  'repo': 'nmci-chat-2',
  'tags': [],
  'updatedDate': '2022-09-20T15:49:06.882Z'},
 {'_id': '632b43fd1d2faa4ffbade771',
  'clientKey': 'demo',
  'createdDate': '2022-09-21T17:03:57.365Z',
  'description': 'A model that is initialized through the Cortex CLI.',
  'experimentId': '1',
  'name': 'nmci-chat-3',
  'organization': 'nearlyhuman',
  'repo': 'nmci-chat-3',
  'tags': [],
  'updatedDate': '2022-09-21T17:03:57.365Z'},
 ...
 ]
```

#### Get a Model By ID

```bash
$ cortex-cli models get -i 632b32731d2faa4ffbade76d
{'_id': '632b32731d2faa4ffbade76d',
 'clientKey': 'demo',
 'createdDate': '2022-09-20T15:49:06.882Z',
 'description': 'A model that is initialized through the Cortex CLI.',
 'experimentId': '1',
 'name': 'nmci-chat-2',
 'organization': 'nearlyhuman',
 'repo': 'nmci-chat-2',
 'tags': [],
 'updatedDate': '2022-09-20T15:49:06.882Z'}
```

#### Run a Model's Pipeline

_NOTE:_ First, cd to the model's local directory. The `-t False` flag is optional and can be used to turn off tracking against the Cortex server. Otherwise it will always appear on the Cortex dashboard UI.
A pipeline is a series of steps that the model performs to transform and validate data, train, and store the model artifact. This pipeline displays in the
Cortex UI where it can be deployed. The steps that define the pipeline are located in the

```bash
$ cortex-cli models run
   + Found the model financialchat
   + Did not find existing pipeline for branch main
   + Pipeline Pending with id: 642c68841368f765a05fdb38
                Loading module financialchat from ./src/financialchat/financialchat.py
   + Loaded pipeline steps
   + Download data completed successfully
   + Fit model completed successfully
   + Evaluate model completed successfully
   + Cleanup model params completed successfully
   > Saving pipeline artifacts...
   + Saved the pipeline artifacts to disk: (models/cortex/642c68841368f765a05fdb38)
   > Packing conda environment...
Collecting packages...
Packing environment at '/home/user/mambaforge/envs/financial_chat' to 'models/cortex/642c68841368f765a05fdb38/environment.tar.gz'
[########################################] | 100% Completed | 13.7s
   + Packed conda environment to disk: (models/cortex/642c68841368f765a05fdb38)
   > Uploading pipeline artifacts to Cortex...
   + Uploaded the pipeline artifacts to Cortex
   + Completed Cortex Pipeline Run
```

### Pipelines

#### Get a List of Pipelines

```bash
$ cortex-cli pipelines list

```

#### Get a Pipeline by ID

```bash
$ cortex-cli pipelines get -i 134123413412341234

```

#### Deploy a Pipeline

```bash
$ cortex-cli pipelines deploy -i 134123413412341234

```

#### Undeploy a Pipeline

```bash
$ cortex-cli pipelines undeploy -i 134123413412341234

```

### Inferences

#### Get a List of Inferences

```bash
$ cortex-cli inferences list

```

#### Get an Inference by ID

```bash
$ cortex-cli inferences get -i 134123413412341234

```
