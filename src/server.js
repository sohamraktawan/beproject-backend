const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
require('dotenv').config()


const app = express();
const port = 3000;


mongoose.connect(process.env.db_connect, { useNewUrlParser: true, useUnifiedTopology: true });

const User = mongoose.model('User', {
  name: String,
  dept: String
});

app.use(bodyParser.json());


app.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});


app.post('/users', async (req, res) => {
  try {
    const { name, dept } = req.body;
    
    
    const newUser = new User({
      name,
      dept
    });

    
    await newUser.save();

    res.json({ message: 'User added successfully', user: newUser });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
