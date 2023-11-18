# Sola Python Utils

## 使い方

### Pyenv

```bash
which python
```

install specific version of python

```bash
pyenv install --list
pyenv install PYTHON_VERSION
```

set global python version

```bash
pyenv local PYTHON_VERSION
pyenv global PYTHON_VERSION
python --version
```

### Poetry

poetry自体のupdate

```bash
poetry self update
```

add library

```bash
poetry add LIBRARY_NAME
```

install

```bash
poetry install
```

build

```bash
poetry build
```

run

```bash
poetry run python SRC_PATH
```

update poetry lock file

```bash
poetry lock
```

### Publish

1. [PiPI](https://pypi.org/)で会員登録
2. メールアドレス認証
3. recovery codesの発行+2段階認証の登録
4. APIトークンの生成
5. publish前にtokenの登録

```bash
poetry config pypi-token.testpypi TOKEN #TestPyPI
poetry config pypi-token.pypi TOKEN # PyPI
```

6. URL登録 if TestPyPI

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/ #TestPyPI
```

7. publish

```bash
poetry publish -r testpypi #TestPyPI
poetry publish #PyPI
```

## Reference

pyenv + poetry

> https://dev.classmethod.jp/articles/pyenv-and-poetry/
>
> https://zenn.dev/tk_resilie/articles/python_my_best_project

### requirements.txtでgitlab上のライブラリを参照

```txt
git+https://oauth2:SECRET_KEY@gitlab.com/REPOSITORY_URL
```
