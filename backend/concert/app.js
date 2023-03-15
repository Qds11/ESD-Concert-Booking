import express from "express";

//import function from models.js
import { getConcertById, getAllConcertData } from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//get all spending data
app.get("/", async (req, res) => {
  const concerts = await getAllConcertData();
  return res.json(concerts);
});

// //get spending data filtered by date range
app.get("/concert/:id", async (req, res) => {

  const id = req.params.id;
  const concert = await getConcertById(id);
  res.json(concert);
});

//PORT
app.listen(5005, () => {
  console.log("Server is running on port 5000");
});
