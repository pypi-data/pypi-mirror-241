from pymongo import MongoClient, TEXT
from gridfs import GridFS
from pypdf import PdfReader
from click import edit
import json
import os

import fields, bibtex, document

#  ──────────────────────────────────────────────────────────────────────────
# PDF file management

def ingest_pdf(file_in_path, fs):
    """Extracts text from PDF and saves to database"""

    # extracting text
    readpdf = PdfReader(file_in_path)
    pdf_text = ''
    for page in readpdf.pages:
        pdf_text += page.extract_text()

    # opening to insert into database
    with open(file_in_path, 'rb') as file:
        file_bytes = file.read()

    # inserting
    file_id = fs.put(file_bytes)

    return file_id, pdf_text


def write_pdf(file_out_path, doc_id, documents, fs, annotated_file=False):
    """Writes out PDF"""

    if annotated_file:
        tmp_id = 'file_id'
    else:
        tmp_id = 'annotated_file_id'

    file_id = documents.find_one(doc_id)[tmp_id]
    
    if file_id:
        file_bytes = fs.get(file_id).read()

        with open(file_out_path, 'wb') as file:
            file.write(file_bytes)

    else:
        print('Document does not have a pdf in the database')


def bib(tags, documents):
    """Builds BibTeX string from given tags"""

    results = in_tags(tags, documents)
    
    bib_str = ''
    for i, doc in enumerate(results):
        doc_id = doc['_id']
        doc = documents.find_one(doc_id)

        tmp_dict = {}
        for field in doc.keys():
            if field in fields.required[doc['type']] + fields.optional[doc['type']]:
                tmp_dict[field] = doc[field]

        bib_str += document.build_bib(tmp_dict)

        if i > 0:
            bib_str += "\n"
    
    return bib_str

#  ──────────────────────────────────────────────────────────────────────────
# Document management

def find_duplicates(doc, documents):
    """Finds duplicates in the database"""

    found_duplicate = False
    duplicates = {}
    for field in doc.keys():
        duplicates[field] = []
        tmp = documents.find({field: doc[field]})
        for tmpi in tmp:
            duplicates[field].append(tmpi)

        if len(duplicates[field]) > 0:
            found_duplicate = True

    return found_duplicate, duplicates


def insert(doc, documents, force=False):
    """Inserts document"""

    found_duplicate, duplicates = find_duplicates(doc, documents)

    if force:
        doc_id = documents.insert_one(doc).inserted_id

    elif not found_duplicate:
        doc_id = documents.insert_one(doc).inserted_id

    else:
        doc_id = None
        print('Document not added, duplicates found')

    return doc_id


def search(search_text, documents):
    """Searches through database"""

    results = documents.find({"$text": {"$search": search_text}})

    search_results = []
    for result in results:
        search_results.append(result)

    return search_results


def regex(regex_text, documents, regex_fields=None, show_all=False):
    """Regex searches database"""

    if regex_fields:
        search_fields = []
        show_fields = {}
        for field in regex_fields:
            if field in fields.all_fields:
                print(field)
                search_fields.append({ field: {'$regex': regex_text} })
                show_fields[field] = True
            else:
                print(field + ' not in allowable search fields.')

    else:
        search_fields = []
        show_fields = {}
        for field in fields.all_fields:
            search_fields.append({ field: {'$regex': regex_text} })
            show_fields[field] = True

    if show_all:
        results = documents.find({"$or": search_fields})

    else:
        results = documents.find({"$or": search_fields}, show_fields)

    regex_results = []
    for result in results:
        regex_results.append(result)

    return regex_results


def in_tags(tags, documents):
    """Regex search through tags"""

    tmp = documents.find({'tags': {"$in": tags}})
    results = []
    for result in tmp:
        results.append(result)

    return results


def modify(doc_id, documents):
    """Modifies document"""

    doc = documents.find_one(doc_id)

    tmp = {}
    for key in doc.keys():
        if key not in ['_id', 'file_id', 'annotated_file_id']:
            tmp[key] = doc[key]

    tmp = json.dumps(tmp)
    tmp = edit(tmp, extension='.json')
    if tmp:
        edited_doc = json.loads(tmp)
        documents.update_one({'_id': doc['_id']}, {'$set': edited_doc})
    else:
        print("No changes made.")


def delete(doc_id, documents, fs):
    """Deletes document"""

    doc = documents.find_one(doc_id)

    if doc:

        if doc['file_id']:
            fs.delete(doc['file_id'])

        if doc['annotated_file_id']:
            fs.delete(doc['annotated_file_id'])

        documents.delete_one({'_id': doc_id})
    
    else:
        print('Document does not exist')


def clean_up(db):
    """Garbage collect database"""

    for collection in db.list_collection_names():
        db.command('compact', collection)

#  ──────────────────────────────────────────────────────────────────────────

class Database():

    def __init__(self, config):

        self.config = config
        self.client = MongoClient('mongodb://root:' + self.config['root_password'] + '@' + self.config['mongo_db_ip'] + ':27017/')
        self.db = self.client[self.config['mongo_db_name']]
        self.documents = self.db['documents']

        # allowing for searchable text fields
        self.documents.create_index([('$**', TEXT)])

        self.db_fs = self.client[self.config['mongo_db_name'] + '_gridfs']
        self.fs = GridFS(self.db_fs)


    def delete(self):
        
        self.client.drop_database(self.config['mongo_db_name'])
        self.client.drop_database(self.config['mongo_db_name'] + '_gridfs')
