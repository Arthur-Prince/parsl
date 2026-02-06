from parsl.config import Config
from parsl.data_provider.file_noop import NoOpFileStaging
from parsl.data_provider.ftp import FTPInTaskStaging
from parsl.data_provider.http import HTTPInTaskStaging
from parsl.executors.taskvine import TaskVineExecutor, TaskVineManagerConfig
from parsl.executors import WorkQueueExecutor
from parsl.executors.threads import ThreadPoolExecutor
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SimpleLauncher
from parsl.providers import LocalProvider



from parsl.config import Config
from parsl.executors.taskvine import TaskVineExecutor, TaskVineManagerConfig
from parsl.executors import WorkQueueExecutor, HighThroughputExecutor
from parsl.executors.threads import ThreadPoolExecutor
from parsl.launchers import SimpleLauncher
from parsl.providers import LocalProvider


def fresh_config():
    return Config(
        executors=[
            ThreadPoolExecutor(
                label="threads",
            ),
            TaskVineExecutor(
                label="taskvine",
                manager_config=TaskVineManagerConfig(port=9000),
                worker_launch_method="provider",
            ),
            WorkQueueExecutor(
                label="workqueue",
                port=9001,
                coprocess=True,
            ),
            HighThroughputExecutor(
                label="htex_local",
                loopback_address="::1",
                worker_debug=True,
                cores_per_worker=1,
                encrypted=True,
                provider=LocalProvider(
                    init_blocks=1,
                    max_blocks=1,
                    launcher=SimpleLauncher(),
                ),
            )
        ],
        strategy="none",
    )

