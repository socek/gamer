# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'hatak==0.2.3',
    'coverage',
    'hatak_logging',
    'hatak_jinja2',
    'hatak_haml',
    'hatak_sql',
    'hatak_alembic',
    'hatak_beaker',
    'hatak_debugtoolbar',
    'hatak_toster',
    'hatak_statics',
    'waitress',
    'uwsgi',

]
dependency_links = [

]

if __name__ == '__main__':
    setup(
        name='gamer',
        version='0.1',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        dependency_links=dependency_links,
        include_package_data=True,
        entry_points="""
            [paste.app_factory]
                main = gamer.application.init:main
            [console_scripts]
                gamer_manage = gamer.application.manage:run
          """,
    )
