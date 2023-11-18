## Usage
```
cyral [OPTIONS] COMMAND [ARGS]...
```

  The Cyral CLI

### Options
|Name|Description|
|---|---|
|`--cp-address TEXT`|Cyral Control Plane Address|
|`--idp TEXT`|Identity Provider to use to authenticate to Cyral|
|`--local-port INTEGER`|Local port number for receiving OAuth2 redirects  [default: 8005]|
|`--stored-creds / --no-stored-creds`|Use and/or store refresh token in ~/.cyral  [default: stored-creds]|
|`--offline-access / --no-offline-access`|Obtain a (long lived) offline refresh token  [default: no-offline-access]|
|`--realm TEXT`|Authentication realm (usually not needed)  [default: default]|
|`--version`|Show the version and exit.|
|`--help`|Show this message and exit.|

### Commands
|Name|Description|
|---|---|
|`access`|Access a data repo.|
|`help`|Prints detailed usage information including commands,...|
|`sidecar`|Sidecar related commands|

## Usage
```
cyral help [OPTIONS]
```

  Prints detailed usage information including commands, subcommands, and
  options.

### Options
|Name|Description|
|---|---|
|`-f, --output-format [plain \| md]`|Output format  [default: plain]|
|`--help`|Show this message and exit.|

## Usage
```
cyral access [OPTIONS] COMMAND [ARGS]...
```

  Access a data repo.

### Options
|Name|Description|
|---|---|
|`--help`|Show this message and exit.|

### Commands
|Name|Description|
|---|---|
|`pg`|Configure access to postgres databases via Cyral in .pgpass file.|
|`repo`|Obtain information to access a data repo|
|`s3`|Configure AWS profile for accessing S3 via Cyral sidecar.|
|`token`|Obtain access token for accessing a data repo.|

## Usage
```
cyral access token [OPTIONS]
```

  Obtain access token for accessing a data repo.

### Options
|Name|Description|
|---|---|
|`-h, --help`|Show help message and exit.|

## Usage
```
cyral access repo [OPTIONS]
```

  Obtain information to access a data repo

### Options
|Name|Description|
|---|---|
|`-n, --name TEXT`|Repo name in Cyral (substring match)|
|`--tag TEXT`|Repo tag (substring match)|
|`-t, --type [auroramysql \| aurorapostgres \| denodo \| dremio \| galera \| mariadb \| mongodb \| mysql \| oracle \| postgresql \| redshift \| s3 \| sqlserver]`|Repo type|
|`--repos-per-page INTEGER`|Number of repos shown per page  [default: 10]|
|`-f, --output-format [plain \| json]`|Output format  [default: plain]|
|`-h, --help`|Show help message and exit.|

## Usage
```
cyral access s3 [OPTIONS]
```

  Configure AWS profile for accessing S3 via Cyral sidecar.

### Options
|Name|Description|
|---|---|
|`--aws-profile TEXT`|Name of the AWS profile to configure  [default: cyral]|
|`--autoconfigure / --no-autoconfigure`|Autoconfigure (without confirmation) S3 proxy settings  [default: no-autoconfigure]|
|`--account-name TEXT`|Preferred account name to use for accessing the s3 repo|
|`--silent / --no-silent`|Do not print confirmation messages  [default: no-silent]|
|`-h, --help`|Show help message and exit.|

## Usage
```
cyral access pg [OPTIONS]
```

  Configure access to postgres databases via Cyral in .pgpass file.

### Options
|Name|Description|
|---|---|
|`--silent / --no-silent`|Do not print confirmation messages  [default: no-silent]|
|`-h, --help`|Show help message and exit.|

## Usage
```
cyral sidecar [OPTIONS] COMMAND [ARGS]...
```

  Sidecar related commands

### Options
|Name|Description|
|---|---|
|`--id TEXT`|the id of the sidecar|
|`--name TEXT`|the name of the sidecar|
|`--help`|Show this message and exit.|

### Commands
|Name|Description|
|---|---|
|`get`|Get information about sidecars in the control plane.|
|`set`|Set different sidecar options.|

## Usage
```
cyral sidecar get [OPTIONS]
```

  Get information about sidecars in the control plane.

### Options
|Name|Description|
|---|---|
|`--output-format [yaml \| json \| table]`|output format  [default: table]|
|`-h, --help`|Show help message and exit.|

## Usage
```
cyral sidecar set [OPTIONS] COMMAND [ARGS]...
```

  Set different sidecar options.

### Options
|Name|Description|
|---|---|
|`--help`|Show this message and exit.|

### Commands
|Name|Description|
|---|---|
|`log-level`|Set the log level for a sidecar service.|

## Usage
```
cyral sidecar set log-level [OPTIONS]
```

  Set the log level for a sidecar service. The argument can be of the form
  <level> (log level applicable to all services) or <service>:<level> (log
  level for a specific service). <level> can be one of fatal, error, warn,
  info, debug, or trace. The list of services may vary depending on the
  sidecar version and configuration. This option can be specified multiple
  times, the last log level specified for a service is the one that is set.

  ### Examples

  #### set the level for all services

  `cyral sidecar set log-level --level debug`

  #### set the level for a single service

  `cyral sidecar set log-level --level dispatcher:warn`

  #### set the level for multiple services

  `cyral sidecar set log-level --level dispatcher:warn --level pg-wire:debug`

### Options
|Name|Description|
|---|---|
|`--level TEXT`|requested log level|
|`-h, --help`|Show help message and exit.|

