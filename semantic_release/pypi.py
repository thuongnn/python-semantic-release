"""PyPI
"""
from invoke import run


def upload_to_pypi(
        dists: str = 'sdist bdist_wheel',
        username: str = None,
        password: str = None,
):
    """Creates the wheel and uploads to pypi with twine.

    :param dists: The dists string passed to setup.py. Default: 'bdist_wheel'
    :param username: PyPI account username string
    :param password: PyPI account password string
    """
    run('python setup.py {}'.format(dists))
    run('twine upload -u {} -p {}'.format(username, password))
    run('rm -rf build dist')
