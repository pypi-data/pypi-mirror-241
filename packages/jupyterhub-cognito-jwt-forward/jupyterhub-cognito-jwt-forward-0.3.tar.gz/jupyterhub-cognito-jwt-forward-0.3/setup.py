from setuptools import setup

setup(
    name='jupyterhub-cognito-jwt-forward',
    version='0.3',
    url='https://github.com/fldsblzs/jwtauthenticator',
    author='fldsblzs',
    author_email='foldesibalazs@gmail.com',
    license='Apache 2.0',
    packages=['jupyterhub-cognito-jwt-forward'],
    install_requires=[
        'jupyterhub',
        'python-jose',
        'PyJWT',
        'requests'
    ]
)
