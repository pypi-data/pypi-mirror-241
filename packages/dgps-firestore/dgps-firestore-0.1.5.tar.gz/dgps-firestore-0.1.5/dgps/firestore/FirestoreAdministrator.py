import datetime
import logging
import re
import traceback
import uuid

import pytz
from google.cloud import firestore

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


class DocumentNotFoundError(Exception):
    pass


class FirestoreAdministrator:
    def __init__(self, singleton=False):
        # self.db = firestore.AsyncClient()
        self.db = firestore.Client()
        self._is_singleton = singleton

    def increment_field(self, collection_id, document_id, increment_dict):
        def key_transform(key):
            return re.sub(r"[^\w.]+", "", key)

        try:
            ref = self.db.collection(str(collection_id)).document(str(document_id))
            for key, _ in increment_dict.items():
                new_key = key_transform(key)
                if new_key != key:
                    LOG.info(f"renaming {key} to {new_key}")
            firestore_increment_dict = {
                key_transform(key): firestore.Increment(value)
                for key, value in increment_dict.items()
            }
            LOG.info(f"incrementing {increment_dict} in {collection_id} {document_id}")
            ref.update(firestore_increment_dict)
        except Exception as exc:
            error_text = (
                "Exception while incrementing firestore field.\n"
                f"collection: {collection_id}\n"
                f"document: {document_id}\n"
                f"increment_dict: {increment_dict}\n"
                f"Stacktrace:\n{traceback.format_exc()}\n"
                f"Exception: {exc}"
            )
            LOG.error(error_text)

    def add_document_to_collection(self, collection_id, document_id, data):
        try:
            doc_ref = self.db.collection(str(collection_id)).document(str(document_id))
            data["firestore_creation_timestamp"] = firestore.SERVER_TIMESTAMP
            doc_ref.set(data, merge=True)
            now = datetime.datetime.now(pytz.utc)
            datetime_string = now.strftime("%Y-%m-%d--%H-%M-%Z")
            data["firestore_creation_timestamp"] = datetime_string
            LOG.info(
                f"Added {document_id} document to {collection_id} firestore collection."
            )
        except Exception as exc:
            error_text = (
                "Exception while while writing to firestore.\n"
                f"collection: {collection_id}\n"
                f"document: {document_id}\n"
                f"data: {data}\n"
                f"Stacktrace:\n{traceback.format_exc()}\n"
                f"Exception: {exc}"
            )
            LOG.error(error_text)

    # def get_firebase_doc_dict(self, collection_id, document_id):
    #     collection_ref = self.db.collection(str(collection_id))
    #     doc_ref = collection_ref.document(str(document_id))
    #     doc = doc_ref.get()
    #     if doc.exists:
    #         return doc.to_dict()
    #     else:
    #         return None

    def delete_document_from_collection(self, collection_id, document_id):
        document_found = True
        try:
            doc_ref = self.db.collection(str(collection_id)).document(str(document_id))
            if doc_ref.get().exists:
                doc_ref.delete()
                LOG.info(
                    f"Deleted {document_id} document from {collection_id} firestore collection."
                )
            else:
                LOG.info(
                    f"Document {document_id} does not exist in {collection_id} firestore collection."
                )
                document_found = False
        except Exception as exc:
            error_text = (
                "Exception while attempting to delete from firestore.\n"
                f"collection: {collection_id}\n"
                f"document: {document_id}\n"
                f"Stacktrace:\n{traceback.format_exc()}\n"
                f"Exception: {exc}"
            )
            LOG.error(error_text)
        if not document_found:
            raise DocumentNotFoundError(
                f"Document {document_id} does not exist in {collection_id} firestore collection."
            )

    def update_document_in_collection(self, collection_id, document_id, data):
        try:
            current_datetime = datetime.datetime.now(pytz.utc)
            current_datestamp = current_datetime.strftime("%Y-%m-%d_%H:%M:%S_%Z%z")
            uuid4 = str(uuid.uuid4())
            doc_dict = self.get_firebase_doc_dict(collection_id, document_id)
            if doc_dict is not None:
                new_collection_id = collection_id + "_archive"
                new_document_id = (
                    document_id + "_" + current_datestamp + "_" + str(uuid4)
                )
                self.add_document_to_collection(
                    new_collection_id, new_document_id, doc_dict
                )
            self.add_document_to_collection(collection_id, document_id, data)
        except Exception as exc:
            LOG.error("Exception while writing to firestore.")
            LOG.error(f"collection: {collection_id}")
            LOG.error(f"document: {document_id}")
            LOG.error(f"data: {data}")
            LOG.error(f"Stacktrace: {traceback.print_stack()}")
            LOG.error(f"Exception: {exc}")

    def document_exists(self, collection_id, document_id):
        doc_ref = self.db.collection(str(collection_id)).document(str(document_id))
        return doc_ref.get().exists

    def query_firebase(self, collection_id, document_id, query):
        doc_dict = self.get_firebase_doc_dict(collection_id, document_id)
        if doc_dict is not None:
            return doc_dict[query]
        else:
            return None

    # def get_firebase_docs(self, collection_id):
    #     collection_ref = self.db.collection(str(collection_id))
    #     docs_ref = collection_ref.stream()

    #     for doc in docs_ref:
    #         print(f'{doc.id} => {doc.to_dict()}')

    def get_firebase_doc_dict(self, collection_id, document_id):
        collection_ref = self.db.collection(str(collection_id))
        doc_ref = collection_ref.document(str(document_id))
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def list_collections(self):
        return [col.id for col in self.db.collections()]


_singleton_instance = None


def get_firestore_administrator(singleton=True):
    global _singleton_instance
    if singleton:
        if _singleton_instance is None:
            _singleton_instance = FirestoreAdministrator(singleton=True)
        return _singleton_instance
    else:
        return FirestoreAdministrator(singleton=False)


if __name__ == "__main__":
    fs_admin_singleton = get_firestore_administrator()
    print(fs_admin_singleton.list_collections())


# Usage:
# # To get a singleton instance:
# fs_admin_singleton = get_firestore_administrator()

# # To get a new, non-singleton instance:
# fs_admin_non_singleton = get_firestore_administrator(singleton=False)

# # # Assume these functions are defined to convert your objects to and from dictionaries
# def object_to_dict(obj):
#     # Implement this function based on your object structure
#     return obj.model_dump(
#         exclude_defaults=True,
#         exclude_none=True,
#     )

# def dict_to_object(dict_obj, obj_class):
#     # Implement this function based on your object structure
#     return obj_class.load_from_model(dict_obj)

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# def get_object(obj_id, obj_class, collection_id):
#     doc_ref = db.collection(collection_id).document(obj_id)
#     doc_dict = doc_ref.get().to_dict()
#     return dict_to_object(doc_dict, obj_class)

# # Example Usage
# # Assume `voter` is an instance of Voter class
# save_object(voter, 'Voters')

# # To get the object back from Firestore
# retrieved_voter = get_object(voter.prefix + voter.id, Voter, 'Voters')
