
> :warning: **This module is now legacy**: The same functionality is now in proton-vpn-network-manager module, version `0.6.3` and upwards.


# Proton VPN Network Manager OpenVPN

The `proton-vpn-network-manager-openvpn` component adds support for the OpenVPN
protocol using [NetworkManager](https://networkmanager.dev).

## Development

Even though our CI pipelines always test and build releases using Linux distribution packages,
you can use pip to set up your development environment.

### Proton package registry

If you didn't do it yet, to be able to pip install Proton VPN components you'll
need to set up our internal Python package registry. You can do so running the
command below, after replacing `{GITLAB_TOKEN`} with your
[personal access token](https://gitlab.protontech.ch/help/user/profile/personal_access_tokens.md)
with the scope set to `api`.

```shell
pip config set global.index-url https://__token__:{GITLAB_TOKEN}@gitlab.protontech.ch/api/v4/groups/777/-/packages/pypi/simple
```

In the index URL above, `777` is the id of the current root GitLab group,
the one containing the repositories of all our Proton VPN components.

### Known issues

This component depends on `proton-vpn-network-manager` which, unfortunately, it
currently requires installing quite a few distribution packages. If you didn't
install them yet, head over to this component's
[readme file](https://gitlab.protontech.ch/ProtonVPN/linux/new-client/vpnconnection/python-protonvpn-network-manager#known-issues)
for more details.

### Virtual environment

You can create the virtual environment and install the rest of dependencies as follows:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Unit tests

You can run the unit tests with:

```shell
pytest tests
```

### Integration tests

You can run the integration tests with:

```shell
pytest tests_integration
```

You can set the following environment variables to change the integration tests configuration:

 * `PROTON_API_ENVIRONMENT`: the name of the Proton API environment (for example, `atlas`).
 * `TEST_VPN_SERVER_NAME`: the name of the VPN server to connect to.
 * `TEST_OPENVPN_USERNAME`: the OpenVPN username used to establish connections.
 * `TEST_OPENVPN_PASSWORD`: the OpenVPN password used to establish connections.
