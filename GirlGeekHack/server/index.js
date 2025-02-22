import mongoose from "mongoose"
import express from "express"
import cors from "cors"
import dotenv from "dotenv"



dotenv.config()
const app = express()
// app.use(bodyParser.urlencoded({
//   extended: true
// }));
// app.use(bodyParser.json());
// app.use(cors())

// app.use('/blogs' , routes)
// app.use('/create' , createroutes)

app.get('/' , (req , res) => {
  res.send("hey")
})

const PORT = process.env.PORT || 6000
const URL = process.env.URL
main().catch(err => console.log(err));

async function main() {
  await mongoose.connect(URL);
}
app.listen( PORT , () => {
    console.log(`Server is running on ${PORT}`);
})


// const server = app.listen(process.env.PORT || 5000, () => {
//   const port = server.address().port;
//   console.log(`Express is working on port ${port}`);
// });