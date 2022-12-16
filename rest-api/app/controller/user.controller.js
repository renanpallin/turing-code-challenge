const { Router } = require('express');
const userService = require('../service/user.service');

const userRouter = Router();

/**
 * List all users
 * You can filter with `name` and `email` query strings
 */
userRouter.get('/', async (req, res) => {
  const users = await userService.getAll(req.query);
  res.json(users);
});

/**
 * Get a spefic user by its id
 */
userRouter.get('/:id', async (req, res) => {
  const user = await userService.getById(req.params.id);
  if (user) return res.json(user);
  res.status(404).json(null);
});

/**
 * Create a user
 */
userRouter.post('/', async (req, res) => {
  const user = await userService.create(req.body);
  res.status(201).json(user);
});

/**
 * Update a user
 */
userRouter.put('/:id', async (req, res) => {
  const updatedUser = await userService.update(req.params.id, req.body);
  if (updatedUser) return res.json(updatedUser);
  res.status(404).json(null);
});

/**
 * Delete a user
 */
userRouter.delete('/:id', async (req, res) => {
  const deletedUser = await userService.deleteById(req.params.id);
  if (deletedUser) return res.json(deletedUser);
  res.status(404).json(null);
});

module.exports = userRouter;
