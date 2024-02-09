const express = require("express");
const app = express();
const cors = require("cors");
const mongoose = require("mongoose");
const cookieParser = require('cookie-parser')
require('dotenv').config();
const dotenv = require('dotenv');
const path = require('path')
const { isEmail, isEmpty, isStrongPassword } = require("validator")
const jwt = require("jsonwebtoken")
const bcrypt = require("bcryptjs")



app.use(cors());
app.use(cookieParser());
app.use(express.json());

const dbURI = process.env.db_connect

mongoose.connect(dbURI,{ useNewUrlParser: true, useUnifiedTopology: true })
.then(res=>{
    console.log("connected to db")
})
.catch(err=>{
    console.log(err);
});

const taskSchema = new mongoose.Schema({
  username:String,
  title:String,
  desc:String,
  timeDue:Number,
  priority:String,
  status:String

},{versionKey:false})


const Task = mongoose.model("task", taskSchema);

const UserSchema = new mongoose.Schema({
    username:{
        type: String,
        required: [true, 'Please enter an username'],
        unique: true,

    },
    email:{
        type: String,
        required:[true, "Please enter an email"],
        unique: true,
        validate: [isEmail, "Please enter a valid email"]
    },
    password:{
        type: String,
        
        required: [true, 'Please enter a password'],
        minlength: [6, "The password should be atleast 6 characters long"],
        validate:[isStrongPassword, 'Please enter a  strong password']

    },

}, {versionKey:false})

UserSchema.statics.login = async function(email,password){
    const user = await this.findOne({ email });
    if(user){
        const auth = await bcrypt.compare(password, user.password)
        console.log(password)
        console.log(user.password)

        if(auth){
            return user
        }
        throw Error('incorrect password')
    }
    throw Error('incorrect email')
}

const User = mongoose.model('user', UserSchema);

app.post('/signup', async (req, res) => {

    let {username, email,password} = req.body;
    try{
        const salt = await bcrypt.genSalt();
        password = await bcrypt.hash(password, salt);
        let postsLiked = []
        let postsDisliked = []
        const user = await User.create({username, email, password, postsLiked, postsDisliked});
        const token = createToken(user._id);
        res.send(token);
        res.status(201).json(user);
    }
    catch(err){
        console.log(err);
        errors = handleErrors(err);
        console.log(errors);
        res.status(201).json({errors:errors});

    }

});

const handleErrors = (err) =>{

    let errors = {email:'', password:'', username:''};
    let field;
    if(err.code === 11000){

        field=(Object.keys(Object.values(err)[4]));


        if(field.length === 1){

            if(field[0]==='username'){
            errors.username = 'This username is already in use'

            }else if(field[0]==='email'){
            errors.email='This email already registered'
            }
        }else if(field.includes('username')){
            errors.username = 'This username is already in use'
        }else if(field.includes('email')){
            errors.email='This email already registered'
        }
    }else{
        console.log(err.errors.username);
        if(err.errors.username){
            errors.username=err.errors.username.message
        }
        if(err.errors.email){
            errors.email=err.errors.email.message
        }
        if(err.errors.password){
            errors.password=err.errors.password.message
        }



            
        }

  
        return errors;

}

const handleErrors1 =(err)=>{
    
    let errors = {email:"", password:""}
    if(err.message === 'incorrect email'){
        console.log("yes")
        errors.email=err.message
    }
    if(err.message === 'incorrect password'){
        console.log("yes")
        errors.password=err.message
    }
    return errors
}


var now = new Date();
var time = now.getTime();
var expireTime = time + 1000*36000

const createToken = (id) =>{
    return jwt.sign({ id }, 'soham post application secret',{
        expiresIn: expireTime
    });
};

let errors

app.post('/login', async (req, res) =>{
    const { email, password } = req.body;
    try{
        const user = await User.login(email, password);
        const token = createToken(user._id);
        res.send(token);
        res.status(200).json({user: user._id})
    }
    catch (err){

        errors = handleErrors1(err);

        res.status(201).json({errors:errors});
    }
});

app.post('/auth', async (req,res) =>{
    const token = req.body.token;


    let auth;
    jwt.verify(token, 'soham post application secret', async (err, decodedToken)=>{
        if(err){
            console.log("false")
            auth = "false"
            res.send(auth)

        }else{
            let user =  await User.findById(decodedToken.id)

            auth = "true"
            res.send(user)
        }
    })
})




app.post('/create', (req,res)=>{
    const timeDue = req.body.timeDue
    const username = req.body.username
    const title = req.body.title;
    const desc = req.body.desc;
    const priority = req.body.priority;
    const status = "assigned"

    const newTask = new Task({

        username,
        title,
        desc,
        timeDue,
        priority,
        status
        
    });

    newTask.save()
    .then(result=>{
        console.log("posted");
        res.end("done");
    })
    .catch(err=>{
        console.log(err);
    })
});

app.get('/tasks', (req, res)=>{
    Task.find()
    .then(foundtasks=>{
        res.json(foundtasks)
    })
})

app.post("/complete", (req,res)=>{
    let id = req.body.id
    Task.findById(id)
    .then(res=>{
        let task = res
        if(task.timeDue-Date.now()>0){
            task.status = "completed"
        }else if(task.timeDue-Date.now()<=0){
            task.status = "completed-late"
        }

        task.save()
        .then(res=>{
            console.log(res)
        })
        .catch(err=>{
            console.log(err)
        })
    })
})

app.post("/delete", (req,res)=>{
    let id = req.body.id
    Task.findByIdAndDelete(id)
    .then(res=>{
        console.log(res)
    })
    .catch(err=>{
        console.log(err)
    })
})

app.listen(process.env.PORT || 3001, ()=>{
    console.log("express running is localhost 3001");
})
