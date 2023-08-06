from setuptools import setup, find_packages

setup(name="msg_srv_project",
      version="0.0.1",
      description="message server",
      author="Oleg Lo",
      author_email="olomakin@ya.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )