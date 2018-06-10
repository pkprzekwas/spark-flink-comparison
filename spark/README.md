# Apache Spark

### Running simple job

This part is fully focused on presenting the simpliest way to run a Spark job locally. It consists
of simple script which reads content of `/etc/hosts` hence it is dedicated for UNIX machines. SBT is
used to setup dependencies, compile and build a `jar` file.

Prerequisite: `SBT`

Build and run simple script:
```bash
make example-run
```
To clean build artefacts
```bash
make example-clean
```

