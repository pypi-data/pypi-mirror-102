# docker-buildtool

`docker-buildtool` extends the Dockerfile format. It serves as a
drop-in replacement for `docker build`, and works with unmodified
Dockerfiles.

Its main goal is to make code in many different repositories feel like a
single project. This is particularly desirable in research, where
you'll often want to make local changes to many repositories at
once.

`docker-buildtool` relies on all code being checked out in a
predictable way across different developers' machines. At OpenAI, we
require everyone to clone the repositories from `github.com/openai` to
a single folder, such as `~/openai`.

Its core functionality then:

1. Allows a Dockerfile to opt in to which code should be included in
   the build context. (In contrast, the default behavior of `docker
   build` is to require opting out.)
2. Errors out a build which is missing dependencies, printing out the
   appropriate `git clone` to use: `docker_buildtool.error.Error: Missing required path: /Users/gdb/openai/cloudgym. (HINT: you can obtain this by running "git clone git@github.com:openai/cloudgym.git /Users/gdb/openai/cloudgym")`
3. Allows a Dockerfile to specify its build root. This makes it easy
   to have multiple Dockerfiles build from a common root, while
   distributed in the component repositories.

It also provides secondary, more experimental functionality:

1. `DOCKER_BUILDTOOL_RSYNC=y docker-buildtool build` will `rsync` your
   files to whatever remote machine is specified by your
   `$DOCKER_HOST`, and do the build on that machine. If you have a
   sizable build context, this will generally save loads of time.
2. `docker-buildtool pull` runs a `git pull` in all dependent
   repositories. Particularly important for projects with lots of
   changes across different repositories.
3. Provides template expansion via `#docker-buildtool:variable varname`. This
   can be used in places where build args cannot, for example, by
   dynamically selecting the base image: `FROM
   docker.openai.com/base:#docker-buildtool:variable version` will
   expand to `FROM
   docker.openai.com/base:0.0.1`
4. Recording the Git revisions of each dependent repository. You
   generally don't want to include the `.git` repository, so this
   becomes useful for introspection.
5. Bundling your build context into a tarball on S3, so that future runs
   of that container can download fresh code.

## FAQ

- **Does `docker-buildtool` clone my dependencies at build time?** No,
  while `docker-buildtool` does know how to clone your dependencies,
  those are just for informational purposes if someone's missing them:
  it's still your job to clone them, and they get loaded into the
  build context.

## Installation

Install directly form `pip`:

```
pip install docker-buildtool
```

## Usage

- To build a docker image, run `docker-buildtool -t tag` in a directory
  with a Dockerfile. This will generate a `.dockerignore` and a modified
  Dockerfile, and then run `docker build`.
- To pull in all dependent repositories, run `docker-buildtool pull`.
- [experimental] To view revision state for all dependent
  repositories, run `docker-buildtool version`. Prints a
  human-readable git status for al dependent repositories, including
  current branch name, commit hashes, unpulled changes from origin,
  unpushed local changes, modified uncommitted files, and submodule
  versions.

## Dockerfile syntax

### Front matter

`docker-buildtool`'s dependency and file inclusion is configured via a
YAML [front matter](https://jekyllrb.com/docs/frontmatter/), encased
in comments, to the top of the Dockerfile. So add a big block comment
like the following to the top of your Dockerfile:

```
# ---
# build_root: ../..
# ignore:
#  - universe-envs/flashgames/src/**/vexpect
#  - universe-envs/flashgames/build
#  - universe-envs/flashgames/out
# include:
#  - universe-envs/controlplane
#  - universe-envs/flashgames
#  - universe-envs/base/openai-tigervnc
#  - universe-envs/base/openai-setpassword
#  - {'path': 'gym-demonstration', 'git': 'git@github.com:openai/gym-demonstration.git', 'setup': 'pip install -e .'}
#  - {'path': 'universe', 'git': 'git@github.com:openai/universe.git', 'setup': 'pip install -e .'}
# ---

FROM ubuntu:16.04
...
COPY . /app
```

The following front matter directives are supported:

- `build_root`: defines where the build happens, relative to the
  Dockerfile. Generally should be the common code root.
- `ignore`: Any files to ignore. Supports `.dockerignore` syntax,
  including `**` and `!`.
- `include`: Any files to include. These are used to generate a
  `.dockerignore` file, with `!` prefixed. (`docker-buildtool` will
  also manually expand `**` and interior `*`'s, which aren't properly
  supported by `.dockerignore`.)
- `default_ignore` (default: `True`): Also ignores `**/.git, **/*.egg-info, **/*.o`

### [experimental] Variable expansion

The directive `#docker-buildtool:variable varname` (where varname
matches `[\w-]*`) gets expanded to the value of `varname`. You provide
the value of `varname` as the `-v` argument to `docker-buildtool`:
`docker-buildtool -v varname=value`.

So for example, `docker-buildtool -v version=0.0.1` will expand

```
FROM docker.openai.com/base:#docker-buildtool:variable version
```

To:

```
FROM docker.openai.com/base:0.0.1
```
