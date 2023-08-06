from setuptools import setup
setup(name='whitenoise_player',
      version='0.0.1',
      description='White noise player',
      url="https://python3.whitenoi.se/",
      long_description='Just play white noise with whitenoise.play()',
      author='Adam Jenca',
      author_email='jenca.a@gjh.sk',
      install_requires=['numpy','sounddevice'],
      packages=['whitenoise'])
