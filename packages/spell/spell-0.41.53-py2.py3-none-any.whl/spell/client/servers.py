from spell.client.model import SpellModel
from spell.client.models import ModelVersion

from spell.api.models import (
    BatchingConfig,
    ModelServerCreateRequest,
    Environment,
    Repository
)

from spell.client.utils import get_pip_conda_dependencies

from spell.cli.utils.parse_utils import get_name_and_tag, parse_tag


class ModelServersService:
    """A class for managing Spell model servers."""

    def __init__(self, client):
        self.client = client

    def list(self):
        """Lists model servers.

        Parameters:
            name (str): Model server name

        Returns:
            A :obj:`list` of :py:class:`SpellModelServer` objects.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        model_servers = self.client.api.get_model_servers()
        model_servers = [ModelServer(self.client.api, server) for server in model_servers]
        return model_servers

    def get(self, name):
        """Get a model server.

        Parameters:
            name (str): model server name

        Returns:
            A :py:class:`SpellModelServer`.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        model_server = self.client.api.get_model_server(name)
        return ModelServer(self.client.api, model_server)

    def rm(self, name):
        """Remove a model server.

        Parameters:
            name (str): Model server name

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self.client.api.delete_model_server(name)

    def serve(
        self,
        model,
        entrypoint,
        github_url,
        **kwargs
    ):
        """
        Create a new model server using a model.

        Parameters:
            model (str): Targeted model, should be in MODEL:VERSION format
            entrypoint (str): Path to the file to be used as the model server entrypoint, e.g.
                `serve.py` or similar.
            github_url (str): a GitHub URL to a repository for code to include in the server.
            github_ref (str, optional): a reference to a commit, branch, or tag in the repository
                corresponding to :obj:`github_url` for code to include in the run
                (default: master).
            commit_ref (str, optional): git commit hash to use (default: HEAD).
            name (str, optional): Name of the model server. Defaults to the model name.
            node_group (str, optional): Name of the node group to serve from. Defaults to the
                default node group.
            classname (str, optional): Name of the `Predictor` class. Only required if more than
                one predictor exists in the entrypoint.
            pip_packages (:obj:`list` of :obj:`str`, optional): pip dependencies (default: None).
                For example: ``["moviepy", "scikit-image"]``.
            apt_packages (:obj:`list` of :obj:`str`, optional): apt dependencies (default: None).
                For example: ``["python-tk", "ffmpeg"]``
            conda_file (str, optional): a path to a conda file.
            requirements_file (str, optional): a path to a requirements file
            envvars (:obj:`dict` of :obj:`str` -> :obj:`str`, optional): name to value mapping of
            environment variables for the server (default: None).
            attached_resources (:obj:`dict` of :obj:`str` -> :obj:`str`, optional): resource name
                to mountpoint mapping of attached resouces for the run (default: None). For
                example: ``{"runs/42" : "/mnt/data"}``
            resource_requirements (:obj:`dict` of :obj:`str` -> :obj:`str`, optional):
            configuration mapping for node resource requirements: CPU, GPU, RAM, etcetera.
                Has sane default values.
            num_processes (:obj:`int`): The number of processes to run the model server on. By
                default this is (2 * numberOfCores) + 1 or equal to the available GPUs if
                applicable.
            pod_autoscale_config (:obj:`dict` of :obj:`str` -> :obj:`str`, optional):
                configuration mapping for pod autoscaling: min pods, max pods, and target requests
                per second. Has sane default values.
            enable_batching (:obj:`bool`, optional): Whether or not to enable model server
                batching. Defaults to False.
            batching_config (:obj:`dict` of :obj:`str` -> :obj:`str`, optional): If model server
                batching is enabled, the values passed to this parameter are used to configure it.
                If left empty, the default batching parameter values will be used.
            description: (:obj:`str`, optional): Model server description, defaults to none.
            debug (:obj:`bool`, optional): Launches the model server in debug mode. Should not be
                used in production.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        model_name, model_tag = get_name_and_tag(model)
        if model_tag is None:
            raise ValueError(f"Model parameter value {model} must be in MODEL:VERSION format.")
        model_version_id, model_version_name = parse_tag(model_tag)

        server_name = kwargs.get("name", model_name)

        pip, conda_file = get_pip_conda_dependencies(kwargs)
        create_request_environment = Environment(
            apt=kwargs.get("apt_packages", None),
            pip=pip,
            conda_file=conda_file,
            env_vars=kwargs.get("envvars", None)
        )

        # TODO: refactor to obviate the need to import from the spell.cli path.
        from spell.cli.commands.server import (
            create_pod_autoscale_config, create_resource_requirements
        )
        pod_autoscale_config = kwargs.get("pod_autoscale_config", {})
        pod_autoscale_config = create_pod_autoscale_config(
            pod_autoscale_config.get("min_pods", None),
            pod_autoscale_config.get("max_pods", None),
            pod_autoscale_config.get("target_cpu_utilization", None),
            pod_autoscale_config.get("target_requests_per_second", None)
        )
        resource_requirements = kwargs.get("resource_requirements", {})
        resource_requirements = create_resource_requirements(
            resource_requirements.get("ram_request", None),
            resource_requirements.get("cpu_request", None),
            resource_requirements.get("ram_limit", None),
            resource_requirements.get("cpu_limit", None),
            resource_requirements.get("gpu_limit", None),
        )

        if kwargs.get("enable_batching", False):
            batching_config = kwargs.get("batching_config", {})
            batching_config = BatchingConfig(
                max_batch_size=batching_config.get(
                    "max_batch_size",
                    BatchingConfig.DEFAULT_MAX_BATCH_SIZE
                ),
                request_timeout_ms=batching_config.get(
                    "request_timeout",
                    BatchingConfig.DEFAULT_REQUEST_TIMEOUT
                )
            )
        else:
            batching_config = BatchingConfig(is_enabled=False)

        repository = Repository(
            github_url=github_url,
            commit_hash=kwargs.get("commit_hash", "HEAD"),
            github_ref=kwargs.get("github_ref", None)
        )

        create_request = ModelServerCreateRequest(
            entrypoint,
            model_name,
            server_name,
            model_version_id=model_version_id,
            model_version_name=model_version_name,
            repository=repository,
            environment=create_request_environment,
            batching_config=batching_config,
            predictor_class=kwargs.get("classname", None),
            node_group=kwargs.get("node_group", None),
            description=kwargs.get("description", None),
            attached_resources=kwargs.get("attached_resources", None),
            pod_autoscale_config=kwargs.get("pod_autoscale_config", None),
            resource_requirements=kwargs.get("resource_requirements", None),
            num_processes=kwargs.get("num_processes", None),
            debug=kwargs.get("debug", False)
        )
        self.client.api.new_model_server(create_request)


class ModelServer(SpellModel):
    """Object representing a Spell model server.

    Attributes:
        id (int): Model server id
        server_name (str): Model server name
        status (str): Model server status (e.g. `Running`, `Stopped`)
        url (str): Model server endpoint URL
        created_at (datetime.datetime): Model server creation timestamp
        updated_at (datetime.datetime): Timestamp for the last time an action was performed on
            this server.
        cluster (dict): Model serving cluster configuration details such as provider, region,
            subnet, and cloud provider credentials.
        model_version (ModelVersion): A py:class:`ModelVersion` object containing information on
            the model being served. See the corresponding docs for more information.
        entrypoint (str): The model server entrypoint (e.g. `serve.py`).
        workspace (dict): Details describing the git repository the model server was launched
            from.
        git_commit_hash (str): Commit hash fingerprinting the version of the code this server
            is running.
        pods (list of ModelServerPod): Lists current and historic Kubernetes pods that served or
            are serving this server.
        creator (User): The Spell user who created this model server initially.
        resource_requirements (ContainerResourceRequirements): The resource requirements and
            limits currently set for this model server. To learn more refer to the model server
            documentation.
        pod_autoscale_config (PodAutoscaleConfig): Model server performance configuration values:
            min pods, max pods, and target requests per second per pod.
        additional_resources (list of Resource): Lists additional files (besides the model)
            attached to this model server.
        batching_config (BatchingConfig): Batching configuration details. Refer to the
            corresponding section of the docs for more information.
        environment (Environment): All additional `pip`, `apt`, and `conda` dependencies installed
            onto this model server.
    """

    model = "model_server"

    def __init__(self, api, model_server):
        self._api = api
        self.__set_from_model_server_object(api, model_server)

    def __set_from_model_server_object(self, api, model_server):
        model_server.model_version = ModelVersion(api, model_server.model_version)
        self.model_server = model_server

    def stop(self):
        """Stops the model server.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self._api.stop_model_server(self.model_server.server_name)

    def start(self):
        """Starts the model server.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self._api.start_model_server(self.model_server.server_name)
