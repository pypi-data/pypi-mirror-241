# The Cyral CLI Tool

Use this tool to obtain credentials for accessing a data repo via the Cyral sidecar.

**Note 1** This tool does not work with Cyral versions before 3.0. If you are using an
older version of Cyral, please use the [gimme-db-token](https://pypi.org/project/cyral-gimme-db-token/)
tool instead.

**Note 2** Use version 1.x of this tool for Cyral version 3.X and version 2.x for Cyral version 4.X and greater.

## Usage

```
cyral <global options> <command> <subcommand> <command options>
```

For detailed usage instructions:

```bash
cyral --help
```

### Global Options

- `--cp-address <control plane address>` Cyral Control Plane Address, e.g., `mycompany.app.cyral.com` (the address may need a :8000 suffix in some cases).
- `--idp <idp alias>` The identity provider to use for authentication.
- `--offline-access` Obtain a long-lived offline access token for authentication to the control plane.
- `--no-stored-creds` Do not store or use a stored refresh token.
- `--realm` The authentication realm in the Cyral control plane. This is usually not needed. Please contact Cyral Support for help if authentication is failing without this option.
- `--version` Show package version and exit.
- `--help` Show command help.

### Top Level Commands

### `access`

Tools for accessing different options on the cyral CP

It has the following subcommands:

- `token` Print a token for authenticating to a repo using your email address as user name.
- `repo` Show list of accessible data repos and print connection information for the selected repo.
  + Use `--type`, `--tag`, `--name` options to specify repo filters.
- `s3` Write configuration needed to access S3 to AWS config files.
- `pg` Write configuration needed to access selected postgres database to `.pgpass` file.

### `sidecar` 

Tools for interacting with the Cyral sidecars

It has the following subcommands:

- `get` Get information for a sidecar or sidecars.
- `set` Set options on a sidecar.

#### `set`

Set options for a Cyral sidecar. It has the following subcommands:

- `log-level` Sets the log level for sidecar service(s).

