
import datetime
import os


class DockerCommand:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class DockerEmulator:
    def __init__(self):
        self.images = {}
        self.containers = {}
        self.networks = {}
        self.volumes = {}
        self.services = {}
        self.secrets = {}

    def show_help(self):
        """
        Выводит справку по доступным командам.
        """
        print("Доступные команды:")
        print("help - выводит эту справку.")
        print("docker pull <имя_образа> - скачивает образ Docker.")
        print("docker images - показывает список доступных образов.")
        print("docker run <имя_образа> - запускает контейнер из образа.")
        print("docker ps - показывает список запущенных контейнеров.")
        print("docker ps -a - показывает список всех контейнеров.")
        print("docker stop <имя_контейнера> - останавливает контейнер.")
        print("docker rm <имя_контейнера> - удаляет контейнер.")
        print("docker network create <имя_сети> - создает сеть Docker.")
        print("docker network ls - показывает список сетей Docker.")
        print("docker exec -it <имя_контейнера> <команда> - выполняет команду в контейнере.")
        print("docker build -t <имя_образа> <путь_к_контексту> - строит образ Docker.")
        print("docker push <имя_образа> - отправляет образ в репозиторий.")
        print("docker pull <имя_образа> - скачивает образ из репозитория.")
        print("docker login - авторизуется в репозитории.")
        print("docker logout - выходит из репозитория.")
        print("docker version - показывает версию Docker.")
        print("docker volume create <имя_тома> - создает том Docker.")
        print("docker volume ls - показывает список томов Docker.")
        print("docker volume rm <имя_тома> - удаляет том Docker.")
        print("docker service create --name <имя_сервиса> <имя_образа> - создает сервис Docker.")
        print("docker service ls - показывает список сервисов Docker.")
        print("docker service rm <имя_сервиса> - удаляет сервис Docker.")
        print("docker secret create <имя_секрета> <файл> - создает секрет Docker.")
        print("docker secret ls - показывает список секретов Docker.")
        print("docker secret rm <имя_секрета> - удаляет секрет Docker.")
        print("docker rmi <имя_образа> - удаляет образ Docker.")
        print("clear - очищает консоль.")

    def handle_command(self, command):
        """
        Обрабатывает команду пользователя.

        Args:
            command (str): Введенная пользователем команда.
        """
        command_parts = command.split()
        command_name = command_parts[0]
        command_args = command_parts[1:]
        command_obj = DockerCommand(command_name, command_args)

        if command_obj.name == "help":
            self.show_help()
        elif command_obj.name == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command_obj.name == "docker":
            if command_obj.args[0] == "ps":
                if len(command_obj.args) == 1:
                    self.show_containers(all=False)
                elif command_obj.args[1] == "-a":
                    self.show_containers(all=True)
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "images":
                self.show_images()
            elif command_obj.args[0] == "network" and command_obj.args[1] == "ls":
                self.show_networks()
            elif command_obj.args[0] == "volume" and command_obj.args[1] == "ls":
                self.show_volumes()
            elif command_obj.args[0] == "service" and command_obj.args[1] == "ls":
                self.show_services()
            elif command_obj.args[0] == "secret" and command_obj.args[1] == "ls":
                self.show_secrets()
            elif command_obj.args[0] == "rmi":
                if len(command_obj.args) > 1:
                    self.remove_image(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "stop":
                if len(command_obj.args) > 1:
                    self.stop_container(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "rm":
                if len(command_obj.args) > 1:
                    self.remove_container(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "volume" and command_obj.args[1] == "rm":
                if len(command_obj.args) > 2:
                    self.remove_volume(command_obj.args[2])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "service" and command_obj.args[1] == "rm":
                if len(command_obj.args) > 2:
                    self.remove_service(command_obj.args[2])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "secret" and command_obj.args[1] == "rm":
                if len(command_obj.args) > 2:
                    self.remove_secret(command_obj.args[2])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "run":
                if len(command_obj.args) > 1:
                    self.run_container(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "pull":
                if len(command_obj.args) > 1:
                    self.pull_image(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "build":
                if len(command_obj.args) > 2:
                    self.build_image(command_obj.args[2], command_obj.args[3])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "push":
                if len(command_obj.args) > 1:
                    self.push_image(command_obj.args[1])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "login":
                self.login()
            elif command_obj.args[0] == "logout":
                self.logout()
            elif command_obj.args[0] == "version":
                self.show_version()
            elif command_obj.args[0] == "volume" and command_obj.args[1] == "create":
                if len(command_obj.args) > 2:
                    self.create_volume(command_obj.args[2])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "service" and command_obj.args[1] == "create":
                if len(command_obj.args) > 3:
                    self.create_service(command_obj.args[3], command_obj.args[4])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            elif command_obj.args[0] == "secret" and command_obj.args[1] == "create":
                if len(command_obj.args) > 3:
                    self.create_secret(command_obj.args[3], command_obj.args[4])
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
            else:
                command_function = getattr(self, command_obj.name, None)
                if command_function:
                    command_function(*command_obj.args)
                else:
                    print("Неизвестная команда. Попробуйте 'help' для справки.")
        else:
            print("Неизвестная команда. Попробуйте 'help' для справки.")

    def show_list(self, data_type, all=False):
        """
        Выводит список элементов определенного типа.

        Args:
            data_type (str): Тип данных (images, containers, networks, volumes, services, secrets).
            all (bool): Флаг, указывающий, нужно ли выводить все элементы или только активные.
        """
        data = getattr(self, data_type)
        if all:
            print(f"Список всех {data_type}:")
        else:
            print(f"Список активных {data_type}:")
        if data:
            for item_name, info in data.items():
                print(f"{item_name} {info['created']}")
        else:
            print(f"{data_type.title()} не найдены.")

    def pull_image(self, image_name):
        self.images[image_name] = {
            "created": datetime.datetime.now(),
            "tags": ["latest"],
        }
        print(f"Образ '{image_name}' успешно скачан.")

    def show_images(self):
        self.show_list("images")

    def run_container(self, image_name):
        if image_name in self.images:
            container_name = f"container{len(self.containers) + 1}"
            self.containers[container_name] = {
                "image": image_name,
                "status": "running",
                "created": datetime.datetime.now(),
            }
            print(f"Контейнер '{container_name}' успешно запущен из образа '{image_name}'.")
        else:
            print(f"Образ '{image_name}' не найден.")

    def show_containers(self, all=False):
        self.show_list("containers", all)

    def stop_container(self, container_name):
        if container_name in self.containers:
            self.containers[container_name]["status"] = "stopped"
            print(f"Контейнер '{container_name}' успешно остановлен.")
        else:
            print(f"Контейнер '{container_name}' не найден.")

    def remove_container(self, container_name):
        if container_name in self.containers:
            del self.containers[container_name]
            print(f"Контейнер '{container_name}' успешно удален.")
        else:
            print(f"Контейнер '{container_name}' не найден.")

    def create_network(self, network_name):
        self.networks[network_name] = {
            "created": datetime.datetime.now(),
        }
        print(f"Сеть '{network_name}' успешно создана.")

    def show_networks(self):
        self.show_list("networks")

    def exec_command(self, container_name, command_to_run):
        if container_name in self.containers:
            print(f"Выполнение команды '{command_to_run}' в контейнере '{container_name}'...")
            # Здесь можно добавить логику для имитации выполнения команды
            print("Команда успешно выполнена.")
        else:
            print(f"Контейнер '{container_name}' не найден.")

    def build_image(self, image_name, context_path):
        self.images[image_name] = {
            "created": datetime.datetime.now(),
            "tags": ["latest"],
        }
        print(f"Образ '{image_name}' успешно построен из контекста '{context_path}'.")

    def push_image(self, image_name):
        if image_name in self.images:
            print(f"Образ '{image_name}' успешно отправлен в репозиторий.")
        else:
            print(f"Образ '{image_name}' не найден.")

    def login(self):
        print("Успешно авторизован в репозитории.")

    def logout(self):
        print("Успешно вышел из репозитория.")

    def show_version(self):
        print("Docker version 20.10.14")

    def create_volume(self, volume_name):
        self.volumes[volume_name] = {
            "created": datetime.datetime.now(),
        }
        print(f"Том '{volume_name}' успешно создан.")

    def show_volumes(self):
        self.show_list("volumes")

    def remove_volume(self, volume_name):
        if volume_name in self.volumes:
            del self.volumes[volume_name]
            print(f"Том '{volume_name}' успешно удален.")
        else:
            print(f"Том '{volume_name}' не найден.")

    def create_service(self, service_name, image_name):
        if image_name in self.images:
            self.services[service_name] = {
                "image": image_name,
                "created": datetime.datetime.now(),
            }
            print(f"Сервис '{service_name}' успешно создан из образа '{image_name}'.")
        else:
            print(f"Образ '{image_name}' не найден.")

    def show_services(self):
        self.show_list("services")

    def remove_service(self, service_name):
        if service_name in self.services:
            del self.services[service_name]
            print(f"Сервис '{service_name}' успешно удален.")
        else:
            print(f"Сервис '{service_name}' не найден.")

    def create_secret(self, secret_name, secret_file):
        self.secrets[secret_name] = {
            "file": secret_file,
            "created": datetime.datetime.now(),
        }
        print(f"Секрет '{secret_name}' успешно создан из файла '{secret_file}'.")

    def show_secrets(self):
        self.show_list("secrets")

    def remove_secret(self, secret_name):
        if secret_name in self.secrets:
            del self.secrets[secret_name]
            print(f"Секрет '{secret_name}' успешно удален.")
        else:
            print(f"Секрет '{secret_name}' не найден.")

    def remove_image(self, image_name):
        if image_name in self.images:
            del self.images[image_name]
            print(f"Образ '{image_name}' успешно удален.")
        else:
            print(f"Образ '{image_name}' не найден.")

def main():
    """
    Основная функция.
    """
    docker = DockerEmulator()
    while True:
        command = input("Введите команду: ")
        docker.handle_command(command)

if __name__ == "__main__":
    main()





