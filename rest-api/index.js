const express = require('express');
const bodyParser = require('body-parser');

require('dotenv-safe').config();

const userRouter = require('./app/controller/user.controller');
const connectToMongo = require('./app/db/connection');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

app.use('/user', userRouter);

app.get('/', (req, res) => {
  res.json({
    author: 'Renan Pallin',
    description: 'CRUD using MongoDb',
    routes: {
      'GET /user': 'List all users (filter with ?name=<name>&email=<email>)',
      'GET /user/:id': 'Get a user',
      'POST /user': 'Create a user',
      'PUT /user/:id': 'Update a user',
      'DELETE /user/:id': 'Delete a user',
    },
  });
});

async function main() {
  await connectToMongo();
  app.listen(port, () => console.log(`Server running at ${port}`));
}
main();
