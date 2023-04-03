import express from "express";
import {
  RECOMMENDATION_MICROSERVICE_URL,
  TICKETING_MICROSERVICE_URL,
} from "./config.js";
//import function from models.js
import {
  getConcertById,
  getAllConcertData,
  updateConcertStatus,
} from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";
import axios from 'axios';


const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//get all concerts
app.get("/", async (req, res) => {
  const concerts = await getAllConcertData();
  const userId = req.query.userid;
   console.log(userId)
  if (userId) {
    const recommended = await axios.get(
      `${RECOMMENDATION_MICROSERVICE_URL}/${userId}`
    );
    return res.json({ concerts: concerts, recommended: recommended.data });
  }
  return res.json({concerts:concerts,recommended:null})
 });


 //get concert by id and checks status
app.get("/concert/:id", async (req, res) => {
  const id = req.params.id;
  const result = await getConcertById(id);
  const concert = result.data;
  if (concert[0].status && concert[0].status === "closed") {
    res.json(concert);
    return;
  }
  if (concert[0].status && concert[0].status.includes("available")) {
    try {
      const {
        data: { status },
      } = await axios.get(`${TICKETING_MICROSERVICE_URL}/${id.toString()}`);
      if (status.includes("sold out")) {
        await updateConcertStatus(id, status);
        concert[0].status = status;
      }
    } catch (err) {
      console.log(err);
    }
  }
  res.json(concert);
});

//PORT
app.listen(5005, () => {
  console.log("Server is running on port 5005");
});
