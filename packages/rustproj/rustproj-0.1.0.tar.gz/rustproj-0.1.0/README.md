# RustProj

Simple rust project generator. 

## Steps to run

- Create a new project

```bash
user@programmer~:$ rustproj --proj <proj-name>
```

- Create a new library

```bash
user@programmer~:$ rustproj --proj <proj-name> --lib
```

- Create a project with both main and lib

```bash
user@programmer~:$ rustproj --proj <proj-name> --both
```

- Force creation (used when project already exists)

```bash
user@programmer~:$ rustproj --proj <proj-name> [--lib | --both]
```

- Check version

```bash
user@programmer~:$ rustproj --version
```

## License

Licensed under <a href="https://github.com/frankhart2018/rustproj/blob/master/LICENSE">MIT</a> license.