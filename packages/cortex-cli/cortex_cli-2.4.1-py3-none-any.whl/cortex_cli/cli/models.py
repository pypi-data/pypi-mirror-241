from cookiecutter.main import cookiecutter
import plumbum.cli
import requests
from collections import namedtuple
import cortex_cli.cli.api.github_api as gh

import traceback
import os
import os.path
import yaml
import sys
import os
import importlib
from datetime import datetime
from os import walk

from cortex_container_tools.util.models import Trainer
from cortex_cli.cli.cli_api_base import CliApiBase

from cortex_cli import __version__


class ModelsCli(plumbum.cli.Application):
    NAME = 'models'


@ModelsCli.subcommand('init')
class InitModel(CliApiBase):
    MODEL_TEMPLATES_PATH = 'model_templates'
    MODEL_TEMPLATES = [
        'digits',
        'chatgpt'
    ]


    _name = plumbum.cli.SwitchAttr(
        names=['-n', '--name'],
        argtype=str,
        help='The name of the model. Should use a readable format, ie. Digits Model',
        default=None
    )

    _repo = plumbum.cli.SwitchAttr(
        names=['-r', '--repo'],
        argtype=str,
        help='The name of the repository. Should use dash case, ie. digits-model',
        mandatory=True
    )

    _description = plumbum.cli.SwitchAttr(
        names=['-d', '--description'],
        argtype=str,
        default='A model that is initialized through the Cortex CLI.',
        help='A description of the model'
    )

    _template = plumbum.cli.SwitchAttr(
        names=['-t', '--template'],
        argtype=str,
        default='digits',
        help='The template to use for the model. The default is "digits".\nAvailable choices are: ' + ', '.join(MODEL_TEMPLATES),
    )

    _token = plumbum.cli.SwitchAttr(
        names=['--github-token'],
        argtype=str,
        envname='GH_TOKEN'
    )

    _org = plumbum.cli.SwitchAttr(
        names=['--github-org'],
        argtype=str,
        envname='GH_ORG',
        default='nearlyhuman'
    )

    _path = plumbum.cli.SwitchAttr(
        names=['-p', '--path'],
        argtype=str,
        envname='MODEL_PATH',
        default='.'
    )

    _register = plumbum.cli.Flag(
        names=["--register"],
        default=True
    )

    # Properties

    @property
    def _template_location(self):
        current = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        template_path = os.path.join(current, self.MODEL_TEMPLATES_PATH)
        return os.path.join(template_path, f'{self._template}_model')

    @property
    def _model_path(self):
        return os.path.join(self._path, self._repo)


    def main(self, *args):
        self._error_message = None

        # Instantiate the model name if it hasn't been set.
        if not self._name:
            self._name = self._repo.replace('-', ' ').title()

        github = gh.Github(
            self._repo,
            self._description,
            # TODO: Need to separate out this organization because the GH account can be from anywhere.
            self._org,
            self._token
        )

        try:
            self._validate_repo()
            self._generate_template_repo()

            # Create the repository in Github
            self._create_repo(github)

            # Register the model with Cortex
            self._register_model()
        except Exception as e:
            self._fail(e)
            self._error_message = e
        finally:
            if not self._error_message:
                self._pass(f'Successfully generated the model repository at "{self._model_path}"')
        return


    def _validate_repo(self):
        if os.path.exists(self._model_path):
            raise Exception(f'The directory "{self._model_path}" already exists. Either rename the directory or register the repository directly.')


    def _generate_template_repo(self):
        cookiecutter(
            self._template_location,
            no_input=True,
            output_dir=self._path,
            extra_context={
                'model_name': self._name,
                'model_repo': gh.Repo().repo,
                'description': self._description,
                'version': __version__
            }
        )


    def _create_repo(self, github):
        if self._token:
            try:
                # Create the repository in Github
                response = self._handle_api_response(gh.create_repo(github))

                # Commit and push to the new repo in Github
                repo = gh.Repo(path=self._model_path)
                repo.init() \
                    .set_remote(github.owner, github.repo_name) \
                    .add() \
                    .commit('Initial commit. Generated from Cortex CLI using the model template.') \
                    .push()

                self._pass(
                    f'Created the GitHub repository "{self._org}/{self._repo}"')
                return response
            except Exception as e:
                raise Exception(f'An error occurred while initializing the GitHub repo.\n{e}')


    def _register_model(self):
        if self._register:
            response = requests.post(
                url=self._endpoint,
                headers=self._headers,
                json={
                    'name': self._name,
                    'repo': self._repo,
                    'githubEnabled': True if self._token else False
                }
            )

            self._handle_api_response(
                response, f'Registered the model repository {response.json()["_id"]}')


@ModelsCli.subcommand('register')
class RegisterModel(CliApiBase):
    _repo = plumbum.cli.SwitchAttr(
        names=['-r', '--repo'],
        argtype=str,
        mandatory=True
    )

    _name = plumbum.cli.SwitchAttr(
        names=['-n', '--name'],
        argtype=str,
        mandatory=True
    )


    def main(self, *args):
        try:
            response = self._register_model()
            self._print(response)
        except Exception as e:
            self._fail(e)


    def _register_model(self):
        return self._handle_api_response(requests.post(
            url=self._endpoint,
            headers=self._headers,
            json={
                'name': self._name,
                'repo': self._repo,
                'githubEnabled': True if gh.Repo().hash else False
            }
        ))


@ModelsCli.subcommand('run')
class RunModelPipeline(CliApiBase):
    _path = plumbum.cli.SwitchAttr(
        names=['-p', '--path'],
        argtype=str,
        envname='MODEL_PATH',
        default='.'
    )

    _tracking = plumbum.cli.Flag(
        names=['-t', '--tracking'],
        default=True
    )

    _running_pipeline_id = plumbum.cli.SwitchAttr(
        names=['-i', '--pipeline-id'],
        argtype=str,
        envname='NH_PIPELINE_ID',
        default=None
    )

    _verbose = plumbum.cli.SwitchAttr(
        names=['-v', '--verbose'],
        argtype=bool,
        envname='CORTEX_VERBOSE',
        default=False
    )

# -------------------------------------------------------------------------------

    def main(self, *args):
        # Run trainer
        trainer = Trainer(
            use_tracking=self._tracking, 
            pipeline_id=self._running_pipeline_id, 
            verbose=self._verbose
        ).from_file(self._path)

        try:
            trainer.run()
        except Exception as e:
            print(e)
