Scan a container image

Usage:
  trivy image [flags] IMAGE_NAME

Aliases:
  image, i

Examples:
  # Scan a container image
  $ trivy image python:3.4-alpine

  # Scan a container image from a tar archive
  $ trivy image --input ruby-3.1.tar

  # Filter by severities
  $ trivy image --severity HIGH,CRITICAL alpine:3.15

  # Ignore unfixed/unpatched vulnerabilities
  $ trivy image --ignore-unfixed alpine:3.15

  # Scan a container image in client mode
  $ trivy image --server http://127.0.0.1:4954 alpine:latest

  # Generate json result
  $ trivy image --format json --output result.json alpine:3.15

  # Generate a report in the CycloneDX format
  $ trivy image --format cyclonedx --output result.cdx alpine:3.15

Scan Flags
      --file-patterns strings   specify config file patterns
      --offline-scan            do not issue API requests to identify dependencies
      --parallel int            number of goroutines enabled for parallel scanning, set 0 to auto-detect parallelism (default 5)
      --rekor-url string        [EXPERIMENTAL] address of rekor STL server (default "https://rekor.sigstore.dev")
      --sbom-sources strings    [EXPERIMENTAL] try to retrieve SBOM from the specified sources (oci,rekor)
      --scanners strings        comma-separated list of what security issues to detect (vuln,misconfig,secret,license) (default [vuln,secret])
      --skip-dirs strings       specify the directories or glob patterns to skip
      --skip-files strings      specify the files or glob patterns to skip

Report Flags
      --compliance string          compliance report to generate (docker-cis-1.6.0)
      --dependency-tree            [EXPERIMENTAL] show dependency origin tree of vulnerable packages
      --exit-code int              specify exit code when any security issues are found
      --exit-on-eol int            exit with the specified code when the OS reaches end of service/life
  -f, --format string              format (table,json,template,sarif,cyclonedx,spdx,spdx-json,github,cosign-vuln) (default "table")
      --ignore-policy string       specify the Rego file path to evaluate each vulnerability
      --ignorefile string          specify .trivyignore file (default ".trivyignore")
      --list-all-pkgs              output all packages in the JSON report regardless of vulnerability
  -o, --output string              output file name
      --output-plugin-arg string   [EXPERIMENTAL] output plugin arguments
      --report string              specify a format for the compliance report. (all,summary) (default "summary")
  -s, --severity strings           severities of security issues to be displayed (UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL) (default [UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL])
      --show-suppressed            [EXPERIMENTAL] show suppressed vulnerabilities
  -t, --template string            output template

Cache Flags
      --cache-backend string   [EXPERIMENTAL] cache backend (e.g. redis://localhost:6379) (default "fs")
      --cache-ttl duration     cache TTL when using redis as cache backend
      --redis-ca string        redis ca file location, if using redis as cache backend
      --redis-cert string      redis certificate file location, if using redis as cache backend
      --redis-key string       redis key file location, if using redis as cache backend
      --redis-tls              enable redis TLS with public certificates, if using redis as cache backend

DB Flags
      --db-repository string        OCI repository to retrieve trivy-db from (default "ghcr.io/aquasecurity/trivy-db:2")
      --download-db-only            download/update vulnerability database but don't run a scan
      --download-java-db-only       download/update Java index database but don't run a scan
      --java-db-repository string   OCI repository to retrieve trivy-java-db from (default "ghcr.io/aquasecurity/trivy-java-db:1")
      --no-progress                 suppress progress bar
      --skip-db-update              skip updating vulnerability database
      --skip-java-db-update         skip updating Java index database

Registry Flags
      --password strings        password. Comma-separated passwords allowed. TRIVY_PASSWORD should be used for security reasons.
      --registry-token string   registry token
      --username strings        username. Comma-separated usernames allowed.

Image Flags
      --docker-host string              unix domain socket path to use for docker scanning
      --image-config-scanners strings   comma-separated list of what security issues to detect on container image configurations (misconfig,secret)
      --image-src strings               image source(s) to use, in priority order (docker,containerd,podman,remote) (default [docker,containerd,podman,remote])
      --input string                    input file path instead of image name
      --platform string                 set platform in the form os/arch if image is multi-platform capable
      --podman-host string              unix podman socket path to use for podman scanning
      --removed-pkgs                    detect vulnerabilities of removed packages (only for Alpine)

Vulnerability Flags
      --ignore-status strings   comma-separated list of vulnerability status to ignore (unknown,not_affected,affected,fixed,under_investigation,will_not_fix,fix_deferred,end_of_life)
      --ignore-unfixed          display only fixed vulnerabilities
      --skip-vex-repo-update    [EXPERIMENTAL] Skip VEX Repository update
      --vex strings             [EXPERIMENTAL] VEX sources ("repo", "oci" or file path)

Misconfiguration Flags
      --checks-bundle-repository string   OCI registry URL to retrieve checks bundle from (default "ghcr.io/aquasecurity/trivy-checks:0")
      --helm-api-versions strings         Available API versions used for Capabilities.APIVersions. This flag is the same as the api-versions flag of the helm template command. (can specify multiple or separate values with commas: policy/v1/PodDisruptionBudget,apps/v1/Deployment)
      --helm-kube-version string          Kubernetes version used for Capabilities.KubeVersion. This flag is the same as the kube-version flag of the helm template command.
      --helm-set strings                  specify Helm values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --helm-set-file strings             specify Helm values from respective files specified via the command line (can specify multiple or separate values with commas: key1=path1,key2=path2)
      --helm-set-string strings           specify Helm string values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --helm-values strings               specify paths to override the Helm values.yaml files
      --include-non-failures              include successes and exceptions, available with '--scanners misconfig'
      --misconfig-scanners strings        comma-separated list of misconfig scanners to use for misconfiguration scanning (default [azure-arm,cloudformation,dockerfile,helm,kubernetes,terraform,terraformplan-json,terraformplan-snapshot])
      --tf-exclude-downloaded-modules     exclude misconfigurations for downloaded terraform modules

Module Flags
      --enable-modules strings   [EXPERIMENTAL] module names to enable
      --module-dir string        specify directory to the wasm modules that will be loaded (default "/root/.trivy/modules")

Secret Flags
      --secret-config string   specify a path to config file for secret scanning (default "trivy-secret.yaml")

License Flags
      --ignored-licenses strings         specify a list of license to ignore
      --license-confidence-level float   specify license classifier's confidence level (default 0.9)
      --license-full                     eagerly look for licenses in source code headers and license files

Rego Flags
      --check-namespaces strings    Rego namespaces
      --config-check strings        specify the paths to the Rego check files or to the directories containing them, applying config files
      --config-data strings         specify paths from which data for the Rego checks will be recursively loaded
      --include-deprecated-checks   include deprecated checks
      --skip-check-update           skip fetching rego check updates
      --trace                       enable more verbose trace output for custom queries

Package Flags
      --pkg-relationships strings   list of package relationships (unknown,root,direct,indirect) (default [unknown,root,direct,indirect])
      --pkg-types strings           list of package types (os,library) (default [os,library])

Client/Server Flags
      --custom-headers strings   custom headers in client mode
      --server string            server address in client mode
      --token string             for authentication in client/server mode
      --token-header string      specify a header name for token in client/server mode (default "Trivy-Token")

Global Flags:
      --cache-dir string          cache directory (default "/root/.cache/trivy")
  -c, --config string             config path (default "trivy.yaml")
  -d, --debug                     debug mode
      --generate-default-config   write the default config to trivy-default.yaml
      --insecure                  allow insecure server connections
  -q, --quiet                     suppress progress bar and log output
      --timeout duration          timeout (default 5m0s)
  -v, --version                   show version
