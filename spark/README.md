# Apache Spark

### Prerequisites
- `SBT`
- Spark (version 2.3)

### Quick start
Build and run script:
```bash
make build
APP=<app_name> make run
```
Available apps:
- sql (default)
- kafka
- streaming

To clean artifacts:
```bash
make clean
```

### Tips and Tricks

##### Running in Intellij
1. Open the project in Intellij.
2. Find `build.sbt` file.
3. Run `Import project`