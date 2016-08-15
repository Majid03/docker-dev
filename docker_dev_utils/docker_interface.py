from docker_dev_utils.subprocess import run_command
from yaml import safe_load as yaml_deserialize


def run_docker_compose_subcommand(
    subcommand_name,
    subcommand_args,
    docker_compose_file_path,
    project_name
):
    project_file_arg = '--file={}'.format(docker_compose_file_path)
    command_args = [project_file_arg, subcommand_name] + subcommand_args
    command_environ = {'COMPOSE_PROJECT_NAME': project_name}
    output = run_command('docker-compose', command_args, command_environ)
    return output


def get_docker_compose_config(docker_compose_file_path, project_name):
    docker_compose_config_yaml = run_docker_compose_subcommand(
        'config',
        [],
        docker_compose_file_path,
        project_name,
    )
    docker_compose_config = yaml_deserialize(docker_compose_config_yaml)
    return docker_compose_config


def run_docker_subcommand(subcommand_name, subcommand_args):
    command_args = [subcommand_name] + subcommand_args
    output = run_command('docker', command_args)
    return output
