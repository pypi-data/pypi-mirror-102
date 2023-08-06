from setuptools import setup, find_packages

setup(name="message_server_zda",
      version="0.0.1",
      description="message_server_zda",
      author="Dmitrii Zarubin",
      author_email="zda_87@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
