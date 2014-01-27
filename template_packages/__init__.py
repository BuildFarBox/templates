#coding: utf8
import os
from utils import get_hash_key, smart_unicode
from utils.exchange import jade2jinja
from bson import Binary
from configs.database import db
from utils.path import to_template_key
import cPickle as pickle
import datetime

CORE_TEMPLATE_EXTS = ['.jade','.html', '.htm']

PKS_ROOT = os.path.dirname(__file__)
PKS_STATUS_FILE = os.path.join(PKS_ROOT, 'pks.txt')

def get_template_folders():
    folders = []
    for name in os.listdir(PKS_ROOT):
        folder_path = os.path.join(PKS_ROOT, name)
        if os.path.isdir(folder_path):
            folders.append(folder_path)
    return folders



def dump_folder_to_db(folder):
    folder_name = folder.replace(PKS_ROOT, '').strip('/')

    files = []
    for dir_path, dir_names, filenames in os.walk(folder):
        if '/.' in dir_path:
            continue
        for filename in filenames:
            if filename.lower().split('.')[0] in ['license', 'readme']:
                # 版权 & readme不dump到数据库
                continue
            if not filename.startswith('.'):
                files.append(os.path.join(dir_path, filename))
            else:
                continue

    resources = {}

    for fi in files:
        pk_dir_name, t_filename = fi.replace(PKS_ROOT, '').strip('/').split('/', 1)

        with open(fi) as f:
            content = f.read()
        hash_key = get_hash_key(content)

        ext = os.path.splitext(fi)[1].lower()


        if ext in CORE_TEMPLATE_EXTS:
            content = smart_unicode(content)
            if ext == '.jade':
                content = jade2jinja.exchange(content)
        else:
            content = Binary(content)

        if not db.template.exists(hash_key): # save the content with hash into database
            template_doc = dict(
                _id = hash_key,
                content = content,
                path = t_filename,
                date = datetime.datetime.utcnow()
            )
            db.template.save(template_doc)

        resources[to_template_key(t_filename)] = hash_key

    # save the template_package info into database
    template_package_name = folder_name.title()
    pk_id = get_hash_key('farbox'+template_package_name.lower())

    pk_doc = dict(
        _id = pk_id,
        title = template_package_name,
        resources = resources,
    )

    db.template_package.save_doc(pk_doc, just_save=True)


    return {'template_key': pk_id, 'title': template_package_name}


def dump_template_packages():
    pks = []
    for folder in get_template_folders():
        pks.append(dump_folder_to_db(folder))
    with open(PKS_STATUS_FILE, 'w') as f:
        pickle.dump(pks, f)
    return pks


def get_template_packages():
    if not os.path.isfile(PKS_STATUS_FILE):
        dump_template_packages()
    try:
        with open(PKS_STATUS_FILE) as f:
            return pickle.load(f)
    except:
        return []


