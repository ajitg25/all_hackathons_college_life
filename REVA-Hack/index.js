const express = require('express');
const app = express();
require('dotenv').config();
const port = 3000
const bodyParser = require("body-parser");
const path = require('path');
// const fs = require('fs');


// const loc = require(__dirname + "/location.js");
// const nodeWebCam = require('node-webcam');


// function get_location(){
//   var cur_loc = loc.getLoc();
//   return cur_loc;
// }

const { auth, requiresAuth} = require('express-openid-connect');
app.use(
  auth({
    authRequired : false,
    auth0Logout: true,
    issuerBaseURL:process.env.ISSUER_BASE_URL ,
    baseURL: process.env.BASE_URL,
    clientID:process.env.CLIENT_ID ,
    secret: process.env.SECRET ,
    idpLogout: true,
  })
);


app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')))


app.get('/', (req, res) => {
  if(req.oidc.isAuthenticated()){
    res.sendFile(path.join(__dirname+'/login.html'));

  }
  else{
    res.redirect('http://localhost:3000/login');
  }
  // res.sendFile(req.oidc.isAuthenticated() ? path.join(__dirname+'/login.html') : "logged out")
})

app.get('/callback', (req, res) => {
  res.send('Hello Callback!')

})
app.get('/success', (req, res) => {
  res.send('SUCCESS!')

})

var LoggedInAs = ""

app.post("/home", function(req, res){
  console.log(req.body);
  LoggedInAs = req.body.loginas;
  console.log(LoggedInAs)
  if(LoggedInAs=='Rider'){
    res.sendFile(path.join(__dirname+'/srequest.html'));

  }
  else{
    res.send("Driver SIde")
  }
});

app.get("/home", function(req, res){
  console.log(req.body);
  LoggedInAs = req.body.loginas;
  console.log(LoggedInAs)
  if(LoggedInAs=='Rider'){
    res.sendFile(path.join(__dirname+'/srequest.html'));

  }
  else{
    res.send("Driver Side")
  }
});


app.post("/SetDest", function(req, res){
  console.log(req.body);
  // const c = captureShot().then((response) => { 
  //         // Whatever we resolve in captureShot, that's what response will contain
  //          res.send('<img src="${response}"/>')
  //       })

 
  res.sendFile(path.join(__dirname+'/waiting.html'));


  
});

app.get("/paym", function(req,res){
  res.sendFile(path.join(__dirname+'/payment.html'));
})

// function payments(){
//   console.log("dsds");
//   res.redirect('http://localhost:3000/paym');
// }


app.get("/SetDest", function(req, res){
  console.log("DS")
    res.redirect('http://localhost:3000/logout');

  
});

app.post('/cam', (req, res) => {
  console.log(req.body);
    //  const c = captureShot('robin').then((response) => { 
    //       // Whatever we resolve in captureShot, that's what response will contain
    //        res.send('<img src="${response}"/>')
    //   })
  

})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})