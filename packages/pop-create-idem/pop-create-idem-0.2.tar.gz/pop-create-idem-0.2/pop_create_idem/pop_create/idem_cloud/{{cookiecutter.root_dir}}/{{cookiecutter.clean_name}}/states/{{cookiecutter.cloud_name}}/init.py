def __init__(hub):
    # This enables acct profiles that begin with "{{cookiecutter.cloud_name}}" for states
    hub.states.{{cookiecutter.cloud_name}}.ACCT = ["{{cookiecutter.acct_plugin}}"]
