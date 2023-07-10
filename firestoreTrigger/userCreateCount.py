from google.cloud import firestore

db = firestore.Client(project="user-crud-391515")
count_ref = db.collection("user-count")


def main(event, context):
    count_ref.document("createCount").update({"value": firestore.Increment(1)})
    print("document created!")
