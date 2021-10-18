from setuptools import find_packages, setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='finn-api-gateway',
      version='0.1',
      description="finn's API Gateway",
      long_description='',
      author='Asutosh Parida',
      author_email='ast.jva@gmail.com',
      entry_points={
              'console_scripts': [
                  'finn-api = api_gateway:main',
              ],
          },
      classifiers=[
        'Programming Language :: Python :: 3.9',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux'
      ],
      packages=find_packages(),
      install_requires=[
          'importlib',
          'datetime',
          'json5',
          'logging',
          'yaml-1.3',
          'PyYAML',
          'Werkzeug==2.0.2',
          'Flask==2.0.2',
          'Flask-RESTful==0.3.9',
          'flask-accepts==0.18.4',
          'flask-restx==0.5.1',
          'validators==0.18.2',
          'MarkupSafe==2.0.1',
          'marshmallow==3.12.2',
          'flask_caching',
          'flask-pytest'
      ],
      dependency_links=[],
      package_data={'':['*.yaml']},
      setup_requires=['pytest-runner'],
      tests_require=['mock', 'pytest'],
      zip_safe=False)
