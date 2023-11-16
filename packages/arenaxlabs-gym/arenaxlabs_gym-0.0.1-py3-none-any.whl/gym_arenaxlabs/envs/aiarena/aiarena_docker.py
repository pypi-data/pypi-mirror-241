import docker
import socket
import time

class AIArenaDocker:
    def __init__(self, image_name = "ghcr.io/arenax-labs/ai-arena-researcher-game:latest", container_name = "ai-arena-researcher-game"):
        self.image_name = image_name
        self.container_name = container_name

        self.container_host = 'localhost'
        self.container_port = 8080

        print("Setting up Game Container...")
        self.client = docker.from_env()

    def container_exists(self):
        try:
            self.client.containers.get(self.container_name)
            return True
        except docker.errors.NotFound:
            return False

    def container_running(self):
        container = self.client.containers.get(self.container_name)
        return container.status == 'running'

    def is_image_up_to_date(self):
        try:
            local_image = self.client.images.get(self.image_name)
            local_digest = local_image.attrs.get('RepoDigests')[0].split('@')[1]

            remote_image = self.client.images.get_registry_data(self.image_name)
            remote_digest = remote_image.attrs.get('Descriptor', {}).get('digest')

            return local_digest == remote_digest

        except docker.errors.ImageNotFound:
            return False
        except Exception as e:
            print(f"Error checking image update: {e}")
            return False

    def pull_image(self):
        try:
            self.client.images.pull(self.image_name)
        except docker.errors.APIError as e:
            if "authentication required" in str(e):
                print(f"Warning: Unable to pull image {self.image_name}. Please login to GitHub Packages.")
            else:
                print(f"Error: {e}")

    def wait_for_container(self):
        while True:
            try:
                with socket.create_connection((self.container_host, self.container_port), timeout=5):
                    break
            except (ConnectionRefusedError, TimeoutError):
                print(f"Port {self.container_port} is not yet open. Retrying...")
        time.sleep(1)

    def run_game(self):
        if (not self.is_image_up_to_date()):
            self.pull_image()
        
        if (not self.container_exists() or not self.container_running()):
            if (self.container_exists()):
                container = self.client.containers.get(self.container_name)
                container.start()
            else:
                self.client.containers.run(self.image_name, name=self.container_name, ports={'8080/tcp': self.container_port}, detach=True)

            self.wait_for_container()
            print(f"Container {self.container_name} is now running on port 8080!")
        else:
            self.wait_for_container()
            print(f"Container {self.container_name} is already running on port 8080!")

    def stop_game(self):
        self.client.containers.get(self.container_name).stop()