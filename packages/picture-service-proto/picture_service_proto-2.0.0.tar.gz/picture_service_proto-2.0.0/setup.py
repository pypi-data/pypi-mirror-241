from distutils.core import setup

setup(
    name='picture_service_proto',
    version='2.0.0',
    description='GRPC client for picture_service_proto',
    author='ci',
    author_email='p.a.anokhin@gmail.com',
    packages=['picture_service_proto'],
    package_data={
      'picture_service_proto': ['*.pyi', 'py.typed'],
    },
    include_package_data=True,
)
