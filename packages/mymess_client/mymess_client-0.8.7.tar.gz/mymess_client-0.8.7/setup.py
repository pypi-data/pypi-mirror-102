from setuptools import setup, find_packages

setup(name="mymess_client",
      version="0.8.7",
      description="My Messenger Client",
      author="Aleksei Dolov",
      author_email="stentory@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
