from setuptools import setup, find_packages

setup(name="mymess_server",
      version="0.0.1",
      description="My Messenger Server",
      author="Aleksei Dolov",
      author_email="stentory@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
