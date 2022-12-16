# REST API - Users

This is a REST API for Users using Node JS and MongoDB.

## Environment Variables

You will find a `.env.example` with a empty `MONGO_DB_URL=`.
Copy this file and rename it for just `.env` and put a connection string for a running MongoDB instance.

Example

```bash
MONGO_DB_URL=<my-mongodb-connection-string>
```

A instance is provided with this project and can be used for test this project.

## Running the project

```bash
# install dependencies
npm install

# running the project
npm start
```

You should see the app running at default port 3000.
You can change the port for this application setting a environment variable named PORT

# How to use this API

Make a GET request to `http://localhost:3000/` or just open in your browser.
You will be able to see a list of all routes and a short description.

| Route            | Description                                             |
| ---------------- | ------------------------------------------------------- |
| GET /user:       | List all users (filter with ?name=<name>&email=<email>) |
| GET /user/:id    | Get a user                                              |
| POST /user       | Create a user                                           |
| PUT /user/:id    | Update a user                                           |
| DELETE /user/:id | Delete a user                                           |

You can filter your data using `name` and `email` query string paramm, like in `http://localhost:3000/user?name=Renan`

## Author

Renan Pallin
renanpallin@gmail.com
