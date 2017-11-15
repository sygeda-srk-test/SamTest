# SamTest
It is a part of CI environment to check python's sources with `pylint` in the `TeamCity`.
Environment built by `Docker` & `TeamCity`
To download TeamCity-Agent image
*(be sure docker installed and run)*
```
docker pull 000bas007/tc:agent
```
to run:

```
docker run --name tc-agent -p 9090:9090 000bas007/tc:agent
```

Also, you can use `TEAMCITY_SERVER` & `AGENT_NAME` as environment variables:

```
docker run --name tc-agent -p 9090:9090 -e TEAMCITY_SERVER=http://10.0.0.1:8111 000bas007/tc:agent
```
*(be sure that `TeamCity` agent is authrized by the server)*

After each pull request to the `GitHub` repository, `TeamCity` will run the `pylint` for all `*.py` files and return status to the repository.

