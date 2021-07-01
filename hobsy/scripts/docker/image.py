import docker
from docker.models.images import Image
import os


client = docker.from_env()


def build(path: str, tag: str, **kwargs) -> Image:
  return client.images.build(path=path, tag=tag, **kwargs)


def save(image: Image, name: str, dest: str = ".") -> str:
  path = os.path.join(dest, f'{name}.tar')
  with open(path, 'wb') as f:
    for chunk in image.save():
      f.write(chunk)
  return path
