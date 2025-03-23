```
commit 5fef6a8560993e193c71bdf001be60d832fd0ee3
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 13:59:14 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 13:59:14 2025 +0100

    [#1]: update project version from 0.0.0 to 0.0.1

commit 0e314f98003a0216f8709f7fda352ece3c43771e
Merge: f881328 10b5b02
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 13:57:52 2025 +0100
Commit:     GitHub <noreply@github.com>
CommitDate: Sun Mar 23 13:57:52 2025 +0100

    Merge pull request #6 from DesmoDyne/feature/2/create-first-version
    
    feature/2/create-first-version

commit 10b5b024e97a9e942900201285c93150a95b66a8
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 09:15:54 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 13:54:24 2025 +0100

    [#2]: get Publish GitHub Action to work; doc countless issues

commit 389a002dc40dace1e2bc25ac9256fe8f1ce3ae24
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 07:49:31 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 08:01:43 2025 +0100

    [#2]: add third GitHub Action / CI/CD conf: do setup, run `uv publish`;
    
    fails with `error: No files found to publish` (presumably) because
    artifacts / package was built in build workflow, is not available here

commit e7b17d67fecdda8f599b22ad5125f58cd951a6c7
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 07:34:10 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 07:49:51 2025 +0100

    [#2]: add second GitHub Action / CI/CD conf: do setup, run `uv build`;
    
    make this the lead doc: first alphabetically --> likely first looked at

commit 1ad9466feddab549d6c0432c764d5ba7bc0e27f1
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sun Mar 23 07:01:46 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 07:49:51 2025 +0100

    [#2]: add first GitHub Action / CI/CD conf: do setup, run `uv sync`

commit 6ab2ec5f6f7d57f448d2be1ffdc37b532dd93d07
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Sat Mar 22 08:28:09 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:15 2025 +0100

    [#2]: gitlab.com project deploy tokens were rotated: update local copies

commit b111e67cc95a5cbbe51df5a428e0303b256759a0
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 18:38:54 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:15 2025 +0100

    [#2]: review approach to methods: do not return values, but set members;
    
    init members to None so they always exist and to list them all;
    move secrets setup to own method; rename _data_dict to _secrets;
    verify there is at least one logger conf'd, use first if more than one

commit f61895e46e1d64a9749b14653e809b2a2b598546
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 14:58:13 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: refactor to using reviewed conf data model: process console confs,
    
    then process handler confs, finally call dictConfig(...) with the result

commit 9cdf830ed8ff4b2ca8c1083b5c5ddada050ac60a
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 14:52:41 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: adapt to reviewed conf data model: prep log root wherever needed

commit 294d5b5d9e828c0b79d1952505daae089e87ab52
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 14:51:23 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: move sample log output to match flow and simplify coming changes

commit cee34a2fb4505d54c1a6d37661289d8d1a5bd15d
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 12:09:48 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: add conf for console and reference to it in handler conf

commit 6c7391a11cdffbdbad3777ca6e3c321975d17e93
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 12:07:40 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: add pydantic model for rich logging conf extending logging conf

commit a5bc49895c98470f0fabd34f3e349ce569f1d798
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Fri Mar 21 12:04:07 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: add a pydantic model for python logging configuration, many TODOs;
    
    use in own conf file model; add conf: works but logs to stdout, not file

commit 3b2219be4a615b6298b755658484d3ae5e71a6c2
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 18 09:25:51 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: doc issues with rich logging ./. two backends; work around

commit 9cf6a91c95ee3d1389bd7ba9bddcc14d10bb4926
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 18 09:15:35 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: suppress pyright issue; doc keyring issue; add doc and TODO

commit f1e01d4685e9527f53ae2726de5c5d2313755508
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 18 09:14:12 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: enable live issues in VS Code: add VS Code conf file

commit ac5da62bd7933dbe01151d7e1ef33d1ba13469d4
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 18 09:12:59 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: ruff doesn't show any live issues in VS Code; remove:
    
    $ (cd code/python && uv remove --group dev ruff)
        ...

commit 1806b19e505e5485c1470cbbfd53f2fd1d446964
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Thu Mar 13 11:09:54 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: add data file; add to conf file model/conf; use it; add func docs

commit ddd60fe9113d7b266f05754acb6734f29770c717
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 11 19:05:30 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Sun Mar 23 06:53:14 2025 +0100

    [#2]: add conf file model; process conf, set up logging; add conf file

commit 02e8d8237c5ed49f1d114c3c6f44bc2c4bbd36c8
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 11 14:42:22 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:11:44 2025 +0100

    [#2]: $ (cd code/python && uv add platformdirs pydantic PyYAML rich)

commit fd144d6127ddcd8414e179125403cc586bd02592
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 11 14:32:32 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:11:44 2025 +0100

    [#2]: make keyring load backend: conf project entry points; doc issues

commit 7384d791d75f539c6f72c22d4d17fc2ca3d8fa1b
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Tue Mar 11 14:30:25 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:11:44 2025 +0100

    [#2]: implement the very first version of the backend; add py.typed

commit f0333688b0c8a72acc422feef26567d6a2698cd8
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Mon Mar 10 16:29:52 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:11:44 2025 +0100

    [#2]: $ (cd code/python && uv add --group dev ruff)
    
    Resolved 16 packages in 385ms
          Built keyring-insecure-backend @ file:/// [...]
           ... keyring-insecure-backend/code/python
    Prepared 2 packages in 1.18s
    Uninstalled 1 package in 2ms
    Installed 2 packages in 3ms
     ~ keyring-insecure-backend==0.0.0 (from file:/// [...]
        ... keyring-insecure-backend/code/python)
     + ruff==0.9.10

commit 597989ae0e02ecb3f1f5e61711ff48f6f818e105
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Mon Mar 10 16:00:39 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:11:44 2025 +0100

    [#2]: $ (cd code/python && uv add keyring)
    
    Resolved 15 packages in 304ms
          Built keyring-insecure-backend @ file:/// [...]
           ... keyring-insecure-backend/code/python
    Prepared 6 packages in 570ms
    Uninstalled 1 package in 1ms
    Installed 6 packages in 4ms
     + jaraco-classes==3.4.0
     + jaraco-context==6.0.1
     + jaraco-functools==4.1.0
     + keyring==25.6.0
     ~ keyring-insecure-backend==0.0.0 (from file:/// [...]
        ... keyring-insecure-backend/code/python)
     + more-itertools==10.6.0

commit 67473263ea8227db59de9af4c4d5c9d5895f2a40
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Mon Mar 10 15:56:41 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:07:19 2025 +0100

    [#2]: get `uv sync` to work; add uv.lock; done with:
    
    $ (cd code/python && \
         mkdir keyring_insecure_backend && cd $_ && touch __init__.py)

commit df1a25791eb8cd1f74bfc485b8c8e21cbcb48b03
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Mon Mar 10 15:53:22 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Tue Mar 18 09:07:19 2025 +0100

    [#2]: align python project conf with corporate convention, extend:
    
    + add file header, order sections alphabetically, replace " by ',
      add classifiers, description, license; reset version to 0.0.0
    + NOTE: attempting to create a venv at this stage fails with
      $ (cd code/python && uv sync)
          ... (python exception leaked by uv omitted) ...
      ValueError: Unable to determine which files to ship
      inside the wheel using the following heuristics:
      https://hatch.pypa.io/latest/plugins/ ...
       ... builder/wheel/#default-file-selection
    
      The most likely cause of this is that there is no directory that
      matches the name of your project (keyring_insecure_backend).
    
      At least one file selection option must be defined
      in the `tool.hatch.build.targets.wheel` table,
      see: https://hatch.pypa.io/latest/config/build/
    
      As an example, if you intend to ship a directory named `foo` that
      resides within a `src` directory located at the root of your project,
      you can define the following:
    
      [tool.hatch.build.targets.wheel]
      packages = ["src/foo"]
    
      hint: This usually indicates a problem
      with the package or the build environment.

commit f9939c61142def2e4fec17ce1e62c81e4ef83180
Author:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
AuthorDate: Mon Mar 10 15:27:20 2025 +0100
Commit:     Stefan Schablowski <stefan.schablowski@desmodyne.com>
CommitDate: Mon Mar 10 15:46:59 2025 +0100

    [#2]: initialize python project; done with:
    
    $ (cd code/python && \
        uv init --bare \
                --name keyring-insecure-backend \
                --package \
                --python 3.10)

```
