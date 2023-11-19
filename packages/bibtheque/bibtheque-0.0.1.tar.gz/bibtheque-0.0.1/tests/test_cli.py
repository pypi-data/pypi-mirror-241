from click.testing import CliRunner

from config import config
from cli import bibtheque
import test_vars, database

#  ──────────────────────────────────────────────────────────────────────────

config['mongo_db_name'] = 'test_db'

#  ──────────────────────────────────────────────────────────────────────────

# example

# @click.command()
# @click.argument('name')
# def hello(name):
   # click.echo(f'Hello {name}!')

# def test_hello_world():
  # runner = CliRunner()
  # result = runner.invoke(hello, ['Peter'])
  # assert result.exit_code == 0
  # assert result.output == 'Hello Peter!\n'

#  ──────────────────────────────────────────────────────────────────────────
# running tests

def test_insert():
    runner = CliRunner()
    result = runner.invoke(bibtheque, ['--config', config, 'insert', '--file', 'test.pdf', '-n', 'test notes for test pdf', '--tags', 'test, tags, here', '--force', test_vars.doi_url])
    # print(result.output)
    assert result.exit_code == 0


def test_search():
    runner = CliRunner()
    result = runner.invoke(bibtheque, ['--config', config, 'search', 'notes'])
    # print(result.output)
    assert result.exit_code == 0


def test_regex():
    runner = CliRunner()
    result = runner.invoke(bibtheque, ['--config', config, 'regex', '--fields', 'tags', 'here'])
    print(result.output)
    assert result.exit_code == 0


#  ──────────────────────────────────────────────────────────────────────────
# cleaning test database

def clean(config):
    DB = database.Database(config)
    DB.delete()

clean(config)
