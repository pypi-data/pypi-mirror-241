# JupyterHub Cognito JWT Forward

Handle the authentication in Jupyter Hub when the actual authentication is happening on the application load balancer level in AWS. This authenticator just parses the forwarded JWT coming from AWS and sets the email.

> This implementation is not secure, only use this behind a load balancer with Cognito Authentication action configured.

## Installation

This package can be installed with pip:

```
pip install jupyterhub-cognito-jwt-forward
```

## Configuration

```py
# jupyterhub_config.py

# Using JSONWebTokenAuthenticator
c.JupyterHub.authenticator_class = 'jupyterhub-cognito-jwt-forward.jwtauthenticator.JSONWebTokenAuthenticator'
c.JSONWebTokenAuthenticator.header_name = 'x-amzn-oidc-data'

# Using JSONWebTokenLocalAuthenticator
c.JupyterHub.authenticator_class = 'jupyterhub-cognito-jwt-forward.jwtauthenticator.JSONWebTokenLocalAuthenticator'
c.JSONWebTokenLocalAuthenticator.header_name = 'x-amzn-oidc-data'

c.JSONWebTokenLocalAuthenticator.create_system_users = True # (optional)
```