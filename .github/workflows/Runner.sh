# Create a folder
$ mkdir actions-runner && cd actions-runner
# Download the latest runner package
$ curl -o actions-runner-linux-arm-2.322.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.322.0/actions-runner-linux-arm-2.322.0.tar.gz
Copied!# Optional: Validate the hash
$ echo "583fc5f933eb2f0f9f388ef304085629181cef54e63fe3445eed92dba4a87c46  actions-runner-linux-arm-2.322.0.tar.gz" | shasum -a 256 -c
# Extract the installer
$ tar xzf ./actions-runner-linux-arm-2.322.0.tar.gz
Configure
# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/Apetree100122/arangodb_datasets --token A5WRBZ34BVNEC3VXZOTSUZ3HWCJKO
# Last step, run it!
$ ./run.sh
Using your self-hosted runner
# Use this YAML in your workflow file for each job
runs-on: self-hosted
