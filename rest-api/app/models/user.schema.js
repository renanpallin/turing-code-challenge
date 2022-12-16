const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  id: String,
  name: String,
  email: String,
});

const User = mongoose.model('User', UserSchema);

module.exports = User;
