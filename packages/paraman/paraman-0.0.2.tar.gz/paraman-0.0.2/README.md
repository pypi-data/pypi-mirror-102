# paraman

## Requirements

- Python 3.6.7+
- (Optional) [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) for deploying a CloudFormation template

## Installation

```bash
$ pip install paraman
```

### Docker

**TODO**: Update DockerHub pipeline

```bash
docker run --rm -it unfor19/paraman
```

## Features

1. Get SSM Parameters by path, output: `.parameters.json` and `.parameters_types.json`
1. Generate SSM parameters to CloudFormation templates, according to Get SSM Parameters, output: `.merged.yaml`
1. Deploy CloudFormation template `.merged.yaml`, output: CloudFormation Stack in AWS
1. Put SSM Parameters values in AWS, according to Get SSM Parameters, output: `SSM Parameters with a dummy value "empty" in AWS`


## Usage

<!-- available_commands_start -->

```
Usage: paraman [OPTIONS] COMMAND [ARGS]...

  Examples:

  paraman parameter-get                    
  --parameters-region eu-west-1            
  --prefix-to-replace /my-app/development/ 
  --exclude-paths "/accounts/,/google_credentials/,/cookie_secret"

  paraman cloudformation-create            
  --prefix-to-replace /my-app/development/ 
  --replace-prefix-with /my-app/test/

  aws cloudformation deploy                
  --region us-east-1                       
  --template-file .merged.yaml             
  --stack-name test-virginia

  paraman parameter-put                    
  --parameters-region us-east-1            
  --prefix-to-replace /my-app/dev/         
  --replace-prefix-with /my-app/test/      
  --overwrite=true

Options:
  -ci, --ci                Use this flag to avoid confirmation prompts
  -dev, --local-dev        Use this flag for local tests with localstack
  -u, --endpoint-url TEXT  Set a custom AWS endpoint_url
  --help                   Show this message and exit.

Commands:
  cloudformation-create  Alias: cc Gets SSM Parameters from AWS or from the...
  parameter-get          Alias: pg Gets `parameters_region` and...
  parameter-put          Alias: pp Gets `parameters_region` and...
  version                Print the installed version
```

<!-- available_commands_end -->

## Contributing

Report issues/questions/feature requests on the [Issues](https://github.com/doitintl/paraman/issues) section.

Pull requests are welcome! Ideally, create a feature branch and issue for every single change you make. These are the steps:

1. Fork this repo
1. Create your feature branch from master (`git checkout -b my-new-feature`)
1. Install from source
   ```bash
    $ git clone https://github.com/${GITHUB_OWNER}/paraman.git && cd paraman
    ...
    $ pip install --upgrade pip
    ...
    $ python -m venv ./ENV
    $ . ./ENV/bin/activate
    ...
    $ (ENV) pip install --editable .
    ...
    # Done! Now when you run 'paraman' it will get automatically updated when you modify the code
   ```
1. Add the code of your new feature
1. Test - make sure all commands work properly (**TODO**: add tests)
1. Commit your remarkable changes (`git commit -am 'Added new feature'`)
1. Push to the branch (`git push --set-up-stream origin my-new-feature`)
1. Create a new Pull Request and tell us about your changes

## Authors

Created and maintained by [Meir Gabay](https://github.com/unfor19)
