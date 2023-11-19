import click
import sys
import subprocess
from pathlib import Path

#  ──────────────────────────────────────────────────────────────────────────
# local imports

import database, bibtex, document
from config import config

#  ──────────────────────────────────────────────────────────────────────────
# global variables

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

#  ──────────────────────────────────────────────────────────────────────────

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--config', type=dict, default=config)
@click.pass_context
def bibtheque(ctx, config):
    """A tool to manage bibliographic items, particularily for research.
    """
    ctx.obj = database.Database(config)

#  ──────────────────────────────────────────────────────────────────────────
# Insert

@click.command()
@click.option('-f', '--file', 'file', default=None, help='PDF file path', type=str)
@click.option('-a', '--annotated', 'annotated', default=None, help='Annotated PDF file path', type=str)
@click.option('-t', '--tags', 'tags', default='', help='Comma delimited tags')
@click.option('-n', '--notes', 'notes', default='', help='Additional notes', type=str)
@click.option('-s', '--synopsis', 'synopsis', default='', help='Synopsis of the work', type=str)
@click.option('--force', is_flag=True, default=False, show_default=True, help='Force insert of document', type=bool)
@click.argument('standard', type=str)
@click.pass_obj
def insert(DB, file, annotated, tags, notes, synopsis, force, standard):
    """Insert a document into the database."""

    doc_bib_dict = document.determine_standard(standard)

    # listifying tags
    tmp = tags.split(',')
    tags = []
    for tag in tmp:
        tags.append(tag.strip())

    if file:
        file_id, file_text = database.ingest_pdf(file, DB.fs)
    else:
        file_id, file_text = None, None
    
    if annotated:
        annotated_file_id, annotated_file_text = database.ingest_pdf(annotated, DB.fs)
    else:
        annotated_file_id, annotated_file_text = None, None
    
    doc = document.build_doc(doc_bib_dict, file_id=file_id, file_text=file_text, annotated_file_id=annotated_file_id, annotated_file_text=annotated_file_text, tags=tags, notes=notes, synopsis=synopsis)

    doc_id = database.insert(doc, DB.documents, force=force)

bibtheque.add_command(insert)

#  ──────────────────────────────────────────────────────────────────────────
# Search

@click.command()
@click.argument('search_text', default='')
@click.pass_obj
def search(DB, search_text):
    """Searches the database with SEARCH_TEXT.

    If left blank, returns all items in the database.
    """

    if search_text:
        results = database.search(search_text, DB.documents)
    else:
        results = DB.documents.find()

    for result in results:
        print(result)

bibtheque.add_command(search)

#  ──────────────────────────────────────────────────────────────────────────
# Regex

@click.command()
@click.option('-s', '--show-all', 'show_all', is_flag=True, default=False, help='Show all fields, regardless of fields searched')
@click.option('-f', '--fields', 'regex_fields', default=None, help='Comma delimited document fields to Regex search')
@click.argument('regex_text')
@click.pass_obj
def regex(DB, show_all, regex_fields, regex_text):
    """Searches the database via regex with REGEX_TEXT."""

    # listifying fields
    tmp = regex_fields.split(',')
    regex_fields = []
    for regex_field in tmp:
        regex_fields.append(regex_field.strip())

    results = database.regex(regex_text, DB.documents, regex_fields=regex_fields, show_all=show_all)
    
    for result in results:
        print(result)

bibtheque.add_command(regex)

#  ──────────────────────────────────────────────────────────────────────────
# Modify

@click.command()
@click.argument('doc_id')
@click.pass_obj
def modify(DB, doc_id):
    """Opens the default text editor to edit the document with the given DOC_ID."""

    database.modify(doc_id, DB.documents)

bibtheque.add_command(modify)

#  ──────────────────────────────────────────────────────────────────────────
# Delete

@click.command()
@click.argument('doc_id')
@click.pass_obj
def delete(DB, doc_id):
    """Deletes the document with the given DOC_ID."""

    confirm = input('Are you sure you want to delete this document? y/[n] ')
    confirm = confirm.strip()

    if confirm:
        if confirm in ['y', 'yes']:
            database.delete(doc_id, DB.documents, DB.fs)
        elif confirm in ['n', 'no']:
            print('Aborted')

    else:
        print('Aborted')

bibtheque.add_command(delete)

#  ──────────────────────────────────────────────────────────────────────────
# Write out

@click.command()
@click.option('-a', '--annotated', 'annotated', is_flag=True, default=False, help='Writes out annotated file')
@click.option('-f', '--file', 'file', default=None, help='Path to write out PDF file to')
@click.argument('doc_id', type=str)
@click.pass_obj
def write(DB, annotated, file, doc_id):
    """Writes PDF from database to FILE path."""

    if file:
        database.write_pdf(file, doc_id, DB.fs, annotated_file=annotated)
    else:
        file = doc_id + '.pdf'
        database.write_pdf(file, doc_id, DB.fs, annotated_file=annotated)

bibtheque.add_command(write)

#  ──────────────────────────────────────────────────────────────────────────
# Bib

@click.command()
@click.argument('tags', nargs=-1)
@click.pass_obj
def bib(DB, tags):
    """Prints BibTeX entries for the given TAGS."""

    bib_str = database.bib(tags, DB.documents)
    
    print(bib_str)

bibtheque.add_command(bib)

#  ──────────────────────────────────────────────────────────────────────────
# Clean up database

@click.command()
@click.pass_obj
def clean(DB):
    """MongoDB doesn't release space when an entry is deleted. This forces the database to garbage collect."""

    # cleaning documents
    database.clean_up(DB.db)

    # cleaning GridFS database
    database.clean_up(DB.db_fs)

bibtheque.add_command(clean)

