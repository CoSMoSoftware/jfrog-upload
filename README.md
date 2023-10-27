# jfrog-upload
Upload build artifacts to JForg Artifactory generic registry.

# Example of usage:
```bash
- name: 'Upload build artifacts - JFrog Artifactory'
  uses: CoSMoSoftware/jfrog-upload@v0.0.1
  with:
    access_token: ${{ secrets.< access_token | password > }}
    user_name: ${{ secrets.<user_name> }}
    registry_url: "https://jfrog-sfo.dolby.net/artifactory/dolbyio-capi-generic-sfo/<TARGET_FILE_PATH>"
    artefacts_patterns: |
      ./build*/my-artefact-0.1.2-ubuntu20*.zip
      ./build*/my-artefact-*-ubuntu20-dbgsym.zip
    action_shell: <bash | powershell> # required only for powershell - bash is set as default.
```
