const mongoose = require('mongoose');

const mongoUrl = process.env.MONGO_DB_URL || 'mongodb://localhost:27017/test';
async function connectToMongo() {
  try {
    mongoose.set('strictQuery', true);
    console.log(`Connecting to database...`);
    await mongoose.connect(mongoUrl, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('Connected to MongoDB');
  } catch (error) {
    console.error('Could not connect to MongoDB:', error);
  }
}

module.exports = connectToMongo;
