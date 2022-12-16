const User = require('../models/user.schema');

const userService = {
  getAll: async ({ name, email } = {}) => {
    const query = {};
    if (name) query.name = new RegExp(name, 'gmi');
    if (email) query.email = new RegExp(email, 'gmi');

    const users = await User.find(query);
    return users;
  },
  getById: async (id) => {
    try {
      const user = await User.findById(id);
      return user;
    } catch (error) {
      console.error(error);
      return null;
    }
  },
  create: ({ name, email }) => {
    const userData = {
      name,
      email,
    };
    return User.create(userData);
  },
  update: async (id, { name, email }) => {
    try {
      const userData = {
        name,
        email,
      };

      return await User.findByIdAndUpdate(id, userData);
    } catch (error) {
      console.error(error);
      return null;
    }
  },
  deleteById: async (_id) => {
    try {
      return await User.findByIdAndDelete(_id);
    } catch (error) {
      console.error(error);
      return null;
    }
  },
};

module.exports = userService;
