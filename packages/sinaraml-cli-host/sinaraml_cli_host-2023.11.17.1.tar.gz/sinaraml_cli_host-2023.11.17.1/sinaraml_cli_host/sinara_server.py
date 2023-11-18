import os
from docker import types
import socket
from .docker_utils import ensure_docker_volume, \
                          docker_volume_remove, \
                          docker_container_create, \
                          docker_container_exists, \
                          docker_container_start, \
                          docker_container_running, \
                          docker_container_stop, \
                          docker_container_remove, \
                          docker_container_exec


class SinaraServer():

    subject = 'server'
    container_name = 'jovyan-single-use'
    sinara_images = ['buslovaev/sinara-notebook', 'buslovaev/sinara-cv']

    @staticmethod
    def add_command_handlers(root_parser):
        parser_server = root_parser.add_parser(SinaraServer.subject, help='sinara server subject')
        server_subparsers = parser_server.add_subparsers(title='action', dest='action', help='Action to do with subject')

        SinaraServer.add_create_handler(server_subparsers)
        SinaraServer.add_start_handler(server_subparsers)
        SinaraServer.add_stop_handler(server_subparsers)
        SinaraServer.add_remove_handler(server_subparsers)

    @staticmethod
    def add_create_handler(root_parser):
        server_create_parser = root_parser.add_parser('create', help='create sinara server')
        server_create_parser.add_argument('--instanceName', default=SinaraServer.container_name, help='sinara server container name (default: %(default)s)')
        server_create_parser.add_argument('--runMode', default='q', choices=["q", "b"], help='Runmode, quick (q) - work, data, tmp will be mounted inside docker volumes, basic (b) - work, data, tmp will be mounted from host folders (default: %(default)s)')
        server_create_parser.add_argument('--createFolders', default='y', choices=["y", "n"], help='y - create work, data, tmp folders in basic mode automatically, n - folders must be created manually (default: %(default)s)')
        server_create_parser.add_argument('--gpuEnabled', choices=["y", "n"], help='y - Enables docker container to use Nvidia GPU, n - disable GPU')
        server_create_parser.add_argument('--memRequest', default='4g', type=str, help='Amount of memory requested for server container (default: %(default)s)')
        server_create_parser.add_argument('--memLimit', default='8g', type=str, help='Maximum amount of memory for server container (default: %(default)s)')
        server_create_parser.add_argument('--cpuLimit', default='4', type=int, help='Number of CPU cores to use for server container (default: %(default)s)')
        server_create_parser.add_argument('--jovyanRootPath', help='Path to parent folder for data, work and tmp (only used in basic mode with createFolders=y)')
        server_create_parser.add_argument('--jovyanDataPath', help='Path to data fodler on host (only used in basic mode)')
        server_create_parser.add_argument('--jovyanWorkPath', help='Path to work folder on host (only used in basic mode)')
        server_create_parser.add_argument('--jovyanTmpPath', help='Path to tmp folder on host (only used in basic mode)')
        server_create_parser.add_argument('--infraName', type=str, help='Infrastructure name to use (default = local_filesystem)')
        server_create_parser.set_defaults(func=SinaraServer.create)

    @staticmethod
    def add_start_handler(root_parser):
        server_start_parser = root_parser.add_parser('start', help='start sinara server')
        server_start_parser.add_argument('--instanceName', default=SinaraServer.container_name, help='sinara server container name (default: %(default)s)')
        server_start_parser.set_defaults(func=SinaraServer.start)

    @staticmethod
    def add_stop_handler(root_parser):
        server_stop_parser = root_parser.add_parser('stop', help='stop sinara server')
        server_stop_parser.add_argument('--instanceName', default=SinaraServer.container_name, help='sinara server container name (default: %(default)s)')
        server_stop_parser.set_defaults(func=SinaraServer.stop)

    @staticmethod
    def add_remove_handler(root_parser):
        server_remove_parser = root_parser.add_parser('remove', help='remove sinara server')
        server_remove_parser.add_argument('--instanceName', default=SinaraServer.container_name, help='sinara server container name (default: %(default)s)')
        server_remove_parser.add_argument('--withVolumes', default='n', choices=["y", "n"], help='y - remove existing data, work, tmp docker volumes, n - keep volumes  (default: %(default)s)')
        server_remove_parser.set_defaults(func=SinaraServer.remove)

    @staticmethod
    def get_free_port(port=8888):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                port += 1
                sock.close()
            else:
                sock.close()
                break
        return port

    @staticmethod
    def create(args):
        def get_opened_ports():
            result = {}
            for port in range(4040, 4061):
                result[str(port)] = str(port)
            host_server_port = str(SinaraServer.get_free_port())
            result['8888'] = host_server_port
            return result

        args_dict = vars(args)
        gpu_requests = []
        sinara_image_num = 1

        if not args.gpuEnabled:
            sinara_image_num = -1
            while sinara_image_num not in [1, 2]:
                try:
                    sinara_image_num = int(input('Please, choose a Sinara for 1) ML or 2) CV projects: '))
                except ValueError:
                    pass
            if sinara_image_num == 2:
                args_dict['gpuEnabled'] = "y"
        
        if args.gpuEnabled == "y":
            gpu_requests = [ types.DeviceRequest(count=-1, capabilities=[['gpu']]) ]

        if not args.infraName:
            infra = input('Please, enter a Sinara infra name (skip to set default infra): ')
            args_dict['infraName'] = 'local_filesystem' if not infra else infra

        sinara_image = SinaraServer.sinara_images[ int(sinara_image_num - 1) ]

        if args.runMode == "q":
            docker_volumes = SinaraServer._prepare_quick_mode(args)
        elif args.runMode == "b":
            docker_volumes = SinaraServer._prepare_basic_mode(args)

        if not docker_container_exists(args.instanceName):

            server_cmd = "start-notebook.sh --ip=0.0.0.0 --port=8888 --NotebookApp.default_url=/lab --NotebookApp.token='' --NotebookApp.password=''"

            docker_container_create(
                image = sinara_image,
                command = server_cmd,
                working_dir = "/home/jovyan/work",
                name = args.instanceName,
                mem_reservation = args.memRequest,
                mem_limit = args.memLimit,
                nano_cpus = 1000000000 * int(args.cpuLimit), # '--cpus' parameter equivalent in python docker client
                shm_size = "512m",
                ports = get_opened_ports(),
                volumes = docker_volumes,
                environment = {
                    "DSML_USER": "jovyan",
                    "JUPYTER_ALLOW_INSECURE_WRITES": "true",
                    "JUPYTER_RUNTIME_DIR": "/tmp",
                    "INFRA_NAME": args.infraName
                },
                device_requests = gpu_requests # '--gpus all' flag equivalent in python docker client
            )
            print("Your jovyan single use container is created")

        elif not docker_container_running(args.instanceName):
            print("Your jovyan single use container is found")
            docker_container_start(args.instanceName)
            print("Started jovyan single use container")

        else:
            print("Your jovyan single use container is already running")

    @staticmethod
    def _prepare_quick_mode(args):
        data_volume = f"jovyan-data-{args.instanceName}"
        work_volume = f"jovyan-work-{args.instanceName}"
        tmp_volume =  f"jovyan-tmp-{args.instanceName}"

        ensure_docker_volume(data_volume, already_exists_msg="Docker volume with jovyan data is found")
        ensure_docker_volume(work_volume, already_exists_msg="Docker volume with jovyan work is found")
        ensure_docker_volume(tmp_volume, already_exists_msg="Docker volume with jovyan tmp data is found")

        return  [f"{data_volume}:/data",
                 f"{work_volume}:/home/jovyan/work",
                 f"{tmp_volume}:/tmp"]

    @staticmethod
    def _prepare_basic_mode(args):
        if args.createFolders == "y":
            if not args.jovyanRootPath:
                jovyan_root_path = input('Please, choose jovyan Root folder path (data, work and tmp will be created there): ')
            
            jovyan_data_path = os.path.join(jovyan_root_path, "data")
            jovyan_work_path = os.path.join(jovyan_root_path, "work")
            jovyan_tmp_path = os.path.join(jovyan_root_path, "tmp")

            print("Creating work folders")
            os.makedirs(jovyan_data_path, exist_ok=True)
            os.makedirs(jovyan_work_path, exist_ok=True)
            os.makedirs(jovyan_tmp_path, exist_ok=True)
        else:
            if not args.jovyanDataPath:
                jovyan_data_path = input("Please, choose jovyan Data path: ")
            if not args.jovyanWorkPath:
                jovyan_work_path = input("Please, choose jovyan Work path: ")
            if not args.jovyanTmpPath:
                jovyan_tmp_path = input("Please, choose jovyan Tmp path: ")

        folders_exist = ''
        while folders_exist not in ["y", "n"]:
            folders_exist = input("Please, ensure that the folders exist (y/n): ")

        if folders_exist == "y":
            print("Trying to run your environment")
        else:
            raise Exception("Sorry, you should prepare the folders beforehand")
        
        return  [f"{jovyan_data_path}:/data",
                 f"{jovyan_work_path}:/home/jovyan/work",
                 f"{jovyan_tmp_path}:/tmp"]

    @staticmethod
    def start(args):
        def prepare_mounted_folders(_instance):
            docker_container_exec(_instance, "chown -R jovyan:users /tmp")
            docker_container_exec(_instance, "chown -R jovyan:users /data")
            docker_container_exec(_instance, "chown -R jovyan:users /home/jovyan/work")
            docker_container_exec(_instance, "rm -rf /tmp/*")

        if not docker_container_exists(args.instanceName):
            raise Exception(f"Your jovyan single use container with name {args.instanceName} doesn't exist")
        docker_container_start(args.instanceName)
        prepare_mounted_folders(args.instanceName)
        print(f'Sinara server {args.instanceName} started\nGo to http://127.0.0.1:8888 to open jupyterlab')

    @staticmethod
    def stop(args):
        if not docker_container_exists(args.instanceName):
            raise Exception(f"Your jovyan single use container with name {args.instanceName} doesn't exist")
        docker_container_stop(args.instanceName)
        print(f'Sinara server {args.instanceName} stopped')

    @staticmethod
    def remove(args):
        if not docker_container_exists(args.instanceName):
            print(f"Your jovyan single use container with name {args.instanceName} has been already removed")
        docker_container_remove(args.instanceName)
        if args.withVolumes == "y":
            print("Removing docker volumes")
            data_volume = f"jovyan-data-{args.instanceName}"
            work_volume = f"jovyan-work-{args.instanceName}"
            tmp_volume =  f"jovyan-tmp-{args.instanceName}"
            docker_volume_remove(data_volume)
            docker_volume_remove(work_volume)
            docker_volume_remove(tmp_volume)
        print(f'Sinara server {args.instanceName} removed')
