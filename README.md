# Documentation

## Introduction

This documentation describes a simple FLASK CRUD backend server that is deployed on the google cloud with help of google cloud run.

**server link:** https://user-crud-ynt2dr7ida-uc.a.run.app/

## Table of Contents

1. [Getting Started](#gettingStarted)
2. [GCP or Firebase Firestore configuration](#firestore)
3. [API documentation](#API)
4. [Google cloud run deployment](#cloudRun)

<a name="gettingStarted"></a>

## Getting Started

### Prerequisites

Before you begin make sure you have following items installed on your system:

- python
- git

#### Installation

To install and set up the project on your local machine, follow these steps:

1. Clone the Git repository using the following command:

   ```bash
   git clone https://github.com/aapanm/CRUD-with-flask
   ```

2. Change to the project directory:

   ```bash
   cd user-operation-system
   ```

3. Activate virtual environment

- for windows

```bash
   .venv\Scripts\activate
```

- for linux/mac

```bash
   .venv/bin/activate
```

4. Installing dependencies

```bash
   pip install requirements.txt
```

5. running the app

- development server

```bash
	flask --app main run --debug
```

- production with gunicorn

```bash
	gunicorn --bind 0.0.0.0:8000 main:app
```

**N.B** Running this app for the first time will end up giving error regrading firestore key configuration. To fix this please see the following section.

<a name="firestore"></a>

## GCP and Firebase Firestore

Firestore is a flexible and scalable cloud-based NoSQL document database provided by Google Cloud Platform (GCP). It uses the Firebase Realtime Database's powerful real-time engine, enabling instant updates whenever data changes.

To create a firestore database there two options, using 1.Firebase 2. GCP console

### Firebase Firestore

To create Firestore database in Firebase you will need to create or use a existing firebase project with location and then select firestore. While selecting firestore, opt for test mode to avoid authentication process in the development procedure. Then download firebase service account key, settings > service account, and after that select Python option for Admin SDK configuration snippet, click Generate new private key, and save it as key.json.

User following code in the `userService.py` file

```python
	from firebase_admin import credentials, firestore, initialize_app
	cred = credentials.Certificate(**path to key.json**)
	default_app = initialize_app(cred)
	db = firestore.client()
```

### Accessing Firestore from GCP console

To access Firestore from gcp console you will have to follow following steps:

- Open gcp account, with only credit/debit information gcp provides $300 free credit available for 3 months.
- Create a project
- Enable Firestore API
- Create a database in the firestore

Now, while configuring firebase we downloaded service account key, similarly here we also need to gcp service account key to configure and authenticate firestore in the google cloud provider to run the database locally. Also while depolying in the gcp we also need to select the service account authentication.

There are seveal ways to create a gcp service account key, In the gcp console after selecting your project, go to IAM > service accounts > create service account > generate service key, this will download the service key.json.

**set up authentication locally (windows)**

Open a powersell and write following command:

```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH to servie key.json"
```

this will set an envireonment variable for that active shell session only, make sure you run your app within that session.

After setting up environment variable, add following codes in the `userService.py`,

```python
from google.cloud import firestore
db = firestore.Client(project="your gcp project id")
```

If you have any doubts, please follow this article:

https://cloud.google.com/firestore/docs/create-database-server-client-library

<a name="API"></a>

## API documentation

**Database information:** The following code in the `userService.py` with create a collection named user-crud if not exists, in the firestore database.

```python
user_ref = db.collection('user-crud')
```

This ia simple crud api, with GET, POST, PATCH, DELETE methods

**Base URL:** https://user-crud-ynt2dr7ida-uc.a.run.app/

### Get all users

- **URL**: `/users`
- **Method**: `GET`
- **Description**: When triggered it fethces all users data
- **Response**:

```json
[
  {
    "userId": 301,
    "userName": "Mutsuddy"
  },
  {
    "userId": 302,
    "userName": "Aapan Mutsuddy"
  }
]
```

### Get specific user data

- **URL**: `/users/{userId}`
- **Method**: `GET`
- **Path Param**: `userId`
- **Description**: When triggered it fethces relevant user data associated with user id provided in the path parameter
- **Response**:

```json
{
  "userId": 301,
  "userName": "Mutsuddy"
}
```

### create user data

- **URL**: `/users`
- **Method**: `POST`
- **Request body**: `{"userId": 301, "userName": "Mutsuddy"}`
- **Description**: When triggered it creates user data provided in the request body
- **Response**:

```json
{
  "data": {
    "userId": 301,
    "userName": "Mutsuddy"
  },
  "success": true
}
```

### update user data

- **URL**: `/users`
- **Method**: `PATCH`
- **Request body**: `{"userId": 301, "userName": "Aapan"}`
- **Description**: When triggered it updates user data provided in the request body
- **Response**:

```json
{
  "data": {
    "userId": 301,
    "userName": "Aapan"
  },
  "success": true
}
```

### Delete user data

- **URL**: `/users/{userId}`
- **Method**: `DELETE`
- **Path Param**: `userId`
- **Description**: When triggered it deletes relevant user data associated with user id provided in the path parameter
- **Response**:

```json
{
  "success": true
}
```

<a name="cloudRun"></a>

## Google cloud run deployment

**Docker file**

To deploy, the application in the google cloud run, we will use docker image, which will be uploaded in the google container registry. Then, from google cloud run project we will use that image to deply our application.

The `Dockerfile` file contains all the necessary codes to generate the docke image. To generate image use following codes:

- building image

```bash
docker build -t <desired image name> .
```

We can also test the docker image locally by running,

```bash
docker run -it -8000:8000 <desired image name>
```

- uploading docker image to docker hub

```bash
docker login
docker tag <desired image name> <docker hub id>/<desired image name>
docker push <docker id>/<desired image name>
```

Now, we can pull this docker image to our google container registry and deploy to cloud run.

In the gcp console, open terminal and put following codes:

- enabling container registry api

```bash
gcloud services enable containerregistry.googleapis.com
```

- pullig docker image

```bash
docker pull <docker hub id>/<desired image name>
docker tag <docker hub id>/<desired image-= name> gcr.io/<gcp project id>/<desired image name>
docker push gcr.io/<gcp project id>/<desired image name>
```

So far, our application docker image is now uploaded in the container registry, now we have to create a service in the cloud run. Add necessary configuration and select uploaded image. In the container settings, set port number specified in the docker file. Then select unauthenticated invocations to make deployment public. After some time application will be deployed and an URL will be generated.

# Conclusion

In this documentation, I tried to mention all the steps I have followed to deploy a simple flask crud application in the google cloud run.
