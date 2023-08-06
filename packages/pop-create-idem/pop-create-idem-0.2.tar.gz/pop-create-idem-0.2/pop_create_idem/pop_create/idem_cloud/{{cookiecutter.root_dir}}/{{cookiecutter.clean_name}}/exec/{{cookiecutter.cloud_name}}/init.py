def __init__(hub):
    # This enables acct profiles that begin with "{{cookiecutter.cloud_name}}" for idem_cloud modules
    hub.exec.{{cookiecutter.cloud_name}}.ACCT = ["{{cookiecutter.acct_plugin}}"]

    def _get_version_sub(ctx, *args, **kwargs):
        api_version = ctx.acct.get("api_version", "latest")
        return hub.exec.vmc[api_version]

    # Get the version sub dynamically from the ctx variable/acct
    hub.pop.sub.dynamic(hub.exec.{{cookiecutter.cloud_name}}, _get_version_sub)
